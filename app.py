# Python libs
from flask import Flask, request, jsonify
import json

# Starting API
app = Flask(__name__)

# Routes (endpoints)
@app.route("/", methods=['GET'])
def base():
    return "<p> main route </p>"

@app.route('/send_json', methods=['POST'])
def receive_json():
    return json.dumps(request.get_json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)