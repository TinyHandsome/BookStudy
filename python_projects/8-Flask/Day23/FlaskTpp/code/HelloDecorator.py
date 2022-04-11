import random
from time import sleep, time


def calc_time(func):
    def wrapper(*args, **kwargs):
        before = time()
        result = func(*args, **kwargs)
        after = time()

        print("play time", after - before)
        return result

    return wrapper


@calc_time
def play(name_game, t=3, level=20):
    print("小花正在打游戏" + name_game)
    sleep(t)
    print('游戏结束')
    return 'Happy'


def can_play(can):
    def can_play_wrapper(fun):
        def wrapper():
            if random.randrange(10) > can:
                fun()
            else:
                print("do homework")

        return wrapper
    return can_play_wrapper


@can_play(10)
def play_game():
    print("Happy to play")


if __name__ == '__main__':
    play_game()
