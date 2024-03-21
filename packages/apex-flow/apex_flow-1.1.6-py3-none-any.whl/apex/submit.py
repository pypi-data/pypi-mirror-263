import glob
import os.path
import tempfile
from typing import Type
from multiprocessing import Pool
from dflow import config, s3_config
from dflow.python import OP
from monty.serialization import loadfn
import fpop, dpdata, apex, phonolammps
from apex.utils import get_task_type, get_flow_type
from apex.config import Config
from apex.flow import FlowFactory


def judge_flow(parameter, specify) -> (Type[OP], str, str, dict, dict):
    # identify type of flow and input parameter file
    num_args = len(parameter)
    if num_args == 1:
        task, run_op = get_task_type(loadfn(parameter[0]))
        flow = get_flow_type(loadfn(parameter[0]))
        task_type = task
        if flow == 'relax':
            flow_type = 'relax'
            if specify in ['props', 'joint']:
                raise RuntimeError(
                    'relaxation json file argument provided! Please check your jason file.'
                )
            relax_param = parameter[0]
            props_param = None
        elif flow == 'props':
            if specify in ['relax', 'joint']:
                raise RuntimeError(
                    'property test json file argument provided! Please check your jason file.'
                )
            flow_type = 'props'
            relax_param = None
            props_param = parameter[0]
        else:
            if specify == 'relax':
                flow_type = 'relax'
            elif specify == 'props':
                flow_type = 'props'
            else:
                flow_type = 'joint'
            relax_param = parameter[0]
            props_param = parameter[0]

    elif num_args == 2:
        task1, run_op1 = get_task_type(loadfn(parameter[0]))
        flow1 = get_flow_type(loadfn(parameter[0]))
        task2, run_op2 = get_task_type(loadfn(parameter[1]))
        flow2 = get_flow_type(loadfn(parameter[1]))
        if not flow1 == flow2:
            if specify == 'relax':
                flow_type = 'relax'
            elif specify == 'props':
                flow_type = 'props'
            else:
                flow_type = 'joint'
            if flow1 == 'relax' and flow2 == 'props':
                relax_param = parameter[0]
                props_param = parameter[1]
            elif flow1 == 'props' and flow2 == 'relax':
                relax_param = parameter[1]
                props_param = parameter[0]
            else:
                raise RuntimeError(
                    'confusion of jason arguments provided: '
                    'joint type of jason conflicts with the other json argument'
                )
        else:
            raise RuntimeError('Same type of input json files')
        if task1 == task2:
            task_type = task1
            run_op = run_op1
        else:
            raise RuntimeError('interaction types given are not matched')
    else:
        raise ValueError('A maximum of two input arguments is allowed')

    return run_op, task_type, flow_type, relax_param, props_param


def submit(
        flow,
        flow_type,
        work_dir,
        relax_param,
        props_param,
        conf=config,
        s3_conf=s3_config,
        labels=None,
):
    # reset dflow global config for sub-processes
    config.update(conf)
    s3_config.update(s3_conf)

    if flow_type == 'relax':
        flow.submit_relax(
            work_dir=work_dir,
            relax_parameter=relax_param,
            labels=labels
        )
    elif flow_type == 'props':
        flow.submit_props(
            work_dir=work_dir,
            props_parameter=props_param,
            labels=labels
        )
    elif flow_type == 'joint':
        flow.submit_joint(
            work_dir=work_dir,
            props_parameter=props_param,
            relax_parameter=relax_param,
            labels=labels
        )


def submit_workflow(
        parameter,
        config_file,
        work_dir,
        flow_type,
        is_debug=False,
        labels=None
):
    try:
        config_dict = loadfn(config_file)
    except FileNotFoundError:
        raise FileNotFoundError(
            'Please prepare global.json under current work direction '
            'or use optional argument: -c to indicate a specific json file.'
        )
    # config dflow_config and s3_config
    wf_config = Config(**config_dict)
    wf_config.config_dflow(wf_config.dflow_config_dict)
    wf_config.config_bohrium(wf_config.bohrium_config_dict)
    wf_config.config_s3(wf_config.dflow_s3_config_dict)
    # set pre-defined dflow debug mode settings
    if is_debug:
        tmp_work_dir = tempfile.TemporaryDirectory()
        config["mode"] = "debug"
        config["debug_workdir"] = config_dict.get("debug_workdir", tmp_work_dir.name)
        s3_config["storage_client"] = None

    # judge basic flow info from user indicated parameter files
    (run_op, calculator, flow_type,
     relax_param, props_param) = judge_flow(parameter, flow_type)
    print(f'Running APEX calculation via {calculator}')
    print(f'Submitting {flow_type} workflow...')
    make_image = wf_config.basic_config_dict["apex_image_name"]
    run_image = wf_config.basic_config_dict[f"{calculator}_image_name"]
    if not run_image:
        run_image = wf_config.basic_config_dict["run_image_name"]
    run_command = wf_config.basic_config_dict[f"{calculator}_run_command"]
    if not run_command:
        run_command = wf_config.basic_config_dict["run_command"]
    post_image = make_image
    group_size = wf_config.basic_config_dict["group_size"]
    pool_size = wf_config.basic_config_dict["pool_size"]
    executor = wf_config.get_executor(wf_config.dispatcher_config_dict)
    upload_python_packages = wf_config.basic_config_dict["upload_python_packages"]
    upload_python_packages.extend(list(apex.__path__))
    upload_python_packages.extend(list(fpop.__path__))
    upload_python_packages.extend(list(dpdata.__path__))
    upload_python_packages.extend(list(phonolammps.__path__))

    flow = FlowFactory(
        make_image=make_image,
        run_image=run_image,
        post_image=post_image,
        run_command=run_command,
        calculator=calculator,
        run_op=run_op,
        group_size=group_size,
        pool_size=pool_size,
        executor=executor,
        upload_python_packages=upload_python_packages
    )
    # submit the workflows
    work_dir_list = []
    for ii in work_dir:
        glob_list = glob.glob(os.path.abspath(ii))
        work_dir_list.extend(glob_list)
    if len(work_dir_list) > 1:
        n_processes = len(work_dir_list)
        pool = Pool(processes=n_processes)
        print(f'submitting via {n_processes} processes...')
        for ii in work_dir_list:
            res = pool.apply_async(
                submit,
                (flow, flow_type, ii, relax_param, props_param, config, s3_config, labels)
            )
        pool.close()
        pool.join()
    elif len(work_dir_list) == 1:
        submit(flow, flow_type, work_dir_list[0], relax_param, props_param, labels=labels)
    else:
        raise RuntimeError('Empty work directory indicated, please check your argument')

    print('Completed!')
