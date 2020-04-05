import logging

from flask import Flask

from ogproxy.config import AppConfiguration, StaticConfiguration
from ogproxy.root import blueprint as root_blueprint

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def create_app():
    app = Flask(StaticConfiguration.APP_NAME, template_folder='ogproxy')
    app.config.from_object(AppConfiguration)
    app.config.from_object(StaticConfiguration)

    register_plugins(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(root_blueprint, url_prefix='/')


def register_plugins(app):
    pass
