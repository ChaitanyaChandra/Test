import logging
import aiomysql
import os
from fastapi import APIRouter, Request
import json

from app.routers.defaults import (
    default_response,
    output_response,
    apply_patchset_to_response,
)


router = APIRouter(
    tags=["update resource requests and limits to deployments"],
    prefix="/requests-limits"
)


DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": 3306,
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "db": "cc",
    "autocommit": True,
}


def cpu_to_milli_cpu(cpu):
    """
    Convert Kubernetes CPU value to milli CPU.

    100m -> 100
    500m -> 500
    1    -> 1000
    0.5  -> 500
    """

    if cpu is None:
        return None

    cpu = str(cpu).strip()

    if cpu.endswith("m"):
        return int(cpu[:-1])

    return int(float(cpu) * 1000)


def memory_to_mb(memory):
    """
    Convert Kubernetes memory value to MB/MiB.

    256Mi -> 256
    512Mi -> 512
    1Gi   -> 1024
    1024Ki -> 1
    """

    if memory is None:
        return None

    memory = str(memory).strip()

    if memory.endswith("Ki"):
        return int(float(memory[:-2]) / 1024)

    if memory.endswith("Mi"):
        return int(float(memory[:-2]))

    if memory.endswith("Gi"):
        return int(float(memory[:-2]) * 1024)

    if memory.endswith("Ti"):
        return int(float(memory[:-2]) * 1024 * 1024)

    # Plain Kubernetes memory value is bytes
    return int(int(memory) / (1024 * 1024))


async def get_resource_values(
    namespace: str,
    deployment: str,
    container: str,
):
    query = f"""
        SELECT
            milli_cpu,
            mb_memory
        FROM c_logs
        WHERE cluster_name = 'master'
          AND namespace = '{namespace}'
          AND deployment = '{deployment}'
          AND container = '{container}'
        ORDER BY log_date DESC
        LIMIT 1
    """

    connection = await aiomysql.connect(**DB_CONFIG)
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute(query)
            return await cursor.fetchone()
    finally:
        connection.close()


@router.post("/mutate")
async def requests_limits_mutation(request: Request):

    body = await request.json()
    logging.debug("Request body ========= ******** ==========")
    logging.debug(json.dumps(body, separators=(",", ":")))
    logging.debug("Request body ========= ******** ==========")
    
    # Admission response
    uid = body["request"]["uid"]
    json_res = default_response(uid)
    patchset = []
    error_msgs = []

    obj = body["request"].get("object", {})
    kind = obj.get("kind", "")
    metadata = obj.get("metadata", {})
    deployment_name = metadata.get("name", "")
    namespace = metadata.get("namespace", "default")

    # Only process Deployments
    if kind != "Deployment":
        logging.debug(f"Skipping kind={kind}, deployment={deployment_name}")
        return output_response(json_res)

    containers = (
        obj
        .get("spec", {})
        .get("template", {})
        .get("spec", {})
        .get("containers", [])
    )

    for index, container in enumerate(containers):

        container_name = container.get("name", "")
        if not container_name:
            continue

        # Get values from MySQL
        cc_data = await get_resource_values(
            namespace=namespace,
            deployment=deployment_name,
            container=container_name,
        )

        if not cc_data:
            logging.debug(f"No c_logs entry found for cluster=master, namespace={namespace}, deployment={deployment_name}, container={container_name}")
            continue

        cc_cpu = cc_data["milli_cpu"]
        cc_memory = cc_data["mb_memory"]

        # Convert DB values to Kubernetes format
        cc_milli_cpu = f"{cc_cpu}m"
        cc_mb_memory = f"{cc_memory}Mi"

        # get values from request
        resources = container.get("resources")
        if not resources:
            logging.debug(f"Skipping container={container_name}: resources is not defined")
            continue

        requests = resources.get("requests")
        if not requests:
            logging.debug(f"Skipping container={container_name}: requests is not defined")
            continue

        current_request_cpu = requests.get("cpu")
        current_request_memory = requests.get("memory")

        # Convert incoming CPU values
        current_request_milli_cpu = (
            cpu_to_milli_cpu(current_request_cpu)
            if current_request_cpu is not None
            else None
        )

        # Convert incoming memory values
        current_request_mb_memory = (
            memory_to_mb(current_request_memory)
            if current_request_memory is not None
            else None
        )

        logging.debug(f"deployment={deployment_name},  Container={container_name}, request_cpu={current_request_milli_cpu}m, request_memory={current_request_mb_memory}Mi, cc_milli_cpu={cc_cpu}m, cc_mb_memory={cc_memory}Mi")

        # CPU REQUEST
        if (
            current_request_milli_cpu is not None
            and current_request_milli_cpu != cc_cpu
        ):

            patchset.append({
                "op": "replace",
                "path": (
                    f"/spec/template/spec/containers/"
                    f"{index}/resources/requests/cpu"
                ),
                "value": cc_milli_cpu
            })

            msg = f"container: {container_name}, spec.template.spec.containers[{index}].resources.requests.cpu changed from {current_request_milli_cpu}m to {cc_cpu}m"
            logging.warning(msg)
            error_msgs.append(msg)

        # MEMORY REQUEST
        if (
            current_request_mb_memory is not None
            and current_request_mb_memory != cc_memory
        ):

            patchset.append({
                "op": "replace",
                "path": (
                    f"/spec/template/spec/containers/"
                    f"{index}/resources/requests/memory"
                ),
                "value": cc_mb_memory
            })

            msg = f"container: {container_name}, spec.template.spec.containers[{index}].resources.requests.memory changed from {current_request_mb_memory}Mi to {cc_memory}Mi"
            logging.warning(msg)

            error_msgs.append(msg)

    # Apply patches
    if len(patchset) > 0:
        json_res = apply_patchset_to_response(
            json_res,
            patchset,
            warnings=error_msgs
        )

        json_res["response"]["allowed"] = True
        logging.info(f"Mutated deployment={deployment_name}, namespace={namespace}, patches={len(patchset)}")

    else:
        logging.debug(f"Skipping mutation for Deployment '{deployment_name}' namespace '{namespace}'")

    return output_response(json_res)