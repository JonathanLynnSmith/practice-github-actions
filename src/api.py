from flask import Flask, jsonify, request, Response
import json
from linter import validate_commit_message

app = Flask(__name__)

@app.route("/", methods=["GET"])
def read_root():
    return jsonify({"message": "Welcome to the commit message linter API! Use /validate to validate a commit message."})

@app.route("/validate", methods=["POST"])
def validate_commit():
    # Parse the JSON body of the request
    data = request.get_json()
    
    # Check if 'message' is in the request data
    if not data or "message" not in data:
        return jsonify({"error": "No commit message provided"}), 400
    
    commit_message = data["message"]
    
    # Validate the commit message using your linter
    valid, reason = validate_commit_message(commit_message)
    
    # Return the validation result in pretty-printed JSON
    response_data = {
        "valid": valid,
        "reason": reason
    }
    
    return Response(
        json.dumps(response_data, indent=4),
        mimetype='application/json'
    )

@app.route("/validateall", methods=["POST"])
def validate_all_commits():
    data = request.get_json()
    
    # Check if 'messages' is in the request data
    if not data or "messages" not in data:
        return jsonify({"error": "No commit messages provided"}), 400
    
    commit_messages = data["messages"]
    
    results = []
    for message in commit_messages:
        valid, reason = validate_commit_message(message)
        results.append({
            "message": message,
            "valid": valid,
            "reason": reason
        })
    
    # Return the results in pretty-printed JSON
    response_data = {"results": results}
    
    return Response(
        json.dumps(response_data, indent=4),
        mimetype='application/json'
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)
