#!/usr/bin/env python


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
        if facter > n:
            break
        count = 0
        while n % facter == 0:
            count += 1
            n = n // facter
        if count > 0:
            arr.append((facter, count))

    return arr


if __name__ == "__main__":
    n = 9973 * (2 * 3 * 5) ** 8
    print(n)
    print(factorize(n))