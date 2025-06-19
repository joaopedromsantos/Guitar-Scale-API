from flask import Flask, jsonify, request

from guitar_scale import GuitarScale

app = Flask(__name__)

@app.route('/scales', methods=['GET'])
def get_scale():
    key = request.args.get('key')
    scale_type = request.args.get('type')

    if not key:
        return jsonify({"error": "Missing 'key' parameter. Example: /scales?key=C&type=major"}), 400
    if not scale_type:
        return jsonify({"error": "Missing 'type' parameter. Example: /scales?key=C&type=major"}), 400

    try:
        guitar_scale = GuitarScale(key, scale_type)

        response_data = {
            "tonic": guitar_scale.key,
            "scaleNotes": guitar_scale.scale_notes
        }

        if scale_type == 'blues':
            response_data['blueNote'] = guitar_scale.blue_note

        return jsonify(response_data), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
