from App.ext import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))


class User(db.Model):
    __tablename__ = 'UserModel'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(16), unique=True)
    u_des = db.Column(db.String(128), nullable=True)


class Animal(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_name = db.Column(db.String(16))


class Dog(Animal):
    d_legs = db.Column(db.Integer, default=4)


class Cat(Animal):
    c_eat = db.Column(db.String(32), default='fish')
