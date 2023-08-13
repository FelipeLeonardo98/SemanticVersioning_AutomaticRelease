from flask import Flask, request, jsonify
import json, requests

app = Flask(__name__)

@app.route("/", methods=['GET'])
def base():
    return "<p> main route </p>"

@app.route('/send_json_to_brazil', methods=['POST'])
def send_and_callback():
    package = json.dumps(request.get_json())
    brazil_response = requests.post('http://127.0.0.1:7001/send_json', json=package)
    return json.dumps(brazil_response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)