from fastapi import APIRouter, Request
import logging
import re
from routers.defaults import default_response, output_response

router = APIRouter(
    tags=['Block re-write params in Ingress annotation'],
    prefix="/validate-rewrite"
)

@router.post("/validate")
async def validate_rewrite_webhook(request: Request):
    body = await request.json()
    sanitized_body = str(body).replace('\r\n', '').replace('\n', '')
    logging.debug("Request body")
    logging.debug(sanitized_body)

    json_res = default_response(body['request']['uid'])

    # check the ingress class name
    if body['request']['object']['spec']['ingressClassName'] != "nginx":
        return output_response(json_res)

    # fail the validation webhook if the rewrite annotation contains any numeric capture group placeholder like $1, $11, $1000
    if 'annotations' not in body['request']['object']['metadata']:
        return output_response(json_res)

    rewrite_annotation = body['request']['object']['metadata']['annotations'].get('nginx.ingress.kubernetes.io/rewrite-target', '')
    if rewrite_annotation and re.search(r'\$\d+', rewrite_annotation):
        json_res['response']['allowed'] = False
        json_res['response']['warnings'].append("Rewrite annotation must not contain numeric capture groups like $1, $2, etc.")

    return json_res

