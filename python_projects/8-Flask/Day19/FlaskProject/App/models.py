from werkzeug.security import check_password_hash, generate_password_hash

from App.ext import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    n_title = db.Column(db.String(32))
    n_content = db.Column(db.String(256))


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16), unique=True)
    _s_password = db.Column(db.String(256))

    @property
    def s_password(self):
        raise Exception("Error  Action： Password can't be access")

    @s_password.setter
    def s_password(self, value):
        self._s_password = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self._s_password, password)
