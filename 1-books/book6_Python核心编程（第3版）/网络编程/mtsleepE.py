import threading
from time import sleep, ctime

loops = [4, 2]


class MyThread(threading.Thread):
    def __init__(self, f, args, name=''):
        super().__init__()
        self.name = name
        self.f = f
        self.args = args

    def run(self):
        self.f(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at: ', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at: ', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all Done at: ', ctime())


if __name__ == '__main__':
    main()
