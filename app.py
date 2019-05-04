from flask import Flask, jsonify

from shema import schema

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    result = schema.execute('{ hello (argument: "graph")}')

    return jsonify(result.data)
