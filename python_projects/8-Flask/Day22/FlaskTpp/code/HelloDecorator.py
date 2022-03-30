from time import sleep, time


def calc_time(func):
    def wrapper(*args):
        before = time()
        func(*args)
        after = time()

        print("play time", after - before)

    return wrapper


@calc_time
def play(name_game, t=3, level=20):
    print("小花正在打游戏" + name_game)
    sleep(t)
    print('游戏结束')


if __name__ == '__main__':
    play("阴阳师")
