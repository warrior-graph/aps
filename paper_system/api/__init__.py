from flask import Blueprint
from flask_restful import Api

from .resources.professor import ProfessorResource
from .resources.student import StudentResource
from .resources.auth import UserLogin

api = Blueprint('api', __name__, url_prefix='/api')

student_api_wrapper = Api(api)
student_api_wrapper.add_resource(StudentResource, '/student')
student_api_wrapper.add_resource(StudentResource, '/student/<int:student_id>', endpoint='/student')

professor_api_wrapper = Api(api)
professor_api_wrapper.add_resource(ProfessorResource, '/professor')
professor_api_wrapper.add_resource(ProfessorResource, '/professor/<int:professor_id>', endpoint='/professor')


login_api_wrapper = Api(api)
login_api_wrapper.add_resource(UserLogin, '/login')
