from App.ext import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    n_title = db.Column(db.String(32))
    n_content = db.Column(db.String(256))
