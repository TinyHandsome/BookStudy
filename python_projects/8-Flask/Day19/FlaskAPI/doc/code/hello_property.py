import hashlib


class Student:

    def __init__(self, _password=None):
        self._password = _password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = hashlib.new('md5', value.encode('utf-8')).hexdigest()

    @password.getter
    def password(self):
        return 'xx'


if __name__ == '__main__':
    student = Student()
    student.password = '110'
    print(student.password)