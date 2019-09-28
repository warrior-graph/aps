from flask import Blueprint, request

from flask_restful import Api, Resource, reqparse
from ..user.models import Student, Professor
from ..extensions import db


api = Blueprint('api', __name__, url_prefix='/api')
api_wrap = Api(api)


class UserResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument(
            'name', help='Name field cannot be blank', required=True)

        parser.add_argument(
            'email', help='Email field cannot be blank', required=True)
        parser.add_argument(
            'password', help='Password field cannot be blank', required=True)
        parser.add_argument(
            'institution', help='Institution field cannot be blank', required=True)
        parser.add_argument(
            'role', help='Role field cannot be blank', required=True)

        data = parser.parse_args()

        if data['role'] == 'student':
            parser.add_argument(
                'registration', help='Registration field cannot be blank', required=True)
        else:
            parser.add_argument(
                'academic_title', help='Academic Title field cannot be blank', required=True)
            parser.add_argument(
                'research_area', help='Research Area field cannot be blank', required=True)

        data = parser.parse_args()

        if data['role'] == 'student':
            student = Student(id=1, name=data['name'], email=data['email'], password_hash=data['password'],
                              institution=data['institution'], registration=data['registration'])
            db.session.add(student)

            try:
                db.session.commit()
                return 'Student was created'
            except Exception as e:
                return str(e)

        if data['role'] == 'professor':
            professor = Professor(id=1, name=data['name'], email=data['email'], password_hash=data['password'],
                              institution=data['institution'], academic_title=data['academic_title'], research_area=data['research_area'])

            db.session.add(professor)

            try:
                db.session.commit()
                return 'Professor was created'
            except Exception as e:
                return str(e)

    def get(self, name):
        parser = reqparse.RequestParser()

        parser.add_argument(
            'role', help='Role field cannot be blank', required=True)
         
        data = parser.parse_args()
        if data['role'] == 'student':
            student = Student.query.filter(Student.name==name).first()
            if student:
                return {'Student name': student.name}
            return {'Message': 'Not found'}, 404

        if data['role'] == 'professor':
            professor = Professor.query.filter(Professor.name==name).first()
            if professor:
                return {'Professor name': professor.name}
            return {'Message': 'Not found'}, 404

        return {'Something gone wrone'}, 500

api_wrap.add_resource(UserResource, '/user')
api_wrap.add_resource(UserResource, '/user/<name>', endpoint='/user')
