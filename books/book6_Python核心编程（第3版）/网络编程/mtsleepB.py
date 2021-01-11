import _thread as thread
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at: ', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
    lock.release()


def main():
    print('starting at: ', ctime())
    locks = []
    nloops = range(len(loops))

    # 首先创建一个锁列表
    for i in nloops:
        # 得到锁对象，获取锁需要花费一些时间
        lock = thread.allocate_lock()
        # 获得每个锁，把锁锁上
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    # 等待/暂停主线程，直到所有锁都被释放之后才会继续执行。
    for i in nloops:
        while locks[i].locked():
            pass

    print('all Done at: ', ctime())


if __name__ == '__main__':
    main()
