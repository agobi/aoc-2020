# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/3

>>> pwds = parse("day03/test.txt")
>>> solve1(pwds)
7
>>> solve2(pwds)
336
"""


import sys


def parse(fn):
    with open(fn, "rt") as f:
        return [x.strip() for x in f]


def count(data, xinc, yinc):
    x, y, c, m = 0, 0, 0, len(data[0])

    for line in data:
        if y % yinc == 0:
            if line[x] == '#':
                c += 1
            x = (x + xinc) % m
        y += 1

    return c


def solve1(data):
    return count(data, 3, 1)


def solve2(data):
    return count(data, 1, 1) * count(data, 3, 1) * count(data, 5, 1) * \
           count(data, 7, 1) * count(data, 1, 2)


if __name__ == '__main__':
    data = parse(sys.argv[1])
    print(solve1(data))
    print(solve2(data))
