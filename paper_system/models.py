from paper_system.extensions import db


class User(db.Model):
    __abstract__ = True
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), primary_key=True)
    password_hash = db.Column(db.String)
    institution = db.Column(db.String(120))


class Student(User):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    registration = db.Column(db.String(120))


class Professor(User):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    academic_title = db.Column(db.String(120))
    research_area = db.Column(db.String)


class Admin(User):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)