mylist = list("abcdefghijklmnop")
print(mylist)
print("|".join(mylist))


def join(iterable, string):
    return string.join(iterable)


print(join(mylist, ','))