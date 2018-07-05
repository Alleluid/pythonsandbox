import random


def roll(die, count, roll_list=False):
    rolls = []
    for i in range(count):
        rolls.append(random.randint(1, die))
    if roll_list:
        return sum(rolls), rolls
    else:
        return sum(rolls)


def testing():
    pass


if __name__ == '__main__':
    testing()
