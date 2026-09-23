import logging
import aiomysql

from fastapi import APIRouter, Request

from routers.defaults import (
    default_response,
    output_response,
    apply_patchset_to_response,
)


router = APIRouter(
    tags=["update resource requests and limits to deployments"],
    prefix="/requests-limits",
)


DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "YOUR_USER",
    "password": "YOUR_PASSWORD",
    "db": "YOUR_DATABASE",
    "autocommit": True,
}


# ---------------------------------------------------------
# CPU conversion
# ---------------------------------------------------------

def cpu_to_milli_cpu(cpu):
    """
    Kubernetes CPU -> milli CPU

    Examples:
        100m  -> 100
        500m  -> 500
        1     -> 1000
        0.5   -> 500
    """

    if cpu is None:
        return None

    cpu = str(cpu).strip()

    if cpu.endswith("m"):
        return int(cpu[:-1])

    return int(float(cpu) * 1000)


# ---------------------------------------------------------
# Memory conversion
# ---------------------------------------------------------

def memory_to_mb(memory):
    """
    Kubernetes memory -> MB/MiB

    Examples:
        256Mi -> 256
        512Mi -> 512
        1Gi   -> 1024
        128Ki -> 0
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


# ---------------------------------------------------------
# Get desired resource values from MySQL
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# Mutation webhook
# ---------------------------------------------------------

@router.post("/mutate")
async def requests_limits_mutation(request: Request):

    body = await request.json()

    logging.debug("Request body")
    logging.debug(f"{body}")

    # -----------------------------------------------------
    # Admission response
    # -----------------------------------------------------

    uid = body["request"]["uid"]

    json_res = default_response(uid)

    patchset = []
    error_msgs = []

    # -----------------------------------------------------
    # Kubernetes object
    # -----------------------------------------------------

    obj = body["request"].get("object", {})

    kind = obj.get("kind", "")

    metadata = obj.get("metadata", {})

    deployment_name = metadata.get("name", "")

    namespace = metadata.get("namespace", "default")

    # -----------------------------------------------------
    # Only process Deployments
    # -----------------------------------------------------

    if kind != "Deployment":

        logging.debug(
            f"Skipping kind={kind}, "
            f"deployment={deployment_name}"
        )

        return output_response(json_res)

    # -----------------------------------------------------
    # Deployment containers
    #
    # spec:
    #   template:
    #     spec:
    #       containers:
    # -----------------------------------------------------

    containers = (
        obj
        .get("spec", {})
        .get("template", {})
        .get("spec", {})
        .get("containers", [])
    )

    # -----------------------------------------------------
    # Process every container
    # -----------------------------------------------------

    for index, container in enumerate(containers):

        container_name = container.get("name", "")

        if not container_name:
            continue

        # -------------------------------------------------
        # Get desired resource values from DB
        # -------------------------------------------------

        desired = await get_resource_values(
            namespace=namespace,
            deployment=deployment_name,
            container=container_name,
        )

        if not desired:

            logging.debug(
                f"No c_logs entry found for "
                f"cluster=master, "
                f"namespace={namespace}, "
                f"deployment={deployment_name}, "
                f"container={container_name}"
            )

            continue

        desired_milli_cpu = desired["milli_cpu"]

        desired_mb_memory = desired["mb_memory"]

        # -------------------------------------------------
        # Convert DB values to Kubernetes resource values
        # -------------------------------------------------

        desired_cpu = f"{desired_milli_cpu}m"

        desired_memory = f"{desired_mb_memory}Mi"

        # -------------------------------------------------
        # Current container resources
        # -------------------------------------------------

        resources = container.get("resources") or {}

        current_requests = resources.get("requests") or {}

        current_limits = resources.get("limits") or {}

        # =================================================
        # Convert incoming CPU
        # =================================================

        current_request_cpu = current_requests.get("cpu")

        current_limit_cpu = current_limits.get("cpu")

        current_request_milli_cpu = cpu_to_milli_cpu(
            current_request_cpu
        )

        current_limit_milli_cpu = cpu_to_milli_cpu(
            current_limit_cpu
        )

        # =================================================
        # Convert incoming memory
        # =================================================

        current_request_memory = current_requests.get("memory")

        current_limit_memory = current_limits.get("memory")

        current_request_mb_memory = memory_to_mb(
            current_request_memory
        )

        current_limit_mb_memory = memory_to_mb(
            current_limit_memory
        )

        logging.debug(
            f"Container={container_name}, "
            f"current request CPU={current_request_milli_cpu}m, "
            f"current request memory={current_request_mb_memory}Mi, "
            f"current limit CPU={current_limit_milli_cpu}m, "
            f"current limit memory={current_limit_mb_memory}Mi, "
            f"desired CPU={desired_milli_cpu}m, "
            f"desired memory={desired_mb_memory}Mi"
        )

        # =================================================
        # CPU REQUEST
        # =================================================

        if current_request_milli_cpu != desired_milli_cpu:

            patchset.append({
                "op": "add",
                "path": (
                    f"/spec/template/spec/containers/"
                    f"{index}/resources/requests/cpu"
                ),
                "value": desired_cpu,
            })

            msg = (
                f"Deployment={deployment_name}, "
                f"container={container_name}: "
                f"requests.cpu changed from "
                f"{current_request_milli_cpu}m to "
                f"{desired_milli_cpu}m"
            )

            logging.warning(msg)

            error_msgs.append(msg)

        # =================================================
        # MEMORY REQUEST
        # =================================================

        if current_request_mb_memory != desired_mb_memory:

            patchset.append({
                "op": "add",
                "path": (
                    f"/spec/template/spec/containers/"
                    f"{index}/resources/requests/memory"
                ),
                "value": desired_memory,
            })

            msg = (
                f"Deployment={deployment_name}, "
                f"container={container_name}: "
                f"requests.memory changed from "
                f"{current_request_mb_memory}Mi to "
                f"{desired_mb_memory}Mi"
            )

            logging.warning(msg)

            error_msgs.append(msg)

        # =================================================
        # CPU LIMIT
        # =================================================

        if current_limit_milli_cpu != desired_milli_cpu:

            patchset.append({
                "op": "add",
                "path": (
                    f"/spec/template/spec/containers/"
                    f"{index}/resources/limits/cpu"
                ),
                "value": desired_cpu,
            })

            msg = (
                f"Deployment={deployment_name}, "
                f"container={container_name}: "
                f"limits.cpu changed from "
                f"{current_limit_milli_cpu}m to "
                f"{desired_milli_cpu}m"
            )

            logging.warning(msg)

            error_msgs.append(msg)

        # =================================================
        # MEMORY LIMIT
        # =================================================

        if current_limit_mb_memory != desired_mb_memory:

            patchset.append({
                "op": "add",
                "path": (
                    f"/spec/template/spec/containers/"
                    f"{index}/resources/limits/memory"
                ),
                "value": desired_memory,
            })

            msg = (
                f"Deployment={deployment_name}, "
                f"container={container_name}: "
                f"limits.memory changed from "
                f"{current_limit_mb_memory}Mi to "
                f"{desired_mb_memory}Mi"
            )

            logging.warning(msg)

            error_msgs.append(msg)

    # -----------------------------------------------------
    # Apply patches
    # -----------------------------------------------------

    if len(patchset) > 0:

        json_res = apply_patchset_to_response(
            json_res,
            patchset,
            warnings=error_msgs,
        )

        json_res["response"]["allowed"] = True

        logging.info(
            f"Mutated deployment={deployment_name}, "
            f"namespace={namespace}, "
            f"patches={len(patchset)}"
        )

    else:

        logging.debug(
            f"Deployment '{deployment_name}' "
            f"namespace '{namespace}' resources "
            f"are already at desired values, "
            f"skipping mutation"
        )

    return output_response(json_res)