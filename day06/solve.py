# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/6

>>> input = parse("day06/test.txt")
>>> solve1(input)
11
>>> solve2(input)
6
"""


import sys
import operator
from functools import reduce


def parse(fn):
    ret, current = [], []
    with open(fn, "rt") as f:
        for line in f:
            line = line.strip()

            if line:
                current.append(line)
            else:
                ret.append(current)
                current = []
        ret.append(current)
        return ret


def solve1(data):
    return sum(len(set(x for c in g for x in c)) for g in data)


def solve2(data):
    return sum(
        len(reduce(operator.and_, [set(x for x in c) for c in g]))
        for g in data
    )


if __name__ == '__main__':
    data = parse(sys.argv[1])
    print(solve1(data))
    print(solve2(data))
