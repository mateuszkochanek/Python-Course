import time
import math

def calculate_time(func):
    def inner_func(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Czas w funkcji: ", end - begin)
    return inner_func


@calculate_time
def sleep_num(num):
    time.sleep(num)

@calculate_time
def big_loop():
    for x in range(1000000000):
        k = x
    return k

sleep_num(10)
big_loop()