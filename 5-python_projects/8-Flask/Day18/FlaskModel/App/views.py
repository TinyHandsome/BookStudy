import random

from flask import Blueprint, render_template, url_for, request
from sqlalchemy import text, and_, or_

from .ext import db, cache
from .models import Student, Cat, Dog, Customer, Address

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


@blue.route('/adddogs/')
def add_dogs():
    for i in range(20):
        dog = Dog()
        dog.a_name = "二哈%d" % random.randrange(10000)
        db.session.add(dog)
    db.session.commit()

    return 'Add dogs success'


@blue.route('/getdogs/')
def get_dogs():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get('per_page', 4, type=int)
    dogs = Dog.query.offset(per_page * (page - 1)).limit(per_page)
    return render_template('Dogs.html', dogs=dogs)


@blue.route('/getdogswithpage/')
def get_dogs_with_page():
    # dogs = Dog.query.paginate().items
    pagination = Dog.query.paginate()
    per_page = request.args.get('per_page', 4, type=int)

    return render_template('Dogs.html', pagination=pagination, per_page=per_page)


@blue.route('/getcatsfilterby/')
def get_cats_filter_by():
    cats = Cat.query.filter_by(id=3)
    return render_template('Cats.html', cats=cats)


@blue.route('/addcustomer/')
def add_customer():
    customer = Customer()
    customer.c_name = '剁手党%d' % random.randrange(1000)

    db.session.add(customer)
    db.session.commit()

    return 'Customer Add Success %s' % customer.c_name


@blue.route('/addaddress/')
def add_address():
    address = Address()
    address.a_position = "皮卡丘%d" % random.randrange(10000)

    address.a_customer_id = Customer.query.order_by(text("-id")).first().id
    db.session.add(address)
    db.session.commit()
    return 'address add success %s' % address.a_position


@blue.route('/getcustomer/')
def get_customer():
    a_id = request.args.get('a_id', type=int)
    address = Address.query.get_or_404(a_id)

    customer = Customer.query.get(address.a_customer_id)
    return customer.c_name


@blue.route('/getaddresses/')
def get_addresses():
    c_id = request.args.get('c_id')
    customer = Customer.query.get(c_id)
    # address = Address.query.filter_by(a_customer_id=customer.id)
    address = customer.address

    return render_template('AddressList.html', address=address)


@blue.route('/getaddresseswithcon/')
@cache.cached(timeout=60)
def get_addresses_with_con():
    # addresses = Address.query.filter(Address.a_customer_id.__eq__(21)).filter(Address.a_position.endswith('6'))
    addresses = Address.query.filter(or_(Address.a_customer_id.__eq__(21), Address.a_position.endswith('6')))
    print("从数据库中查询")

    return render_template('AddressList.html', address=addresses)
