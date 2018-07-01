import itertools as itl
import collections
import string


def logtype(func):
    def wrapper(*args):
        original = func(*args)
        print(f"{func.__name__}: {type(original)}")
        return original
    return wrapper

@logtype
def adder(a, b):
    return a+b

# print(adder(2, 4))

class ReprTest:
    def __init__(self):
        self.string = "string"
        self.represent = "repr"

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.represent

print(ReprTest())