from random import randint
from time import sleep
from queue import Queue
from myThread import MyThread

def writeQ(queue):
    print('producing object for Q...', end='')
    queue.put('xxx', 1)
    print('size now', queue.qsize())

def readQ(queue):
    val = queue.get(1)
    print('consumed object from Q...size now', queue.qsize())

def writer(queue, loops):
    print('制造了', loops, '个生产者！')
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))

def reader(queue, loops):
    print('制造了', loops, '个消费者！')
    for i in range(loops):
        readQ(queue)
        sleep(randint(3, 5))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    q = Queue(maxsize=32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], [q, nloops], funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('all DONE')

if __name__ == '__main__':
    main()