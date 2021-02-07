from multiprocessing import Process
import time
import os


# 唱歌
def sing(num):
    print('唱歌进程的pid：', os.getpid())
    print('唱歌父进程的pid：', os.getppid())
    for i in range(num):
        print('唱歌...')
        time.sleep(0.5)


# 跳舞
def dance(num2):
    print('跳舞进程的pid：', os.getpid())
    print('跳舞父进程的pid：', os.getppid())
    for i in range(num2):
        print('跳舞...')
        time.sleep(0.5)


if __name__ == '__main__':
    print('主进程的pid：', os.getpid())
    p1 = Process(target=sing, args=(5,))
    p2 = Process(target=dance, kwargs={'num2': 2})

    p1.start()
    p2.start()
