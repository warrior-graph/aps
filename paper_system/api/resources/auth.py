from flask_jwt_extended import (create_access_token,
                                create_refresh_token)
from flask_restful import Resource

from paper_system.extensions import auth
from paper_system.models import StudentModel, ProfessorModel
from paper_system.schemas import StudentSchema, ProfessorSchema


class UserLogin(Resource):

    @auth.verify_password
    def verify(username, password):
        if not (username and password):
            return False
        student = StudentModel.query.filter(StudentModel.email == username).first()

        if student:
            return student.verify_password(password)

        professor = ProfessorModel.query.filter(ProfessorModel.email == username).first()

        if professor:
            return professor.verify_password(password)

        return False

    @auth.login_required
    def post(self):
        professor_schema = ProfessorSchema()
        student_schema = StudentSchema()
        user_identity = None
        student = StudentModel.query.filter(StudentModel.email == auth.username()).first()

        if student:
            user_identity = student_schema.dump(student)
            user_identity['role'] = 'student'

        professor = ProfessorModel.query.filter(ProfessorModel.email == auth.username()).first()

        if professor:
            user_identity = professor_schema.dump(professor)
            user_identity['role'] = 'professor'

        if user_identity:
            access_token = create_access_token(identity=user_identity)
            refresh_token = create_refresh_token(
                identity=user_identity)
            return {
                'message': 'Logged in as {}'.format(user_identity['email']),
                'access_token': access_token,
                'refresh_token': refresh_token,
                'role': user_identity['role'],
            }
        else:
            return {'message': 'Wrong credentials'}, 401
