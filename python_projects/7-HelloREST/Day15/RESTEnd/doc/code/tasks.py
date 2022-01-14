from time import sleep

from celery import Celery

app = Celery("tasks", broker='redis://localhost:6379/1')


@app.task
def add(a, b):
    sleep(5)
    return a + b


if __name__ == '__main__':
    # print(add(4, 6))
    print(add.delay(4, 6))
