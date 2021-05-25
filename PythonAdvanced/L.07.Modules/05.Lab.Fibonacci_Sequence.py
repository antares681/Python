from functools import lru_cache

def create_sequence(n):
    assert n >= 1
    if n == 1:
        fibonacciSequence = [0]
    elif n == 2:
        fibonacciSequence = [0, 1]
        create_sequence(fibonacciSequence)
    else:
        fibonacciSequence = [0, 1]
        for n in range(0, n-2)
            fibonacciSequence.append(fibonacciSequence[-1] + fibonacciSequence[-2])
        fibonacciSequence = [n]
    return fibonacciSequence

create_sequence(int(input()))


