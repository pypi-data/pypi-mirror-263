import os.path
import click
from db.base_fuyao_db import get_job_info
from utils.fuyao_log_ali import get_fuyao_log, analyze_job_log
from config.config import NODE_LIST
from utils.utils import send_collect_ranks_stack_request


@click.group()
def cli():
    pass


@cli.command()
@click.option('--job_name', prompt='Job Name',
              help='The name of a job. Checkout a job name by "fuyao view" or "fuyao history".')
@click.option('--env', prompt='Environment', type=click.Choice(['prd', 'dev']),
              help='prd/dev. To determine which DB will be used.')
@click.option('--log_path', default='.',
              help='The path where tool will put the logs.')
# 1. 检查所有的node的log，是否有exception，分析exception
def check_log_exception(job_name, env, log_path):
    """Simple script to get & analyze job log, then return if there is an exception and corresponding details."""
    click.echo(f"Processing Job: {job_name}")

    # 1. get job info from db
    job_info, code = get_job_info(job_name, env)
    click.echo(f"Job Info: {job_info}, Code: {code}")
    if job_info is None:
        click.echo(f"Job {job_name} not found. Or DB error.")
        return

    # 2. get log data
    log_data = get_fuyao_log(job_info, log_path)

    # 3. analyze log data
    fail_info = analyze_job_log(log_data)
    click.echo(f"Fail Info: {fail_info}")


@cli.command()
# 2. 检查所有worker是否完成初始化
def check_workers_initiation():
    # 日志检测是否所有worker都完成初始化
    # build ???
    pass


@cli.command()
# 3. 检查是否有worker process 退出
def check_workers_exit():
    # 日志中有没有worker退出的信息
    # 看主进程相关的子进程有没有退出, 比较数量？？？
    pass


@cli.command()
@click.option('--job_name', prompt='Job Name',
              help='The name of a job. Checkout a job name by "fuyao view" or "fuyao history".')
@click.option('--env', prompt='Environment', type=click.Choice(['prd', 'dev']),
              help='prd/dev. To determine which DB will be used.')
@click.option('--log_path', default='.',
              help='The path where tool will put the logs.')
# 4. 自动收集所有rank的stack
def collect_ranks_stack(job_name, env, log_path):
    """Collect stack info from all ranks."""
    click.echo(f"Processing Job: {job_name}")

    # 1. get job info and nodes info
    job_info, code = get_job_info(job_name, env)
    click.echo(f"Job Info: {job_info}, Code: {code}")
    if job_info is None:
        click.echo(f"Job {job_name} not found. Or DB error.")
        return
    nodes_list = [node.strip() for node in job_info['node_list'].split(',')]
    nodes_list = ['cnwlp-gpu-p02021']
    click.echo(f"node_list: {nodes_list}")

    # 2. get pids @ all ranks
    # 2.1 get node info dict
    if len(nodes_list) == 0:
        # _, nodes_list = get_nodes_by_job(job_name)
        # 不会有job没有node_list吧？
        pass
    else:
        nodes_info_list = []
        for node in nodes_list:
            if node in NODE_LIST:
                nodes_info_list.append({
                    'pod_ip': NODE_LIST[node],
                    'node_name': node,
                })
            else:
                click.echo(f"!!! node: {node} do not exist in NODE_LIST !!!")
                return
        nodes_list = nodes_info_list
    click.echo(f"nodes_list after: {nodes_list}")

    if nodes_list is None or len(nodes_list) == 0:
        return

    # 3. get stack info from all pids
    # 3.1 判断当前集群
    cluster = job_info['site']
    url = ''
    if cluster == 'fuyao':
        url = r'http://fuyao-devop-container.xiaopeng.link/collect_ranks_stack'
    elif cluster == 'fuyao_a1':
        # TODO new dn
        url = r'http://fuyao-devop-container.xiaopeng.link/collect_ranks_stack'
    elif cluster == 'fuyao_b1':
        # TODO new dn
        url = r'http://fuyao-devop-container.xiaopeng.link/collect_ranks_stack'
    # 3.2 对相应集群的master发起调用
    data = send_collect_ranks_stack_request(url, job_name, nodes_list)
    # click.echo(f"Data: {data}")

    # 4. save stack info to file
    log_folder = f'{log_path}/log'
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    rank_data_dict = data['rank_data_dict']
    for node_name, rank_data in rank_data_dict.items():
        filename = f'{log_folder}/{node_name}.log'
        with open(filename, 'w+') as logfile:
            for line in rank_data['data']:
                logfile.write(line + '\n')


@cli.command()
# 5. 自动收集火焰图
def collect_flame_graph():
    pass


@cli.command()
# 6. 自动检查设备是否出现异常；分析是否存在硬件告警及报错（syslog）
def check_device():
    pass


if __name__ == '__main__':
    cli()
