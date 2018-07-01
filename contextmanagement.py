import itertools
import os
import sys
import time as t


class Timer:
    def __init__(self):
        self.time = 0
        self.difference = 0
        self.result_str = "Not Run Yet"

    def __enter__(self):
        self.time = t.clock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.difference = t.clock() - self.time
        self.result_str = f"Exec time: {self.difference:.6} seconds"

    def __str__(self):
        return self.result_str

    def result(self):
        print(self.result_str)


def timeit(func):
    def wrapper(*args):
        with Timer() as timer:
            original = func(*args)
            print(timer)
        return original

    return wrapper


def operation(a):
    for i in range(1000):
        _ = i ** i


class TestObj:
    def __init__(self):
        self.test = "dfg"

    def __enter__(self):
        self.test = "test"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


with TestObj() as testy:
    print(testy.test)


with Timer() as timer:
    operation(6)
    time_taken = timer.result
print(time_taken)
