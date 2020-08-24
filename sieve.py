#!/usr/bin/env python

import numpy as np

# 0  1  2  3  4  5  6
# 3  5  7  9 11 13 15
# *        *        *   [0::3]
#    *              *   [1::5]


def sieve(n: int):
    """n以下の(1を含む)素数を返す"""
    if n == 1:
        return [1]
    primes = [1, 2]
    if n == 2:
        return primes
    flags = np.array([True for i in range(3, n + 1, 2)])
    for i in range(len(flags)):
        if flags[i]:
            n = i * 2 + 3
            primes.append(n)
            flags[i::n] = False
    return primes


if __name__ == "__main__":
    n = 10 ** 8
    print(n, len(sieve(n)))
