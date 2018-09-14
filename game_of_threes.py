def play(num):
    steps = []
    while True:
        result, remainder = divmod(num, 3)
        if result == 1:
            break
        elif remainder == 0:
            steps.append((num, 0))
            num = result
        elif remainder == 1:
            steps.append((num, -1))
            num = num - 1
        elif remainder == 2:
            steps.append((num, +1))
            num = num + 1

    print(*steps, sep='\n')


def main():
    play(100)


if __name__ == '__main__':
    main()
