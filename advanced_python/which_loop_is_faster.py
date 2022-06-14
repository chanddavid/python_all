import timeit

import numpy


def while_loop(n=100):
    a = 0
    i = 0
    while(i < n):
        a += i
        i += 1
    return a


def for_loop(n=100):
    a = 0
    for i in range(n):
        a += i
    return a


def sum_range(n=100):
    return sum(range(n))


def numpy_range(n=100):
    return numpy.sum(numpy.arange(n))


def math_sum(n=100):
    return (n*(n-1))//2


def main():
    print('while loop\t\t', timeit.timeit(while_loop, number=1))
    print('for loop\t\t', timeit.timeit(for_loop, number=1))
    print('sum range\t\t', timeit.timeit(sum_range, number=1))
    print('numpy range\t\t', timeit.timeit(numpy_range, number=1))
    print('math sum\t\t', timeit.timeit(math_sum, number=1))


if __name__ == '__main__':
    main()
