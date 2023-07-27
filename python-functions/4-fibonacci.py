#!/usr/bin/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci = [0, 1]
    for i in range(2, n):
        next_fibonacci = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_fibonacci)

    return fibonacci
