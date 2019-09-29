from flask_restful import Resource

from paper_system.extensions import db
from paper_system.models import StudentModel
from paper_system.schemas import StudentSchema
from .user import user_parser_post, user_parser_get


class StudentResource(Resource):
    def post(self):
        parser = user_parser_post.copy()
        parser.add_argument(
            'registration', help='Registration field cannot be blank', required=True, type=str)
        data = parser.parse_args()

        student = StudentModel(name=data['name'], email=data['email'], password=data['password'],
                               institution=data['institution'], registration=data['registration'])
        db.session.add(student)

        try:
            db.session.commit()
            return 'Student was created'
        except Exception as e:
            return {'message': 'Could not insert student on database', 'database_error': str(e)}, 500

    def get(self, student_id=None):
        parser = user_parser_get.copy()
        parser.add_argument('registration')
        data = parser.parse_args()
        has_id = bool(student_id)
        student_schema = StudentSchema(many=(not has_id), exclude=['password_hash'])

        if has_id:
            student = StudentModel.query.get(student_id)
            if student:
                return {'student': student_schema.dump(student)}
            return {'message': 'Student not found'}, 404

        query = StudentModel.query
        if data['name']:
            query = query.filter(StudentModel.name == data['name'])
        if data['email']:
            query = query.filter(StudentModel.email == data['email'])
        if data['institution']:
            query = query.filter(StudentModel.institution == data['institution'])
        if data['registration']:
            query = query.filter(StudentModel.registration == data['registration'])

        return {'students': student_schema.dump(query.all())}
