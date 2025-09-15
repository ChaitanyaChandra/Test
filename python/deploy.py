from kubernetes import client, config
import csv

# Load kubeconfig (works with ~/.kube/config or inside a pod with ServiceAccount)
config.load_kube_config()

core_v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

# CSV output file
output_file = "deployments_resources.csv"

with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Namespace", "Deployment", "Replicas", "Container",
        "CPU Requests", "Memory Requests", "CPU Limits", "Memory Limits"
    ])

    # Get all namespaces first
    namespaces = core_v1.list_namespace().items
    dev_namespaces = [ns.metadata.name for ns in namespaces if "dev" in ns.metadata.name]

    # Iterate only through filtered namespaces
    for ns in dev_namespaces:
        deployments = apps_v1.list_namespaced_deployment(ns)

        for dep in deployments.items:
            namespace = dep.metadata.namespace
            name = dep.metadata.name
            replicas = dep.spec.replicas if dep.spec.replicas else 0

            # Loop through containers in each deployment
            for container in dep.spec.template.spec.containers:
                resources = container.resources

                cpu_req = resources.requests.get("cpu", "0") if resources.requests else "0"
                mem_req = resources.requests.get("memory", "0") if resources.requests else "0"
                cpu_lim = resources.limits.get("cpu", "0") if resources.limits else "0"
                mem_lim = resources.limits.get("memory", "0") if resources.limits else "0"

                writer.writerow([
                    namespace, name, replicas, container.name,
                    cpu_req, mem_req, cpu_lim, mem_lim
                ])

print(f"✅ Deployment resource details (only for 'dev' namespaces) saved to {output_file}")
