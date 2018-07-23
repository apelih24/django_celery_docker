from celery_test.celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def add(x: int, y: int) -> int:
    return x + y
