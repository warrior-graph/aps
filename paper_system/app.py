from flask import Flask

from .config import DefaultConfig
from .extensions import db
from .utils import INSTANCE_FOLDER_PATH


__all__ = ['create_app']


def create_app(config=None, app_name=None):
    '''Create a Flask app.'''
    
    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(app_name, instance_path=INSTANCE_FOLDER_PATH, instance_relative_config=True)

    configure_app(app)
    configure_extensions(app)
    configure_hook(app)
    configure_cli(app)

    return app
    
def configure_app(app, config=None):
    
    app.config.from_object(DefaultConfig)
    
    if config:
        app.config.from_object(config)

def configure_extensions(app):
    db.init_app(app)

def configure_hook(app):

    @app.before_request
    def before_request():
        pass

def configure_cli(app):

    @app.cli.command()
    def initdb():
        db.drop_all()
        db.create_all()


