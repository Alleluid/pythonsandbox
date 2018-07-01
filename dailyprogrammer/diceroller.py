# https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/
import random


def main():
    # IDK why I did this.
    def num_as_word(num):
        num_words = ["zero", "one", "two", "three", "four", "five",
                     "six", "seven", "eight", "nine", "ten"]
        return num if num > 10 else num_words[num]
    separator = 'd'
    help_str = f"Dice Roller!\nInput format like '2{separator}6'"
    help_str2 = "Cannot roll less than 1 die, cannot roll less than a d2."

    # Start program
    print(help_str)
    while True:
        input_str = input("> ")
        split_input = input_str.partition(separator)

        # First check that it found the separator and the other characters are numbers
        if split_input[1] is separator and (split_input[0].isnumeric() and split_input[2].isnumeric()):
            count, _, die = split_input
            count = int(count)
            die = int(die)
            # print error for invalid rolls
            if count < 1 or die < 2:
                print(help_str2)
                continue
            print(f"Rolling {num_as_word(count)} {num_as_word(die)}-sided {'die' if count == 1 else 'dice'}: ")
            result = 0
            rolls_list = []
            for _ in range(count):
                roll = random.randint(1, die)
                result += roll
                rolls_list.append(roll)
            print(f"{rolls_list} = {result}")
        else:
            print(help_str)


if __name__ == '__main__':
    main()
