from App.ext import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)