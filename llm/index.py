import os
from typing import List, Any
from kubernetes import client, config, dynamic
from kubernetes.client import api_client
from loguru import logger
from agno.tools import Toolkit

# --------------------------------------------------------------------------
# Kubernetes Config
# --------------------------------------------------------------------------
cluster_path = os.getenv("CLUSTER_CONFIG_PATH", "~/.kube/config")
config.load_kube_config(cluster_path)

SUPPORTED_KINDS = [
    "pod",
    "service",
    "configmap",
    "secret",
    "persistentvolumeclaim",
    "deployment",
    "statefulset",
    "daemonset",
    "replicaset",
    "ingress",
    "networkpolicy",
]

class K8sResourceReader(Toolkit):
    """
    Kubernetes tools scoped STRICTLY to a single namespace.
    Tools are conditionally exposed to the agent.
    """

    def __init__(self, list_all: bool = False, **kwargs):
        self.v1 = client.CoreV1Api()
        self.apps_v1 = client.AppsV1Api()
        self.net_v1 = client.NetworkingV1Api()
        self.dyn = dynamic.DynamicClient(api_client.ApiClient())

        tools: List[Any] = []

        # --------------------------------------------------------------
        # Conditionally expose tools to the agent
        # --------------------------------------------------------------
        if list_all:
            tools.extend([
                self.list_pods,
                self.list_services,
                self.list_configmaps,
                self.list_secrets,
                self.list_deployments,
                self.list_statefulsets,
                self.list_ingresses,
                self.get_resource_json,
            ])

        super().__init__(
            name="k8s_namespaced_tools",
            tools=tools,
            **kwargs
        )

    # ------------------------------------------------------------------
    # CORE
    # ------------------------------------------------------------------
    def list_pods(self, namespace: str) -> List[str]:
        """List pod names in a Kubernetes namespace"""
        self._require_ns(namespace)
        pods = [p.metadata.name for p in self.v1.list_namespaced_pod(namespace).items]
        logger.info(f"Fetched pods list {pods} in namespace {namespace}")
        return pods

    def list_services(self, namespace: str) -> List[str]:
        """List service names in a Kubernetes namespace"""
        self._require_ns(namespace)
        services = [s.metadata.name for s in self.v1.list_namespaced_service(namespace).items]
        logger.info(f"Fetched services list {services} in namespace {namespace}")
        return services

    def list_configmaps(self, namespace: str) -> List[str]:
        """List configmap names in a Kubernetes namespace"""
        self._require_ns(namespace)
        cms = [c.metadata.name for c in self.v1.list_namespaced_config_map(namespace).items]
        logger.info(f"Fetched configmaps list {cms} in namespace {namespace}")
        return cms

    def list_secrets(self, namespace: str) -> List[str]:
        """List secret names in a Kubernetes namespace"""
        self._require_ns(namespace)
        secrets = [s.metadata.name for s in self.v1.list_namespaced_secret(namespace).items]
        logger.info(f"Fetched secrets list {secrets} in namespace {namespace}")
        return secrets

    # ------------------------------------------------------------------
    # WORKLOADS
    # ------------------------------------------------------------------
    def list_deployments(self, namespace: str) -> List[str]:
        """List deployment names in a Kubernetes namespace"""
        self._require_ns(namespace)
        deps = [d.metadata.name for d in self.apps_v1.list_namespaced_deployment(namespace).items]
        logger.info(f"Fetched deployments list {deps} in namespace {namespace}")
        return deps

    def list_statefulsets(self, namespace: str) -> List[str]:
        """List statefulset names in a Kubernetes namespace"""
        self._require_ns(namespace)
        sts = [s.metadata.name for s in self.apps_v1.list_namespaced_stateful_set(namespace).items]
        logger.info(f"Fetched statefulsets list {sts} in namespace {namespace}")
        return sts

    # ------------------------------------------------------------------
    # NETWORKING
    # ------------------------------------------------------------------
    def list_ingresses(self, namespace: str) -> List[str]:
        """List ingress names in a Kubernetes namespace"""
        self._require_ns(namespace)
        ings = [i.metadata.name for i in self.net_v1.list_namespaced_ingress(namespace).items]
        logger.info(f"Fetched ingresses list {ings} in namespace {namespace}")
        return ings

    # ------------------------------------------------------------------
    # JSON FETCH
    # ------------------------------------------------------------------
    def get_resource_json(self, kind: str, name: str, namespace: str) -> dict:
        f"""
        Use Kubernetes API to fetch a namespaced resource by kind, name, and namespace.
        SUPPORTED_KINDS: {SUPPORTED_KINDS}
        Retrieve only the exact matching object.
        Return the full resource JSON for troubleshooting.
        
        HARD RULES (MANDATORY):
            - You MUST validate the requested kind
            - If the kind is NOT in SUPPORTED_KINDS, you MUST NOT proceed
            - Unsupported kinds are a HARD ERROR
        """
        self._require_ns(namespace)

        if kind.lower() not in SUPPORTED_KINDS:
            raise ValueError(
                f"Unsupported kind '{kind}'. Supported kinds: {list(SUPPORTED_KINDS)}"
            )

        try:
            res = self.dyn.resources.get(
                kind=kind
            )

            obj = res.get(name=name, namespace=namespace)
            logger.info(f"Fetched JSON for {kind}/{name} in namespace {namespace}")
            return obj.to_dict()
        except Exception as e:
            logger.error(f"Error: {e}")        

    # ------------------------------------------------------------------
    # INTERNAL
    # ------------------------------------------------------------------
    def _require_ns(self, namespace: str):
        if not namespace:
            raise ValueError("❌ namespace is required")
