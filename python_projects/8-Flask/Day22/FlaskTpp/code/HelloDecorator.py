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


if __name__ == '__main__':
    play("阴阳师")
