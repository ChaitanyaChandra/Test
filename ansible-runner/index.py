import ansible_runner
from kubernetes import client, config
import pandas as pd
import os
from halo import Halo
import time
import sys
import send_email


pwd = os.getcwd()

drifted_clusters = set()
isquiet = True

system_csv_col = {
    "os_version_check" : "RedHat OS Version status",
    "kernel_check" : "kernel status"
}

cluster_nodes = {
    'main' : ["cp.durgasri.in", "node1.durgasri.in", "node2.durgasri.in"],
    'master' : ["master.chaitu.net", "node1.chaitu.net"]
}

global_system_df =  pd.DataFrame({"items": list(system_csv_col.values())})
clusters = ['main', 'master']
for cluster in clusters:
    system_df =  pd.DataFrame({f"{cluster} Nodes":  cluster_nodes[cluster]})
    def invoke_ansible_system_playbook():
        if  isquiet:
            start_time = time.time()
            spinner = Halo(text=f"Current Cluster: {cluster}, Running System playbooks..", spinner='dots')
            spinner.start()
        invoke_ansible = ansible_runner.run(
            private_data_dir=f"{pwd}/",
            inventory=f"{pwd}/files/inventries/{cluster}.ini",
            playbook=f"ansible-playbooks/main.yml",
            envvars={'ANSIBLE_FORKS': 10, 'ANSIBLE_RETRIES': 3, 'ANSIBLE_SSH_TIMEOUT': 60, 'ANSIBLE_COMMAND_TIMEOUT': 100},
            extravars={'my_hosts': 'all' },
            quiet=isquiet)
        for key, value in system_csv_col.items():
            data = {}
            for host in cluster_nodes[cluster]:
                facts = invoke_ansible.get_fact_cache(host)
                data[host] = facts.get(f"{key}_response", 'unreachable')
            system_df[value] = system_df[f"{cluster} Nodes"].map(data)
        if  isquiet:
            execution_time = time.time() - start_time
            minutes = int(execution_time // 60)
            seconds = int(execution_time % 60)
            spinner.stop()
            print("\033[32m\u2713\033[0m" + f"Current Cluster: {cluster}, System playbooks completed in {minutes}:{seconds}.")


    invoke_ansible_system_playbook()
    system_df.to_csv(f"{pwd}/files/csv/system_{cluster}.csv", index=False)
    # print(system_df)



    ###################### GENERATE CONSOLIDATED FILE  ##################################

    def generate_consolidated_file():
        with open(f"{pwd}/files/consolidated/{cluster}.txt", "w") as file:
            # system components

            for key, value  in system_csv_col.items():
                file.write(f"\n\n{value}\n-----------------------------------------------------------\n")
                system_components_drifted = system_df[system_df[value] != "insync"]
                for index, row in system_df.iterrows():
                    if system_components_drifted.empty:
                        file.write(f"insync\n")
                        break
                    elif row[value] == "insync":
                        pass
                    else:
                        file.write(f"{row[f"{cluster} Nodes"]} --> {row[value]}\n")

    generate_consolidated_file()

    # For each system check, calculate drift summary
    status_dict = {}
    for item in system_csv_col.values():
        total_nodes = system_df.shape[0]
        insync_count = (system_df[item] == "insync").sum()
        drifted_count = total_nodes - insync_count

        if drifted_count == 0:
            status = "insync"
        else:
            status = f"drifted ({drifted_count} node{'s' if drifted_count > 1 else ''})"

        status_dict[item] = status

    # Map this dict to the global dataframe's 'items' column
    global_system_df[cluster] = global_system_df["items"].map(status_dict)

    global_system_df[cluster] = global_system_df[cluster].apply(
        lambda x: f'<span style="color:red;">{x}</span>' if str(x).startswith("drifted") else x
    )

print(global_system_df)
###################### SEND EMAIL  ##################################
k8s_table = global_system_df.to_html(escape=False, index=False)
folder_path = f"{pwd}/files/consolidated/"
zip_name = 'attachments.zip'
body_data = f"<p>Please find the summary of drifted configuration information.</p>"

body = f"""
<html>
<body>
    <p>Team,</p>
    {body_data}
    <h3 style="color:gray;"><b>1) Cluster Report:</b></h3>
    <h3 style="color:gray;"><b>2) System Components Report:</b></h3>
    {k8s_table}
    <br>
    <p>Regards,<br>HCC Kubernetes Team.</p>
</body>
</html>
"""

folder_path = f"{pwd}/files/consolidated/"
zip_name = 'attachments.zip'
send_email.zip_txt_files(folder_path, zip_name)
send_email.send_email(zip_name, body)

