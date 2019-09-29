from passlib.hash import sha256_crypt
from paper_system.extensions import db


class UserModel(db.Model):
    __abstract__ = True
    name = db.Column(db.String(240))
    email = db.Column(db.String(240), unique=True)
    password_hash = db.Column(db.String)
    institution = db.Column(db.String(240))

    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, password):
        self.password_hash = sha256_crypt.encrypt(password)

    def verify_password(self, password):
        return sha256_crypt.verify(password, self.password_hash)


class StudentModel(UserModel):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    registration = db.Column(db.String(240))


class ProfessorModel(UserModel):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    academic_title = db.Column(db.String(240))
    research_area = db.Column(db.String)


class AdminModel(UserModel):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(240))

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
