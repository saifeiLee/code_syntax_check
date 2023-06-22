import os
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    from . import syntax_check
    app.register_blueprint(syntax_check.bp)
    return app
