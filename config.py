import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = 'postgres://bycwfdqx:NuxjtS4FXDUdMuXPDVT5qqK_95OWPkUj@motty.db.elephantsql.com:5432/bycwfdqx'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
