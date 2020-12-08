# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/7

>>> input = parse("day07/test.txt")
>>> solve1(input)
4
>>> solve2(input)
32
"""

import sys
from collections import defaultdict

import pyparsing as pp
from pyparsing import pyparsing_common as ppc


def parse(fn):
    with open(fn, "r") as f:
        return parse_input(f)


def parse_input(f):
    color = (ppc.identifier + ppc.identifier).setParseAction(
                lambda s, l, t: t[0] + "_" + t[1]
            )
    bag = pp.oneOf(["bags", "bag"])
    colored_bag = (color + bag).setParseAction(lambda s, l, t: t[0])
    numbered_bag = (ppc.integer + colored_bag).setParseAction(
                lambda s, l, t: (t[0], t[1])
            )
    bags = pp.Literal("no other bags").setParseAction(lambda s, l, t: set()) |\
        pp.delimitedList(numbered_bag, ",").setParseAction(
            lambda s, l, t: set(t)
        )

    line_parser = (
        colored_bag + "contain" + bags + "." + pp.LineEnd()
    ).setParseAction(lambda s, l, t: (t[0], t[2]))

    try:
        r = pp.OneOrMore(line_parser).parseFile(f)
        return r
    except pp.ParseSyntaxException as e:
        print(e)


def transpose(x):
    ret = defaultdict(list)
    for k, v in x:
        for vv in v:
            ret[vv[1]].append(k)
    return ret


def traverse(x):
    queue = ['shiny_gold']
    found = set(queue)

    while queue:
        next = queue.pop()
        for i in x[next]:
            if i not in found:
                queue.append(i)
                found.add(i)

    return found


def traverse_count(tree):
    cache = {}

    def count(x):
        count = 1
        for mul, color in tree[x]:
            count += mul * cached_count(color)
        return count

    def cached_count(x):
        if x not in cache:
            cache[x] = count(x)
        return cache[x]

    return cached_count('shiny_gold')


def solve1(input):
    return len(traverse(transpose(input))) - 1


def solve2(input):
    return traverse_count(dict(input.asList()))-1


if __name__ == "__main__":
    input = parse(sys.argv[1])
    print(solve1(input))
    print(solve2(input))
