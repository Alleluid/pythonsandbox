import itertools
import os
import sys
import time as t


class Timer:
    def __init__(self):
        self.time = 0
        self.difference = 0

    def __enter__(self):
        self.time = t.clock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.difference = t.clock() - self.time
        print("Exec time (seconds):", self.difference)


with Timer() as timer:
    _ = [i ** i for i in range(1, 1_000)]

with Timer() as timer2:
    for i in itertools.:
        print(i)

"stasd".star