import logging
import json
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

def default_response(uid: str):
    return {
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": uid,
            "allowed": True,
            "warnings": [],
        }
    }

def output_response(response: dict):
    logging.debug("json response")
    sanitized_response = str(response).replace('\r\n', '').replace('\n', '')
    logging.debug(sanitized_response)
    if len(response['response']['warnings']) > 0:
        response['response']['status'] = {"message": ','.join(response['response']['warnings'])}
    return JSONResponse(content=jsonable_encoder(response)) 