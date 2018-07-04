# https://www.reddit.com/r/dailyprogrammer/comments/8q96da/
import os
import requests


def i_before_e(string: str):
    if 'cie' not in string:
        if 'cei' in string:
            return True
        elif 'ei' not in string:
            return True
    return False


def check_lines_words(lines):
    count = 0
    for word in lines:
        if not i_before_e(word):
            count += 1
    return count


if __name__ == '__main__':
    entry1 = requests.get("https://norvig.com/ngrams/enable1.txt")
    print(len(entry1.text.split("\n")))
    print(check_lines_words(entry1.text.split("\n")))
