import subprocess
import json

namespace = "default"

# Create a CSV header
header = "Deployment_name,Namespace,Replicas,MemoryLimits,CpuLimits,MemoryRequests,CpuRequests\n"
with open("deploy_info.csv", "w") as csv_file:
    csv_file.write(header)

# Get the deployment information in JSON format
deploy_info_json = subprocess.check_output(["kubectl", "get", "deploy", "-n", namespace, "-o", "json"])
deploy_info = json.loads(deploy_info_json)

print(deploy_info)

# Loop through each deploy
for deploy in deploy_info["items"]:
    deploy_name = deploy["metadata"]["name"]

    # Initialize default values
    memory_limits = "N/A"
    cpu_limits = "N/A"
    memory_requests = "N/A"
    cpu_requests = "N/A"
    replicas = "N/A"

    replicas = deploy["spec"].get("replicas", "N/A")


    # Loop through containers defined in the "spec" block
    for container in deploy["spec"]["template"]["spec"]["containers"]:
        resource_limits = container["resources"]["limits"]
        memory_limits = resource_limits.get("memory", "N/A")
        cpu_limits = resource_limits.get("cpu", "N/A")

        resource_requests = container["resources"]["requests"]
        memory_requests = resource_requests.get("memory", "N/A")
        cpu_requests = resource_requests.get("cpu", "N/A")


    print(f"{deploy_name},{namespace},{replicas},{memory_limits},{cpu_limits},{memory_requests},{cpu_requests}\n")

    # Write to CSV file
    with open("deploy_info.csv", "a") as csv_file:
        csv_file.write(f"{deploy_name},{namespace},{replicas},{memory_limits},{cpu_limits},{memory_requests},{cpu_requests}\n")

print("CSV file 'deploy_info.csv' created.")