import ansible_runner
r = ansible_runner.run(private_data_dir='./', inventory="/Users/chandra/Documents/Test/ansible-runner/inv.ini", playbook='ansible-playbooks/main.yml', extravars={"my_hosts": "nodes"})
inventory_hosts = ["node1.chaitu.net", "node2.chaitu.net"]  # Replace 'all' with your group if needed
for host in inventory_hosts:
    facts = r.get_fact_cache(host)
    print(f"Facts for {host}:")
    playbook_message = facts.get('playbook_message', 'insync')
    print(playbook_message)

print(r.status)