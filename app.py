import os

from flask import Flask
from flask_cors import CORS

from database import init_db
from graphql_api import set_routes

app = Flask(__name__)

if os.environ.get('APP_MODE') == 'local':
    app.debug = True
    CORS(app)

set_routes(app)

if __name__ == '__main__':
    init_db()
    app.run()
