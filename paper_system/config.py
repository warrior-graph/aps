import os

from paper_system.utils import INSTANCE_FOLDER_PATH


class BaseConfig(object):
    PROJECT = 'paper_system'

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = True
    TESTING = False

    ADMINS = ['humberto.marques@aluno.uece.br']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'you-will-never-gess'
    SECURITY_PASSWORD_SALT = 'you-will-never-gess'

    LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')

    # Fild upload, should override in production.
    # Limited the maximum allowed payload to 16 megabytes.
    # http://flask.pocoo.org/docs/patterns/fileuploads/#improving-uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'uploads')


class DefaultConfig(BaseConfig):
    DEBUG = True

    SENTRY_DSN = ''

    MAIL_HOST = ''
    FROM_ADDR = ''
    TO_ADDRS = ['']
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

    # Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_ECHO = False
    # QLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be
    # disabled by default in the future.
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = \
        'postgres://bycwfdqx:NuxjtS4FXDUdMuXPDVT5qqK_95OWPkUj@motty.db.elephantsql.com:5432/bycwfdqx'


class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
