import logging
import requests


def send_collect_ranks_stack_request(url, job_name, nodes_list):
    logging.debug('collect ranks stack start!')

    headers = {
        "Content-type": "application/json"
    }
    data = {
        'jobName': job_name,
        'nodesList': nodes_list
    }
    try:
        resp = requests.post(url, json=data, headers=headers, timeout=60)
        logging.info(f"Returns: {resp}")
        return resp.json()
    except Exception as e:
        logging.warning(f"{e}")
        return None
