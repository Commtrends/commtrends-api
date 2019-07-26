import os

from flask import Flask
from flask_cors import CORS

from database import init_db
from graphql_api import set_routes

__app__ = None


def get_app(*args, **kwarg) -> Flask:

    global __app__

    if not __app__:
        __app__ = Flask(__name__, *args, **kwarg)

        if os.environ.get('APP_MODE') == 'local':
            __app__.debug = True

        CORS(__app__)

        set_routes(__app__)

    return __app__


if __name__ == '__main__':
    init_db()
    get_app().run()