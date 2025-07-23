from flask import Flask
from .views.input import input_bp
from .views.records import records_bp
from .views.summary import summary_bp
from .config import Config
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    app.register_blueprint(input_bp)
    app.register_blueprint(records_bp)
    app.register_blueprint(summary_bp)

    return app
