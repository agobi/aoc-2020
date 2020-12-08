# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/1


>>> numbers = parse("day01/test.txt")
>>> solve1(numbers)
514579
>>> solve2(numbers)
241861950
"""

import sys


def parse(fn):
    with open(fn, "r") as f:
        return {int(i) for i in f.readlines()}


def solve1(numbers):
    for i in numbers:
        if (2020 - i) in numbers:
            return i * (2020 - i)


def solve2(numbers):
    for i in numbers:
        for j in numbers:
            if (2020 - i - j) in numbers:
                return i * j * (2020 - i - j)


if __name__ == '__main__':
    numbers = parse(sys.argv[1])
    print(solve1(numbers))
    print(solve2(numbers))
