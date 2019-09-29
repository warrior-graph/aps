from .extensions import ma
from .models import *


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = StudentModel


class ProfessorSchema(ma.ModelSchema):
    class Meta:
        model = ProfessorModel
