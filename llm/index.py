def list_configmaps(self, namespace: str, cluster: str) -> List[str]:
    """List configmap names in a Kubernetes namespace"""
    self._require_ns(namespace)
    config_maps = []
    core_v1_api: client.CoreV1Api = self.config_map.get_config_details(cluster).k8s_core_v1_api
    for cm in core_v1_api.list_namespaced_config_map(namespace).items:
        config_maps.append({
            "name": cm.metadata.name,
            "data": cm.data,
            "created_at": cm.metadata.creation_timestamp,
        })
    logger.info(f"Fetched configmaps list {[cm['name'] for cm in config_maps]} in namespace {namespace}")
    return config_maps


def list_secrets(self, namespace: str, cluster: str) -> List[dict]:
    """List all secrets in a Kubernetes namespace"""
    self._require_ns(namespace)
    secrets = []
    core_v1_api: client.CoreV1Api = self.config_map.get_config_details(cluster).k8s_core_v1_api
    for secret in core_v1_api.list_namespaced_secret(namespace).items:
        secrets.append({
            "name": secret.metadata.name,
            "type": secret.type,
            "data": secret.data,
            "created_at": secret.metadata.creation_timestamp,
        })
    logger.info(f"Fetched secrets list {[s['name'] for s in secrets]} in namespace {namespace}")
    return secrets