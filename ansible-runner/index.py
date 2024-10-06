import ansible_runner
import pandas as pd
import os

pwd = os.getcwd()

r = ansible_runner.run(private_data_dir='./', inventory=f"{pwd}/ansible-runner/inv.ini", playbook='ansible-playbooks/async.yml', extravars={"my_hosts": "nodes"}, quiet=False)

# facts = r.get_fact_cache("localhost")
# # print(f"Facts for {host}:")
# response = facts.get('response', 'unreachible')
# # print(response)
# data[host]=response
#
# df['check version'] = df['nodes'].map(data)
#
# print(df)
# df.to_csv("hello.csv", index=False)