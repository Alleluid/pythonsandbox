import itertools as itl
import collections
import string

my_tup = collections.namedtuple("my_tup", ("a", "b", "c", "x"))
ord_dict = collections.OrderedDict((a, b) for a, b in zip(string.ascii_uppercase, itl.count()))

for k, v in ord_dict.items():
    print(f"key: {k}, value: {v}")