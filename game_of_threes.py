def play(num):
    while num > 1:
        div, mod = divmod(num, 3)
        if mod == 0:
            print(num, '0')
            num = div
        elif mod == 1:
            print(num, '-1')
            num = (num - 1) / 3
        elif mod == 2:
            print(num, '+1')
            num = (num + 1) / 3

    print('1')


def testing():
    play(100)


if __name__ == '__main__':
    testing()
