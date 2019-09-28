import os

from flask import Blueprint

from paper_system.extensions import db
from paper_system.user.models import Student

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<email>/<name>', methods=['POST'])
def dummy(email, name):
    student = Student.query.filter(Student.email == email).first()
    if student:
        return 'Student exists'
    student = Student(name=name, email=email)
    db.session.add(student)
    try:
        db.session.commit()
        return 'Success'
    except Exception as e:
        return str(e)


@user.route('/<email>', methods=['GET'])
def dummy1(email):
    student = Student.query.filter(Student.email == email).first()
    if student:
        return 'Student {} exists'.format(student.name)
    
    return 'Not found'