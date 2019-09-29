"""
    Utils has nothing to do with models and views.
"""

import string
import random
import os

from datetime import datetime


# Instance folder path, make it independent.
INSTANCE_FOLDER_PATH = basedir = os.path.abspath(os.path.dirname(__file__))

ALLOWED_AVATAR_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# Model
STRING_LEN = 64

from itsdangerous import URLSafeTimedSerializer

from flask import current_app


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration=604800):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=current_app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return 'Invalid Token'
    return email



def get_current_time():
    return datetime.utcnow()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_AVATAR_EXTENSIONS


def id_generator(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def make_dir(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    except Exception as e:
        raise e