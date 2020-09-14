#!/usr/bin/env python
import math
import numpy as np
import time


def factorize(n: int):
    """nを素因数分解する"""
    # 2
    count = 0
    while n % 2 == 0:
        count += 1
        n = n // 2
    if count > 0:
        arr = [(2, count)]
    else:
        arr = []

    # 3 以降
    for facter in range(3, n + 1, 2):
        if facter * facter > n:
            if n > 1:
                arr.append((n, 1))
            break
        count = 0
        while n % facter == 0:
            count += 1
            n = n // facter
        if count > 0:
            arr.append((facter, count))

    return arr


class Factorize:
    """最初に素数を求めてから素因数分解する"""

    def __init__(self, max_n):
        """max_n: 因数分解されると想定される最大の整数"""
        self.sieve(math.floor(math.sqrt(max_n)))
        return

    def sieve(self, n):
        """n以下の素数を計算"""
        if n < 2:
            self.primes = []
            return
        self.primes = [2]
        if n == 2:
            return
        flags = np.array([True for i in range(3, n + 1, 2)])
        for i in range(len(flags)):
            if flags[i]:
                prime = i * 2 + 3
                self.primes.append(prime)
                flags[i::prime] = False
        return

    def factorize(self, n):
        """nを素因数分解する"""
        arr = []
        for prime in self.primes:
            if prime * prime > n:
                if prime != 1:
                    arr.append((n, 1))
                    return arr
            count = 0
            while n % prime == 0:
                count += 1
                n = n // prime
            if count > 0:
                arr.append((prime, count))


if __name__ == "__main__":
    n = 2 ** 4 * 1000000007
    print(n)
    t0 = time.time()
    print(factorize(n))
    print(time.time() - t0)

    print('init')
    t0 = time.time()
    f = Factorize(n)
    print(time.time() - t0)
    print('init done')
    t0 = time.time()
    print(f.factorize(n))
    print(time.time() - t0)
