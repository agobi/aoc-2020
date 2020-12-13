# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/13

>>> data = parse("day13/test.txt")
>>> solve1(*data)
295
"""


import sys
from functools import reduce


def parse(fn):
    with open(fn, "rt") as f:
        earliest = int(f.readline())
        buses = [
            (idx, int(x))
            for idx, x in enumerate(f.readline().split(","))
            if x != "x"
        ]

    return earliest, buses


def solve1(earliest, buses):
    bus, wait_time = min(
        ((x, x - earliest % x) for _, x in buses),
        key=lambda x: x[1]
    )

    return bus * wait_time


def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def solve_pair(e1, e2):
    (a, m) = e1
    (b, n) = e2
    g, u, v = xgcd(m, n)
    lcm = m * n / g
    t = (a*v*(n / g) + b*u*(m / g)) % lcm
    return t, lcm


def solve2(buses):
    return reduce(solve_pair, ((-x % m, m) for x, m in buses))[0]


if __name__ == '__main__':
    earliest, buses = parse(sys.argv[1])
    print(solve1(earliest, buses))
    print(solve2(buses))
