import time


def calculate_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        re = func(*args, **kwargs)
        stop_time = time.time()
        print('执行时间是:', stop_time - start_time)
        return re

    return wrapper


@calculate_execute_time
def fun01():
    for item in range(1000000):
        pass


@calculate_execute_time
def fun02():
    for item in range(100000):
        pass


fun01()
fun02()
