

from flask import Flask, request, jsonify
from handlers.create_event_handler import handle_create_event
from handlers.read_event_handler import handle_get_event
from handlers.update_event_handler import handle_update_event
from handlers.delete_event_handler import handle_delete_event

app = Flask(__name__)

@app.route('/create_event', methods=['POST'])
def create_event():
    event_details = request.json
    try:
        result = handle_create_event(event_details)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_event', methods=['GET'])
def get_event():
    event_id = request.args.get('event_id')
    try:
        result = handle_get_event(event_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/update_event', methods=['PUT'])
def update_event():
    event_id = request.json.get('event_id')
    updated_details = request.json
    try:
        result = handle_update_event(event_id, updated_details)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/delete_event', methods=['DELETE'])
def delete_event():
    event_id = request.json.get('event_id')
    try:
        result = handle_delete_event(event_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
