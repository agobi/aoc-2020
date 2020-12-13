# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/5

>>> input = parse("day05/test.txt")
>>> solve1(input)
820
"""


import sys


def parse(fn):
    with open(fn, "rt") as f:
        return [line.strip() for line in f]


def code(b):
    ret = 0
    for i in b:
        ret *= 2
        if i in ('B', 'R'):
            ret += 1
    return ret


def solve1(data):
    return max(code(b) for b in data)


def solve2(data):
    seats = set(range(0, 1024))
    for b in data:
        seats.remove(code(b))

    for s in seats:
        if s-1 not in seats and s+1 not in seats:
            return s


if __name__ == '__main__':
    data = parse(sys.argv[1])
    print(solve1(data))
    print(solve2(data))
