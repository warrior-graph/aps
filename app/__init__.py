from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from app.models import AlunoModelo

@app.before_request
def create_all():
    db.create_all()
    db.commit()


@app.route('/criar_aluno')
def criar_aluno():
    query_aluno = db.session.query(AlunoModelo).filter_by(matricula='123123').first()
    if query_aluno:
        return 'Aluno existente'
    aluno = AlunoModelo(nome='Gabriel', email='gabriel@aluno.uece.br', matricula='123123')
    db.session.add(aluno)
    try:
        db.session.commit()
    except:
        return 'Alguma coisa deu errado'
    return 'Aluno adicionado'


from app import models