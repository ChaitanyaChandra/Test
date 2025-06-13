import ansible_runner
from kubernetes import client, config
import pandas as pd
import os



pwd = os.getcwd()
isquiet = False

invoke_ansible = ansible_runner.run(
    private_data_dir=f"{pwd}/",
    # inventory=f"{pwd}/files/inventries/{cluster}.ini",
    playbook=f"ansible-playbooks/label.yaml",
    envvars={'ANSIBLE_FORKS': 10, 'ANSIBLE_RETRIES': 3, 'ANSIBLE_SSH_TIMEOUT': 60, 'ANSIBLE_COMMAND_TIMEOUT': 100},
    extravars={'my_hosts': 'localhost' },
    quiet=isquiet)

# print(invoke_ansible['localhost'])

