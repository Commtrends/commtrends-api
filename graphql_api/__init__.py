from flask import jsonify, request
from flask_graphql import GraphQLView

from graphql_api.campaign import get_random_campaign
from shema import schema


def set_routes(app):

    def query():
        data = request.data.decode('utf-8')

        result = schema.execute(data)

        return jsonify(result.data)

    def fake_query():
        data = get_random_campaign()
        return jsonify(data)

    app.add_url_rule('/', 'query', fake_query, methods=['POST', 'OPTIONS'])

    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
