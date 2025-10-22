#!/usr/bin/env python3
import os
from datetime import datetime, timedelta, timezone
from kubernetes import client, config

CLUSTERS = ["main", "master"]
NAMESPACE = "default"
THRESHOLD_HOURS = 12
now = datetime.now(timezone.utc)

def cleanup_cluster(cluster_name):
    print(f"Cluster: {cluster_name}")
    kubeconfig = os.path.expanduser(f"~/.kube/{cluster_name}/config")

    try:
        config.load_kube_config(config_file=kubeconfig)
    except Exception as e:
        print(f"Can't load kubeconfig: {e}")
        return

    apps = client.AppsV1Api()
    core = client.CoreV1Api()

    # Scale old deployments
    for d in apps.list_namespaced_deployment(NAMESPACE).items:
        age = now - d.metadata.creation_timestamp  # ✅ keep timezone-aware (no .replace)
        if age > timedelta(hours=THRESHOLD_HOURS):
            print(f"cluster_name: {cluster_name}, namespace: {NAMESPACE}, deployment: {d.metadata.name} → {age} old → scale to 0")
            apps.patch_namespaced_deployment_scale(
                d.metadata.name, NAMESPACE, {"spec": {"replicas": 0}}
            )
        else:
            print(f"cluster_name: {cluster_name}, namespace: {NAMESPACE}, deployment: {d.metadata.name} is fine ({age})")

    # Delete all pods (and print names)
    pods = core.list_namespaced_pod(NAMESPACE).items
    if not pods:
        print(f"cluster_name: {cluster_name}, namespace: {NAMESPACE}, No pods found.")
        return

    print(f"cluster_name: {cluster_name}, namespace: {NAMESPACE}, Deleting {len(pods)} pods:")
    for p in pods:
        print(f"  - {p.metadata.name}")
        core.delete_namespaced_pod(p.metadata.name, NAMESPACE)
    print(f"cluster_name: {cluster_name}, namespace: {NAMESPACE}, Pods deleted.")


def main():
    for c in CLUSTERS:
        cleanup_cluster(c)


if __name__ == "__main__":
    main()
