from celery import shared_task


@shared_task
def add(x, y):
    print("Hello, Celery!")
    return x + y
