from flask import Flask

from paper_system.config import DefaultConfig
from paper_system.extensions import db
from paper_system.utils import INSTANCE_FOLDER_PATH


__all__ = ['create_app']


def create_app(config=None, app_name=None):
    '''Create a Flask app.'''
    
    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(app_name, instance_path=INSTANCE_FOLDER_PATH, instance_relative_config=True)

    configure_app(app)
    configure_hook(app)
    configure_blueprint(app)
    configure_extensions(app)
    configure_cli(app)

    return app
    
def configure_app(app, config=None):
    
    app.config.from_object(DefaultConfig)
    
    if config:
        app.config.from_object(config)

def configure_blueprint(app):
    from .user import user
    from .api import api
    for bp in [user, api]:
        app.register_blueprint(bp)

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


