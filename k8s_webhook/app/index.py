from flask import Flask, request, jsonify
import base64
import json
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
pwd = os.getcwd()

# ------------------ MUTATING WEBHOOK ------------------ #
@app.route('/mutate', methods=['POST'])
def mutate():
    try:
        request_info = request.get_json()
        uid = request_info['request']['uid']
        pod = request_info['request']['object']
        labels = pod.get('metadata', {}).get('labels', {})

        patch = []
        if labels.get('owner') != 'chaitanya':
            if 'labels' not in pod.get('metadata', {}):
                patch.append({
                    "op": "add",
                    "path": "/metadata/labels",
                    "value": {"owner": "chaitanya"}
                })
            else:
                patch.append({
                    "op": "add" if 'owner' not in labels else "replace",
                    "path": "/metadata/labels/owner",
                    "value": "chaitanya"
                })

        response_obj = {
            "uid": uid,
            "allowed": True
        }

        if patch:
            response_obj.update({
                "patchType": "JSONPatch",
                "patch": base64.b64encode(json.dumps(patch).encode()).decode()
            })

        # AdmissionReview-compliant response
        response = {
            "apiVersion": "admission.k8s.io/v1",
            "kind": "AdmissionReview",
            "response": response_obj
        }

        return jsonify(response)

    except Exception as e:
        logging.error(f"Mutation error: {e}")
        return jsonify({
            "apiVersion": "admission.k8s.io/v1",
            "kind": "AdmissionReview",
            "response": {
                "uid": request_info.get("request", {}).get("uid", ""),
                "allowed": False,
                "status": {
                    "code": 500,
                    "message": f"Mutation error: {e}"
                }
            }
        })


# ------------------ VALIDATING WEBHOOK ------------------ #
@app.route('/validate', methods=['POST'])
def validate():
    try:
        request_info = request.get_json()
        uid = request_info['request']['uid']
        pod = request_info['request']['object']
        labels = pod.get('metadata', {}).get('labels', {})

        allowed = 'maintainer' in labels
        response_obj = {
            "uid": uid,
            "allowed": allowed,
            "status": {
                "code": 403 if not allowed else 200,
                "message": "Missing required 'maintainer' label." if not allowed else "Validation passed."
            }
        }

        response = {
            "apiVersion": "admission.k8s.io/v1",
            "kind": "AdmissionReview",
            "response": response_obj
        }

        return jsonify(response)

    except Exception as e:
        logging.error(f"Validation error: {e}")
        return jsonify({
            "apiVersion": "admission.k8s.io/v1",
            "kind": "AdmissionReview",
            "response": {
                "uid": request_info.get("request", {}).get("uid", ""),
                "allowed": False,
                "status": {
                    "code": 500,
                    "message": f"Validation error: {e}"
                }
            }
        })


# ------------------ ENTRY POINT ------------------ #
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,
            ssl_context=(f'{pwd}/../CA/tls.crt', f'{pwd}/../CA/tls.key'))
