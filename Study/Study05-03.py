#斐波那契数列

import time

def fib(i, j, count):
    count += 1
    z = i + j
    if count == 100:
        print(z)
        return
    print(z, end=", ")
    fib(j, z, count)


if __name__ == '__main__':
    time1 = time.time()
    print(1, 1, end=", ")
    fib(1, 1, 2)
    time2 = time.time()
    print(time2 - time1)

    time1 = time.time()
    a = 0
    b = 1
    for _ in range(100):
        a, b = b, a + b
        print(a, end=' ')
    time2 = time.time()
    print(time2 - time1)

