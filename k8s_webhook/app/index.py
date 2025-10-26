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

        # Only mutate if platform_managed=true
        if str(labels.get('platform_managed')).lower() == 'true':
            if labels.get('owner') != 'chaitanya':
                # Check if labels exist
                if not labels:
                    patch.append({
                        "op": "add",
                        "path": "/metadata/labels",
                        "value": {"owner": "chaitanya"}
                    })
                else:
                    patch.append({
                        "op": "add",
                        "path": "/metadata/labels/owner",
                        "value": "chaitanya"
                    })

                logging.info(f"Mutating pod: adding owner=chaitanya")

        response_obj = {
            "uid": uid,
            "allowed": True
        }

        if patch:
            response_obj.update({
                "patchType": "JSONPatch",
                "patch": base64.b64encode(json.dumps(patch).encode()).decode()
            })

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
                "uid": request_info.get('request', {}).get('uid', ''),
                "allowed": True,  # Allow on error to avoid blocking
                "status": {
                    "code": 200,
                    "message": f"Mutation skipped due to error: {str(e)}"
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

        # Only enforce validation if platform_managed=true
        if str(labels.get('platform_managed')).lower() == 'true':
            allowed = 'maintainer' in labels
            status = {
                "code": 200 if allowed else 403,
                "message": "Validation passed." if allowed else "Missing required 'maintainer' label."
            }
            logging.info(f"Validating pod: {'passed' if allowed else 'failed'}")
        else:
            allowed = True
            status = {
                "code": 200,
                "message": "Not managed by platform. Skipping validation."
            }

        response_obj = {
            "uid": uid,
            "allowed": allowed,
            "status": status
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
                "uid": request_info.get('request', {}).get('uid', ''),
                "allowed": False,
                "status": {
                    "code": 500,
                    "message": f"Validation error: {str(e)}"
                }
            }
        })


# ------------------ HEALTH CHECK ------------------ #
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200


# ------------------ ENTRY POINT ------------------ #
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, ssl_context=(f"{pwd}/CA/tls.crt", f"{pwd}/CA/tls.key"))
