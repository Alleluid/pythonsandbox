import string
from collections import namedtuple, defaultdict
import random
from time import sleep


def testing1():
    # Can mutables be in tuples
    # yes
    lst = list(range(10))
    tup = ("one", 2, lst)
    print(tup)
    tup[2].append(10)
    print(tup)


def testing2():
    class RandoForever:
        def __init__(self, num):
            self.num = num

        def __next__(self):
            return random.randint(1, self.num)

        def __iter__(self):
            return self

    class RandoChr:
        chars = string.ascii_letters

        def __next__(self):
            return random.choice(RandoChr.chars)

        def __iter__(self):
            return self

    for r in RandoChr():
        print(r, end='')
        # sleep(0.1)


def str_to_bin(original_str):
    binarys = []
    for l in original_str:
        b = '{0:b}'.format(ord(l))
        binarys.append(b)
    return ''.join(binarys)


if __name__ == '__main__':
    print(str_to_bin(str_to_bin("test")))
