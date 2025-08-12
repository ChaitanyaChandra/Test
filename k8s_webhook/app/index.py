from flask import Flask, request, jsonify
import base64
import json

app = Flask(__name__)

# ------------------ MUTATING WEBHOOK ------------------ #
@app.route('/mutate', methods=['POST'])
def mutate():
    request_info = request.get_json()
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

    response = {
        "response": {
            "uid": request_info['request']['uid'],
            "allowed": True,
            "patchType": "JSONPatch" if patch else None,
            "patch": base64.b64encode(json.dumps(patch).encode()).decode() if patch else None
        }
    }
    return jsonify(response)

# ------------------ VALIDATING WEBHOOK ------------------ #
@app.route('/validate', methods=['POST'])
def validate():
    request_info = request.get_json()
    pod = request_info['request']['object']
    labels = pod.get('metadata', {}).get('labels', {})
    allowed = 'maintainer' in labels

    response = {
        "response": {
            "uid": request_info['request']['uid'],
            "allowed": allowed,
            "status": {
                "code": 403 if not allowed else 200,
                "message": "Missing required 'maintainer' label." if not allowed else "Validation passed."
            }
        }
    }
    return jsonify(response)

# ------------------ ENTRY POINT ------------------ #
if __name__ == '__main__':
    # One server, two paths — runs with TLS
    app.run(host='0.0.0.0', port=443, ssl_context=('tls.crt', 'tls.key'))
