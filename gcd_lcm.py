#!/usr/bin/env python
from functools import reduce


def gcd(a, b):
    """最大公約数
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """最小公倍数
    """
    return a * b // gcd(a, b)


if __name__ == "__main__":
    # 複数あるとき
    X = [4, 6, 8, 40, 128]
    print("X", X)
    print("gcd", reduce(gcd, X))
    print("lcm", reduce(lcm, X))
