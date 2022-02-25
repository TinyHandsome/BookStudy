import random

from flask import Blueprint, render_template, url_for, request

from .ext import db
from .models import Student, Cat, Dog

blue = Blueprint("blue", __name__, template_folder='../templates', url_prefix='/db')


def init_blue(app):
    app.register_blueprint(blue)


@blue.route('/')
def index():
    return 'Hello'


@blue.route('/addstudent/')
def add_student():
    student = Student()
    student.name = "小花%d" % random.randrange(10000)
    db.session.add(student)
    db.session.commit()

    print(db.session)
    print(type(db.session))

    return 'Add Success'


@blue.route('/addstudents/')
def add_students():
    students = []
    for i in range(5):
        student = Student()
        student.name = "小明%d" % i
        students.append(student)

    db.session.add_all(students)
    db.session.commit()

    return "Add students Success"


@blue.route('/getstudent/')
def get_student():
    # student = Student.query.first()
    # 没有last
    # student = Student.query.get_or_404(20)

    student = Student.query.get(21)
    print(student)

    return 'success'


@blue.route('/getstudents/')
def get_students():
    students = Student.query.all()

    for s in students:
        print(s.name)

    # return 'Get Students Success'
    return render_template('StudengList.html', students=students)


@blue.route('/deletestudent/')
def delete_student():
    student = Student.query.first()
    db.session.delete(student)
    db.session.commit()

    return 'Delete Success'


@blue.route('/updatestudent/')
def update_student():
    student = Student.query.first()
    student.name = "Tom"
    db.session.add(student)
    db.session.commit()

    return 'Update Success'


@blue.route('/redir/')
def redir():
    url = url_for('blue.get_student', id=1)
    return url


@blue.route('/addcat/')
def add_cat():
    cat = Cat()
    cat.a_name = "加菲猫"
    cat.c_eat = "骨头"

    db.session.add(cat)
    db.session.commit()

    return 'Cat add Success'


@blue.route('/adddog/')
def add_dog():
    dog = Dog()
    dog.d_legs = 5
    dog.a_name = "傻狗"
    db.session.add(dog)
    db.session.commit()

    return 'Dog Add Success'


@blue.route('/getcats/')
def get_cats():
    # cats = Cat.query.filter(Cat.id.__lt__(5)).all()
    # cats = Cat.query.filter(Cat.id == 2)

    cats = Cat.query.offset(1).limit(2)

    return render_template('Cats.html', cats=cats)


@blue.route('/getdogs/')
def get_dogs():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get('per_page', 4, type=int)
    dogs = Dog.query.offset(per_page * (page - 1)).limit(per_page)
