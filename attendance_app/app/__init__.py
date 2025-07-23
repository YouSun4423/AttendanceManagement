from flask import Flask
from .views.input import input_bp
from .views.records import records_bp
from .views.summary import summary_bp
from .config import Config
import os


def create_app(test_config=None):
    """
    Flaskアプリケーションのファクトリ関数

    Parameters:
    test_config (dict, optional): テスト用の設定.デフォルトはNone

    Returns:
    Flask: 初期化されたFlaskアプリケーションインスタンス
    """
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder="templates",
        static_folder="static"
    )
    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    app.register_blueprint(input_bp)
    app.register_blueprint(records_bp)
    app.register_blueprint(summary_bp)

    return app
