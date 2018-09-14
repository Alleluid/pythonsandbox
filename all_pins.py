import timeit
import time


def timer(func, repeats=100_000, *args, **kwargs):
    def wrapper():
        def print(*args, **kwargs):
            pass
        times = []
        for i in range(repeats):
            # print("iter", i, end="|")
            start = time.time_ns()
            func(*args, **kwargs)
            times.append(time.time_ns() - start)

        diff = sum(times) / len(times)
        print()
        print(f"time: {diff:,.2f} ns")
        print(f"      {diff / 1_000_000:.2f} ms")
        if diff > 100_000_000:
            print(f"      {diff / 1_000_000_000:.2f} s")
    return wrapper


@timer
def testing1():
    var = "a" + str(range(100)) + "b"


@timer
def testing2():
    var2 = f"a{range(100)!s}b"


testing1()
testing2()