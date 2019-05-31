import os

from flask import jsonify, request
from flask.json import load

from shema import schema


def set_routes(app):

    def query():
        data = request.data.decode('utf-8')

        result = schema.execute(data)

        return jsonify(result.data)

    def fake_query():
        current_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(current_path, "../resources/campaigns.json")
        with open(path) as f:
            return jsonify(load(f))

    app.add_url_rule('/', 'query', fake_query, methods=['POST', 'OPTIONS'])
