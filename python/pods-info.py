import subprocess
import json


# Create a CSV header
header = "Pod,RestartCount,MemoryLimits,CpuLimits,MemoryRequests,CpuRequests,podCreationTimeStamp,container_started_at,container_terminated_at,exit_code,message,reason\n"
with open("pods_info.csv", "w") as csv_file:
    csv_file.write(header)

# Get the pod information in JSON format
pod_info_json = subprocess.check_output(["kubectl", "get", "pods", "-n", "default", "-o", "json"])
pod_info = json.loads(pod_info_json)

# print(pod_info)

# Loop through each pod
for pod in pod_info["items"]:
    pod_name = pod["metadata"]["name"]

    # Initialize default values
    memory_limits = "N/A"
    cpu_limits = "N/A"
    memory_requests = "N/A"
    cpu_requests = "N/A"
#     resource_name = "N/A"
    restart_count = "N/A"
    exit_code = "N/A"
    started_at = "N/A"
    finished_at = "N/A"
    message = "N/A"
    reason = "N/A"


    # Extract restart count &  "lastState" if available
    for container_status in pod["status"]["containerStatuses"]:
        restart_count = container_status["restartCount"]
        last_state = container_status.get("lastState", {})
        terminated = last_state.get("terminated", {})

        exit_code = terminated.get("exitCode", "N/A")
        started_at = terminated.get("startedAt", "N/A")
        finished_at = terminated.get("finishedAt", "N/A")
        message = terminated.get("message", "N/A").replace("\n", " ")
        reason = terminated.get("reason", "N/A")

    pod_timestamp = pod["metadata"]["creationTimestamp"]


    # Loop through containers defined in the "spec" block
    for container in pod["spec"]["containers"]:
        resource_limits = container["resources"]["limits"]
        memory_limits = resource_limits.get("memory", "N/A")
        cpu_limits = resource_limits.get("cpu", "N/A")

        resource_requests = container["resources"]["requests"]
        memory_requests = resource_requests.get("memory", "N/A")
        cpu_requests = resource_requests.get("cpu", "N/A")

#         # Extract resource name (APP_NAME)
#         for env_var in container.get("env", []):
#             if env_var["name"] == "APP_NAME":
#                 resource_name = env_var["value"]
#         break

#     if resource_name == "N/A":
#         continue

    # if restart_count == 0:
    #     continue

    print(f"{pod_name},{restart_count},{memory_limits},{cpu_limits},{memory_requests},{cpu_requests},{pod_timestamp},{started_at},{finished_at},{exit_code},{message},{reason}\n")

    # Write to CSV file
    with open("pods_info.csv", "a") as csv_file:
        csv_file.write(f"{pod_name},{restart_count},{memory_limits},{cpu_limits},{memory_requests},{cpu_requests},{pod_timestamp},{started_at},{finished_at},{exit_code},{message},{reason}\n")

print("CSV file 'pods_info.csv' created.")