from kubernetes import client, config
import csv

# Load kubeconfig (works with ~/.kube/config or inside a pod with ServiceAccount)
config.load_kube_config()

v1 = client.CoreV1Api()

# Output CSV file
output_file = "resourcequotas.csv"

# CSV headers
headers = [
    "namespace", "quota_name",
    "cpu_requests_hard", "cpu_requests_used",
    "memory_requests_hard", "memory_requests_used",
    "cpu_limits_hard", "cpu_limits_used",
    "memory_limits_hard", "memory_limits_used"
]

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
            used = rq.status.used or {}

            writer.writerow([
                ns, quota_name,
                hard.get("requests.cpu", "N/A"), used.get("requests.cpu", "0"),
                hard.get("requests.memory", "N/A"), used.get("requests.memory", "0"),
                hard.get("limits.cpu", "N/A"), used.get("limits.cpu", "0"),
                hard.get("limits.memory", "N/A"), used.get("limits.memory", "0")
            ])

print(f"ResourceQuota details (hard & used) saved to {output_file}")
