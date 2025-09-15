from kubernetes import client, config
import csv

# Load kubeconfig (works with ~/.kube/config or inside a pod with ServiceAccount)
config.load_kube_config()

v1 = client.CoreV1Api()

# Output CSV file
output_file = "resourcequotas.csv"

# CSV headers
headers = ["namespace", "quota_name", "cpu_requests", "memory_requests", "cpu_limits", "memory_limits"]

with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    # List all namespaces
    namespaces = ["dev"]

    for ns in namespaces:

        # Get resource quotas in the namespace
        rq_list = v1.list_namespaced_resource_quota(ns).items

        for rq in rq_list:
            quota_name = rq.metadata.name
            hard = rq.status.hard or {}

            cpu_requests = hard.get("requests.cpu", "N/A")
            mem_requests = hard.get("requests.memory", "N/A")
            cpu_limits = hard.get("limits.cpu", "N/A")
            mem_limits = hard.get("limits.memory", "N/A")

            writer.writerow([ns, quota_name, cpu_requests, mem_requests, cpu_limits, mem_limits])

print(f"ResourceQuota details saved to {output_file}")
