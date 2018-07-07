import random
from collections import Counter


def roll(count, die, roll_list=False):
    rolls = []
    for i in range(count):
        rolls.append(random.randint(1, die))
    if roll_list:
        return rolls
    else:
        return sum(rolls)


def testing():
    print("3d6:", Counter([roll(3, 6) for i in range(100_000)]))
    print("1d20:", Counter([roll(1, 20) for i in range(100_000)]))


if __name__ == '__main__':
    testing()
