from app import db


class UsuarioModelo(db.Model):
    __abstract__ = True
    nome = db.Column(db.String(120))
    email = db.Column(db.String(120), primary_key=True)
    hash_senha = db.Column(db.String)
    instuticao = db.Column(db.String(120))


class AlunoModelo(UsuarioModelo):
    __tablename__ = 'aluno'
    id = db.Column(db.Integer, primary_key=True)
    id_evento = db.Column(db.Integer, db.ForeignKey('evento.id'))
    matricula = db.Column(db.String(120))

    evento = db.relationship('EventoModelo', back_populates='alunos')
    artigos = db.relationship('ArtigoModelo', back_populates='aluno')


class ProfessorModelo(UsuarioModelo):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    id_evento = db.Column(db.Integer, db.ForeignKey('evento.id'))
    titulacao = db.Column(db.String(120))
    area_de_pesquisa = db.Column(db.String)

    evento = db.relationship('EventoModelo', back_populates='professores')
    artigos = db.relationship('ArtigoModelo', back_populates='professor')


class AdministradorModelo(UsuarioModelo):
    __tablename__ = 'administrador'
    id = db.Column(db.Integer, primary_key=True)


class EventoModelo(db.Model):
    __tablename__ = 'evento'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    sigla = db.Column(db.String(20))
    data_inicio = db.Column(db.DateTime)
    data_fim = db.Column(db.DateTime)
    palavras_chave = db.Column(db.ARRAY(db.String))
    area_de_concentracao = db.Column(db.String(256))

    alunos = db.relationship('AlunoModelo', back_populates='evento')
    professores = db.relationship('ProfessorModelo', back_populates='evento')
    artigos = db.relationship('ArtigoModelo', back_populates='evento')


class ArtigoModelo(db.Model):
    __tablename__ = 'artigo'
    id = db.Column(db.Integer, primary_key=True)
    id_professor = db.Column(db.Integer, db.ForeignKey('professor.id'))
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id'))
    id_evento = db.Column(db.Integer, db.ForeignKey('evento.id'))
    titulo = db.Column(db.String(256))
    lista_de_autores = db.Column(db.ARRAY(db.String))
    resumo = db.Column(db.Binary) # Arquivo
    status = db.Column(db.String(256))

    professor = db.relationship('ProfessorModelo', back_populates='artigos')
    aluno = db.relationship('AlunoModelo', back_populates='artigos')
    evento = db.relationship('EventoModelo', back_populates='artigos')

