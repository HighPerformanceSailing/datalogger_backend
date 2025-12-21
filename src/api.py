
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class API:
    logger = None

    @app.route('/api/data', methods=['GET'])
    def data():
        if(API.logger):
            return jsonify(data=API.logger.data_record)
        return jsonify(data={})

    def runAPI(self, logger_obj):
        API.logger = logger_obj
        app.run(debug=True, host="0.0.0.0", port=5005)
