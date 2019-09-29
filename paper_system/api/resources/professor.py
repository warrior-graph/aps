from flask_restful import Resource

from paper_system.extensions import db
from paper_system.models import ProfessorModel
from paper_system.schemas import ProfessorSchema
from .user import user_parser_post, user_parser_get


class ProfessorResource(Resource):
    def post(self):
        parser = user_parser_post.copy()
        parser.add_argument(
            'registration', help='Registration field cannot be blank', required=True, type=str)
        data = parser.parse_args()

        professor = ProfessorModel(name=data['name'], email=data['email'], password=data['password'],
                                   institution=data['institution'], academic_title=data['academic_title'],
                                   research_area=data['research_area'])
        db.session.add(professor)

        try:
            db.session.commit()
            return 'Professor was created'
        except Exception as e:
            return {'message': 'Could not insert professor on database', 'database_error': str(e)}, 500

    def get(self, professor_id=None):
        parser = user_parser_get.copy()
        parser.add_argument('academic_title')
        parser.add_argument('research_area')
        data = parser.parse_args()
        has_id = bool(professor_id)
        professor_schema = ProfessorSchema(many=(not has_id), exclude=['password_hash'])

        if has_id:
            professor = ProfessorModel.query.get(professor_id)
            if professor:
                return {'professor': professor_schema.dump(professor)}
            return {'message': 'Professor not found'}, 404

        query = ProfessorModel.query
        if data['name']:
            query = query.filter(ProfessorModel.name == data['name'])
        if data['email']:
            query = query.filter(ProfessorModel.email == data['email'])
        if data['institution']:
            query = query.filter(ProfessorModel.institution == data['institution'])
        if data['academic_title']:
            query = query.filter(ProfessorModel.registration == data['academic_title'])
        if data['research_area']:
            query = query.filter(ProfessorModel.registration == data['research_area'])

        return {'professors': professor_schema.dump(query.all())}
