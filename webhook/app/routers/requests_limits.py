import logging
import json
import string
import re
from fastapi import APIRouter, Request
from routers.defaults import default_response, output_response, apply_patchset_to_response


router = APIRouter(
    tags=['update resource requests and limits to deployments'],
    prefix="/requests-limits"
)

data = [{
  "metadata": {
    "name": "demo-deployment-1",
    "namespace": "chaitanya-chandra-testing"
  },
  "spec": {
      "spec": {
        "containers": [
          {
            "name": "demo-container",
            "resources": {
              "limits": {
                "cpu": "500m",
                "memory": "256Mi"
              },
              "requests": {
                "cpu": "0.01",
                "memory": "0.1Gi"
              }
            }
          }
        ]
      }
    }
},
{
  "metadata": {
    "name": "demo-deployment-2",
    "namespace": "chaitanya-chandra-testing"
  },
  "spec": {
      "spec": {
        "containers": [
          {
            "name": "demo-container",
            "resources": {
              "limits": {
                "cpu": "0.6",
                "memory": "0.25Gi"
              },
              "requests": {
                "cpu": "0.06",
                "memory": "0.13Gi"
              }
            }
          },
          {
            "name": "demo-container-two",
            "resources": {
              "limits": {
                "cpu": "0.6",
                "memory": "0.25Gi"
              },
              "requests": {
                "cpu": "0.06",
                "memory": "0.13Gi"
              }
            }
          }
        ]
      }
    }
}]


@router.post("/mutate")
async def requests_limits_mutation(request: Request):
    body = await request.json()
    sanitized_body = str(body).replace('\r\n', '').replace('\n', '')
    logging.debug("Request body")
    logging.debug(sanitized_body)

    json_res = default_response(body['request']['uid'])

    # patches to apply
    patchset=[]
    kind = body["request"]["object"].get(   "kind", '')
    sanitized_kind = kind.replace('\r\n', '').replace('\n', '')
    deployment_name = body["request"]["object"]["metadata"].get("name", '')
    sanitized_deployment_name = deployment_name.replace('\r\n', '').replace('\n', '')
    containers = body["request"]["object"].get("spec", {}).get("containers", [])

    deployments= [item["metadata"]["name"] for item in data]

    if sanitized_deployment_name in deployments: 
        deployment = next(item for item in data if item["metadata"]["name"] == sanitized_deployment_name)
        deployment_containers = deployment.get("spec", {}).get("spec", {}).get("containers", [])
        deployment_container_names = [c.get("name") for c in deployment_containers]
        error_msgs = []
        
        for index, container in enumerate(containers):
            container_name = container.get("name", "")
            sanitized_container_name = container_name.replace('\r\n', '').replace('\n', '')
            
            if container_name in deployment_container_names:
                desired_container = next(c for c in deployment_containers if c.get("name") == container_name)
                desired_resources = desired_container.get("resources", {})
                
                # Check and patch limits
                desired_limits = desired_resources.get("limits", {})
                current_limits = container.get("resources", {}).get("limits", {})
                for key, val in desired_limits.items():
                    if current_limits.get(key) != val:
                        patchset.append({
                            "op": "replace",
                            "path": f"/spec/containers/{index}/resources/limits/{key}",
                            "value": val
                        })
                        msg = f"spec.containers[{index}].resources.limits.{key} was set to CC desired value"
                        logging.warning(msg)
                        error_msgs.append(msg)
                
                # Check and patch requests
                desired_requests = desired_resources.get("requests", {})
                current_requests = container.get("resources", {}).get("requests", {})
                for key, val in desired_requests.items():
                    if current_requests.get(key) != val:
                        patchset.append({
                            "op": "replace",
                            "path": f"/spec/containers/{index}/resources/requests/{key}",
                            "value": val
                        })
                        msg = f"spec.containers[{index}].resources.requests.{key} was set to CC desired value"
                        logging.warning(msg)
                        error_msgs.append(msg)
        
        if len(patchset) > 0:
            json_res = apply_patchset_to_response(json_res, patchset, warnings=error_msgs)
            json_res['response']['allowed'] = True
        else:
            container_names = [c.get("name", "") for c in containers]
            logging.debug(f"Deployment '{sanitized_deployment_name}' containers {container_names} resources were in CC desired value, skipping mutation")
    else:
        logging.debug(f"Deployment '{sanitized_deployment_name}' is not in CC targeted deployments, skipping mutation")

    return output_response(json_res)

