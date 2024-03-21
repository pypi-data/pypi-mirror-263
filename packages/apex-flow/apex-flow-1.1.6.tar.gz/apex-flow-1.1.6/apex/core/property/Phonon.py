import glob
import json
import logging
import os
import shutil
import re
import subprocess
import dpdata
from pathlib import Path
from pymatgen.core.structure import Structure

from apex.core.structure import StructureInfo
from apex.core.calculator.calculator import LAMMPS_TYPE
from apex.core.calculator.lib import abacus_utils
from apex.core.calculator.lib import vasp_utils
from apex.core.property.Property import Property
from apex.core.refine import make_refine
from apex.core.reproduce import make_repro, post_repro
from dflow.python import upload_packages
upload_packages.append(__file__)


class Phonon(Property):
    def __init__(self, parameter, inter_param=None):
        parameter["reproduce"] = parameter.get("reproduce", False)
        self.reprod = parameter["reproduce"]
        if not self.reprod:
            if not ("init_from_suffix" in parameter and "output_suffix" in parameter):
                self.primitive = parameter.get('primitive', False)
                self.approach = parameter.get('approach', 'linear')
                self.supercell_size = parameter.get('supercell_size', [2, 2, 2])
                self.MESH = parameter.get('MESH', None)
                self.PRIMITIVE_AXES = parameter.get('PRIMITIVE_AXES', None)
                self.BAND = parameter.get('BAND', None)
                self.BAND_POINTS = parameter.get('BAND_POINTS', None)
                self.BAND_CONNECTION = parameter.get('BAND_CONNECTION', True)
            parameter["cal_type"] = parameter.get("cal_type", "relaxation")
            self.cal_type = parameter["cal_type"]
            default_cal_setting = {
                "relax_pos": True,
                "relax_shape": False,
                "relax_vol": False,
            }
            if "cal_setting" not in parameter:
                parameter["cal_setting"] = default_cal_setting
            else:
                if "relax_pos" not in parameter["cal_setting"]:
                    parameter["cal_setting"]["relax_pos"] = default_cal_setting[
                        "relax_pos"
                    ]
                if "relax_shape" not in parameter["cal_setting"]:
                    parameter["cal_setting"]["relax_shape"] = default_cal_setting[
                        "relax_shape"
                    ]
                if "relax_vol" not in parameter["cal_setting"]:
                    parameter["cal_setting"]["relax_vol"] = default_cal_setting[
                        "relax_vol"
                    ]
            self.cal_setting = parameter["cal_setting"]
        else:
            parameter["cal_type"] = "static"
            self.cal_type = parameter["cal_type"]
            default_cal_setting = {
                "relax_pos": False,
                "relax_shape": False,
                "relax_vol": False,
            }
            if "cal_setting" not in parameter:
                parameter["cal_setting"] = default_cal_setting
            else:
                if "relax_pos" not in parameter["cal_setting"]:
                    parameter["cal_setting"]["relax_pos"] = default_cal_setting[
                        "relax_pos"
                    ]
                if "relax_shape" not in parameter["cal_setting"]:
                    parameter["cal_setting"]["relax_shape"] = default_cal_setting[
                        "relax_shape"
                    ]
                if "relax_vol" not in parameter["cal_setting"]:
                    parameter["cal_setting"]["relax_vol"] = default_cal_setting[
                        "relax_vol"
                    ]
            self.cal_setting = parameter["cal_setting"]
            parameter["init_from_suffix"] = parameter.get("init_from_suffix", "00")
            self.init_from_suffix = parameter["init_from_suffix"]
        self.parameter = parameter
        self.inter_param = inter_param if inter_param is not None else {"type": "vasp"}

    def make_confs(self, path_to_work, path_to_equi, refine=False):
        path_to_work = os.path.abspath(path_to_work)
        if os.path.exists(path_to_work):
            #dlog.warning("%s already exists" % path_to_work)
            logging.warning("%s already exists" % path_to_work)
        else:
            os.makedirs(path_to_work)
        path_to_equi = os.path.abspath(path_to_equi)

        if "start_confs_path" in self.parameter and os.path.exists(
            self.parameter["start_confs_path"]
        ):
            init_path_list = glob.glob(
                os.path.join(self.parameter["start_confs_path"], "*")
            )
            struct_init_name_list = []
            for ii in init_path_list:
                struct_init_name_list.append(ii.split("/")[-1])
            struct_output_name = path_to_work.split("/")[-2]
            assert struct_output_name in struct_init_name_list
            path_to_equi = os.path.abspath(
                os.path.join(
                    self.parameter["start_confs_path"],
                    struct_output_name,
                    "relaxation",
                    "relax_task",
                )
            )

        task_list = []
        cwd = os.getcwd()

        if self.reprod:
            print("phonon reproduce starts")
            if "init_data_path" not in self.parameter:
                raise RuntimeError("please provide the initial data path to reproduce")
            init_data_path = os.path.abspath(self.parameter["init_data_path"])
            task_list = make_repro(
                self.inter_param,
                init_data_path,
                self.init_from_suffix,
                path_to_work,
                self.parameter.get("reprod_last_frame", True),
            )
            os.chdir(cwd)

        else:
            if refine:
                print("phonon refine starts")
                task_list = make_refine(
                    self.parameter["init_from_suffix"],
                    self.parameter["output_suffix"],
                    path_to_work,
                )
                os.chdir(cwd)

            else:
                if self.inter_param["type"] == "abacus":
                    CONTCAR = abacus_utils.final_stru(path_to_equi)
                    POSCAR = "STRU"
                else:
                    CONTCAR = "CONTCAR"
                    POSCAR = "POSCAR"

                equi_contcar = os.path.join(path_to_equi, CONTCAR)
                if not os.path.exists(equi_contcar):
                    raise RuntimeError("please do relaxation first")

                if self.inter_param["type"] == "abacus":
                    stru = dpdata.System(equi_contcar, fmt="stru")
                    stru.to("contcar", "CONTCAR.tmp")
                    ptypes = vasp_utils.get_poscar_types("CONTCAR.tmp")
                    ss = Structure.from_file("CONTCAR.tmp")
                    os.remove("CONTCAR.tmp")
                else:
                    ptypes = vasp_utils.get_poscar_types(equi_contcar)
                    ss = Structure.from_file(equi_contcar)
                    # gen structure

                # get user input parameter for specific structure
                st = StructureInfo(ss)
                self.structure_type = st.lattice_structure
                type_param = self.parameter.get(self.structure_type, None)
                if type_param:
                    self.primitive = type_param.get("primitive", self.primitive)
                    self.approach = type_param.get("approach", self.approach)
                    self.supercell_size = type_param.get("supercell_size", self.supercell_size)
                    self.MESH = type_param.get("MESH", self.MESH)
                    self.PRIMITIVE_AXES = type_param.get("PRIMITIVE_AXES", self.PRIMITIVE_AXES)
                    self.BAND = type_param.get("BAND", self.BAND)
                    self.BAND_POINTS = type_param.get("BAND_POINTS", self.BAND_POINTS)
                    self.BAND_CONNECTION = type_param.get("BAND_CONNECTION", self.BAND_CONNECTION)

                os.chdir(path_to_work)
                if os.path.isfile(POSCAR):
                    os.remove(POSCAR)
                if os.path.islink(POSCAR):
                    os.remove(POSCAR)
                os.symlink(os.path.relpath(equi_contcar), POSCAR)
                #           task_poscar = os.path.join(output, 'POSCAR')

                if not self.BAND:
                    raise RuntimeError('No band_path input for phonon calculation!')
                ret = ""
                ret += "ATOM_NAME ="
                for ii in ptypes:
                    ret += " %s" % ii
                ret += "\n"
                ret += "DIM = %s %s %s\n" % (
                    self.supercell_size[0],
                    self.supercell_size[1],
                    self.supercell_size[2]
                )
                if self.MESH:
                    ret += "MESH = %s %s %s\n" % (
                        self.MESH[0], self.MESH[1], self.MESH[2]
                    )
                if self.PRIMITIVE_AXES:
                    ret += "PRIMITIVE_AXES = %s\n" % self.PRIMITIVE_AXES
                ret += "BAND = %s\n" % self.BAND
                if self.BAND_POINTS:
                    ret += "BAND_POINTS = %s\n" % self.BAND_POINTS
                if self.BAND_CONNECTION:
                    ret += "BAND_CONNECTION = %s\n" % self.BAND_CONNECTION

                ret_force_read = ret + "FORCE_CONSTANTS=READ\n"

                task_list = []
                # ------------make for abacus---------------
                if self.inter_param["type"] == "abacus":
                    # make setting.conf
                    ret_sc = ""
                    ret_sc += "DIM=%s %s %s\n" % (
                        self.supercell_size[0],
                        self.supercell_size[1],
                        self.supercell_size[2]
                    )
                    ret_sc += "ATOM_NAME ="
                    for atom in ptypes:
                        ret_sc += " %s" % (atom)
                    ret_sc += "\n"
                    with open("setting.conf", "a") as fp:
                        fp.write(ret_sc)
                    # append NUMERICAL_ORBITAL to STRU after relaxation
                    orb_file = self.inter_param.get("orb_files", None)
                    abacus_utils.append_orb_file_to_stru("STRU", orb_file, prefix='pp_orb')
                    ## generate STRU-00x
                    cmd = "phonopy setting.conf --abacus -d"
                    subprocess.call(cmd, shell=True)

                    with open("band.conf", "a") as fp:
                        fp.write(ret)
                    # generate task.000*
                    stru_list = glob.glob("STRU-0*")
                    for ii in range(len(stru_list)):
                        task_path = os.path.join(path_to_work, 'task.%06d' % ii)
                        os.makedirs(task_path, exist_ok=True)
                        os.chdir(task_path)
                        task_list.append(task_path)
                        os.symlink(os.path.join(path_to_work, stru_list[ii]), 'STRU')
                        os.symlink(os.path.join(path_to_work, 'STRU'), 'STRU.ori')
                        os.symlink(os.path.join(path_to_work, 'band.conf'), 'band.conf')
                        os.symlink(os.path.join(path_to_work, 'phonopy_disp.yaml'), 'phonopy_disp.yaml')
                        try:
                            os.symlink(os.path.join(path_to_work, 'KPT'), 'KPT')
                        except:
                            pass
                    os.chdir(cwd)
                    return task_list

                # ------------make for vasp and lammps------------
                if self.primitive:
                    subprocess.call('phonopy --symmetry', shell=True)
                    subprocess.call('cp PPOSCAR POSCAR', shell=True)
                    shutil.copyfile("PPOSCAR", "POSCAR-unitcell")
                else:
                    shutil.copyfile("POSCAR", "POSCAR-unitcell")

                # make tasks
                if self.inter_param["type"] == 'vasp':
                    cmd = "phonopy -d --dim='%d %d %d' -c POSCAR" % (
                        int(self.supercell_size[0]),
                        int(self.supercell_size[1]),
                        int(self.supercell_size[2])
                    )
                    subprocess.call(cmd, shell=True)
                    # linear response method
                    if self.approach == 'linear':
                        task_path = os.path.join(path_to_work, 'task.000000')
                        os.makedirs(task_path, exist_ok=True)
                        os.chdir(task_path)
                        task_list.append(task_path)
                        os.symlink(os.path.join(path_to_work, "SPOSCAR"), "POSCAR")
                        os.symlink(os.path.join(path_to_work, "POSCAR-unitcell"), "POSCAR-unitcell")
                        with open("band.conf", "a") as fp:
                            fp.write(ret_force_read)
                    # finite displacement method
                    elif self.approach == 'displacement':
                        poscar_list = glob.glob("POSCAR-0*")
                        for ii in range(len(poscar_list)):
                            task_path = os.path.join(path_to_work, 'task.%06d' % ii)
                            os.makedirs(task_path, exist_ok=True)
                            os.chdir(task_path)
                            task_list.append(task_path)
                            os.symlink(os.path.join(path_to_work, poscar_list[ii]), 'POSCAR')
                            os.symlink(os.path.join(path_to_work, "POSCAR-unitcell"), "POSCAR-unitcell")

                        os.chdir(path_to_work)
                        with open("band.conf", "a") as fp:
                            fp.write(ret)
                        shutil.copyfile("band.conf", "task.000000/band.conf")
                        shutil.copyfile("phonopy_disp.yaml", "task.000000/phonopy_disp.yaml")

                    else:
                        raise RuntimeError(
                            f'Unsupported phonon approach input: {self.approach}. '
                            f'Please choose from "linear" and "displacement".'
                        )
                    os.chdir(cwd)
                    return task_list
                # ----------make for lammps-------------
                elif self.inter_param["type"] in LAMMPS_TYPE:
                    task_path = os.path.join(path_to_work, 'task.000000')
                    os.makedirs(task_path, exist_ok=True)
                    os.chdir(task_path)
                    task_list.append(task_path)
                    os.symlink(os.path.join(path_to_work, "POSCAR-unitcell"), POSCAR)

                    with open("band.conf", "a") as fp:
                        fp.write(ret_force_read)
                    os.chdir(cwd)
                    return task_list
                else:
                    raise RuntimeError(
                        f'Unsupported interaction type input: {self.inter_param["type"]}'
                    )

    def post_process(self, task_list):
        cwd = os.getcwd()
        inter_type = self.inter_param["type"]
        if inter_type in LAMMPS_TYPE:
            # prepare in.lammps
            for ii in task_list:
                os.chdir(ii)
                with open("in.lammps", 'r') as f1:
                    contents = f1.readlines()
                    for jj in range(len(contents)):
                        is_pair_coeff = re.search("pair_coeff", contents[jj])
                        if is_pair_coeff:
                            pair_line_id = jj
                            break
                    del contents[pair_line_id + 1:]

                with open("in.lammps", 'w') as f2:
                    for jj in range(len(contents)):
                        f2.write(contents[jj])
                # dump phonolammps command
                phonolammps_cmd = "phonolammps in.lammps -c POSCAR --dim %s %s %s " %(
                    self.supercell_size[0], self.supercell_size[1], self.supercell_size[2]
                )
                with open("run_command", 'w') as f3:
                    f3.write(phonolammps_cmd)
        elif inter_type == "vasp":
            pass
        elif inter_type == "abacus":
            pass
        os.chdir(cwd)

    def task_type(self):
        return self.parameter["type"]

    def task_param(self):
        return self.parameter

    def _compute_lower(self, output_file, all_tasks, all_res):
        cwd = Path.cwd()
        work_path = Path(output_file).parent.absolute()
        output_file = os.path.abspath(output_file)
        res_data = {}
        ptr_data = os.path.dirname(output_file) + "\n"

        if not self.reprod:
            os.chdir(work_path)
            if self.inter_param["type"] == 'abacus':
                shutil.copyfile("task.000000/band.conf", "band.conf")
                shutil.copyfile("task.000000/STRU.ori", "STRU")
                shutil.copyfile("task.000000/phonopy_disp.yaml", "phonopy_disp.yaml")
                os.system('phonopy -f task.0*/OUT.ABACUS/running_scf.log')
                os.system('phonopy -f task.0*/OUT.ABACUS/running_scf.log')
                if os.path.exists("FORCE_SETS"):
                    print('FORCE_SETS is created')
                else:
                    print('FORCE_SETS can not be created')
                os.system('phonopy band.conf --abacus')
                os.system('phonopy-bandplot --gnuplot band.yaml > band.dat')

            elif self.inter_param["type"] == 'vasp':
                shutil.copyfile("task.000000/band.conf", "band.conf")
                if not os.path.samefile("task.000000/POSCAR-unitcell", "POSCAR-unitcell"):
                    shutil.copyfile("task.000000/POSCAR-unitcell", "POSCAR-unitcell")

                if self.approach == "linear":
                    os.chdir(all_tasks[0])
                    assert os.path.isfile('vasprun.xml'), "vasprun.xml not found"
                    os.system('phonopy --fc vasprun.xml')
                    assert os.path.isfile('FORCE_CONSTANTS'), "FORCE_CONSTANTS not created"
                    os.system('phonopy --dim="%s %s %s" -c POSCAR-unitcell band.conf' % (
                            self.supercell_size[0],
                            self.supercell_size[1],
                            self.supercell_size[2]))
                    os.system('phonopy-bandplot --gnuplot band.yaml > band.dat')
                    print('band.dat is created')
                    shutil.copyfile("band.dat", work_path/"band.dat")

                elif self.approach == "displacement":
                    shutil.copyfile("task.000000/band.conf", "band.conf")
                    shutil.copyfile("task.000000/phonopy_disp.yaml", "phonopy_disp.yaml")
                    os.system('phonopy -f task.0*/vasprun.xml')
                    if os.path.exists("FORCE_SETS"):
                        print('FORCE_SETS is created')
                    else:
                        print('FORCE_SETS can not be created')
                    os.system('phonopy --dim="%s %s %s" -c POSCAR-unitcell band.conf' % (
                        self.supercell_size[0],
                        self.supercell_size[1],
                        self.supercell_size[2]))
                    os.system('phonopy-bandplot --gnuplot band.yaml > band.dat')

            elif self.inter_param["type"] in LAMMPS_TYPE:
                os.chdir(all_tasks[0])
                assert os.path.isfile('FORCE_CONSTANTS'), "FORCE_CONSTANTS not created"
                os.system('phonopy --dim="%s %s %s" -c POSCAR band.conf' % (
                    self.supercell_size[0], self.supercell_size[1], self.supercell_size[2])
                    )
                os.system('phonopy-bandplot --gnuplot band.yaml > band.dat')
                shutil.copyfile("band.dat", work_path/"band.dat")

        else:
            if "init_data_path" not in self.parameter:
                raise RuntimeError("please provide the initial data path to reproduce")
            init_data_path = os.path.abspath(self.parameter["init_data_path"])
            res_data, ptr_data = post_repro(
                init_data_path,
                self.parameter["init_from_suffix"],
                all_tasks,
                ptr_data,
                self.parameter.get("reprod_last_frame", True),
            )

        os.chdir(work_path)
        with open('band.dat', 'r') as f:
            ptr_data = f.read()

        result_points = ptr_data.split('\n')[1][4:]
        result_lines = ptr_data.split('\n')[2:]
        res_data[result_points] = result_lines

        with open(output_file, "w") as fp:
            json.dump(res_data, fp, indent=4)

        os.chdir(cwd)
        return res_data, ptr_data
