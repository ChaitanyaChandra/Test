import ansible_runner
import pandas as pd

r = ansible_runner.run(private_data_dir='./', inventory="/Users/chandra/Documents/Test/ansible-runner/inv.ini", playbook='ansible-playbooks/main.yml', extravars={"my_hosts": "nodes"})
nodes = ["node1.chaitu.net", "node2.chaitu.net", "node3.chaitu.net", "node5.chaitu.net"]
df = pd.DataFrame({f"nodes": nodes})
data={}
for host in nodes:
    facts = r.get_fact_cache(host)
    # print(f"Facts for {host}:")
    response = facts.get('response', 'unreachible')
    # print(response)
    data[host]=response

df['check version'] = df['nodes'].map(data)

# print(df)
df.to_csv("hello.csv", index=False)