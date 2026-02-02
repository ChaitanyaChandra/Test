def list_ingresses(self, namespace: str, cluster: str) -> List[dict]:
    """List ingress names in a Kubernetes namespace"""
    self._require_ns(namespace)
    net_v1_api: client.NetworkingV1Api = self.config_map.get_config_details(cluster).k8s_networking_v1_api
    ingress = []
    for ing in net_v1_api.list_namespaced_ingress(namespace).items:
        ingress.append({
            "name": ing.metadata.name,
            "ingress_class_name": ing.spec.ingress_class_name,
            "rules": ing.spec.rules,
            "created_at": ing.metadata.creation_timestamp,
        })
    logger.info(f"Fetched ingresses list {[ing['name'] for ing in ingress]} in namespace {namespace}")
    return ingress