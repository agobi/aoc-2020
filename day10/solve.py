# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/10

>>> input = parse("day10/test2.txt")
>>> solve1(input)
220
>>> solve2(input)
19208
"""


import sys


def parse(fn):
    with open(fn, "rt") as f:
        return sorted(int(x) for x in f)


def solve1(s):
    last = 0
    dist = [0, 0, 0, 1]
    for x in s:
        dist[x - last] += 1
        last = x
    return dist[1] * dist[3]


def solve2(s):
    m = max(s)
    solution = [0] * (m + 1)
    solution[0] = 1

    for x in s:
        solution[x] = solution[x - 1] + solution[x - 2] + solution[x - 3]

    return solution[m]


if __name__ == '__main__':
    data = parse(sys.argv[1])
    print(solve1(data))
    print(solve2(data))
