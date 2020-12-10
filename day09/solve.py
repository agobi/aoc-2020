# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/9

>>> input = parse("day09/test.txt")
>>> solve1(input, 5)
127
>>> solve2(input, 5)
62
"""

from collections import OrderedDict, deque
import itertools
import sys


def parse(fn):
    with open(fn, "rt") as f:
        return [int(i) for i in f]


def solve(data, depth):
    cache = OrderedDict()
    elems = []
    for x in data:
        if len(cache) < depth:
            cache[x] = 0
            elems.append(x)
        else:
            for y in cache:
                z = x - y
                if z != y and z in cache:
                    break
            if z != y and z in cache:
                cache.popitem(False)
                cache[x] = 0
                elems.append(x)
            else:
                return x, elems


def lookup(x, elems):
    data = deque(elems)
    while data:
        sum = 0
        for y_idx in range(len(data)):
            y = data[y_idx]
            sum += y
            if sum == x:
                return list(itertools.islice(data, 0, y_idx+1))
            elif sum > x:
                break
        data.popleft()


def solve1(data, depth):
    x, _ = solve(data, depth)
    return x


def solve2(data, depth):
    x, elems = solve(data, depth)
    sum_elems = lookup(x, elems)
    return min(sum_elems) + max(sum_elems)


if __name__ == "__main__":
    data = parse(sys.argv[1])
    depth = int(sys.argv[2])
    print(solve1(data, depth))
    print(solve2(data, depth))
