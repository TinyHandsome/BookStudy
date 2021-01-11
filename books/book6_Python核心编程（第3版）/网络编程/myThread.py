import threading
from time import ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        super().__init__()
        self.name = name
        self.func = func
        self.args = args
        self.res = None

    def __post_init__(self):
        super().__init__()

    def getResult(self):
        return self.res

    def run(self):
        print('starting', self.name, 'at: ', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at: ', ctime())
