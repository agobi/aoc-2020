# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/14

>>> solve1(parse("day14/test1.txt"))
165
>>> solve2(parse("day14/test2.txt"))
208
"""


import sys
import re


def readmask(mask):
    and_mask, or_mask = 0, 0

    for c in mask:
        and_mask *= 2
        or_mask *= 2

        if c == '0':
            pass
        elif c == '1':
            and_mask += 1
            or_mask += 1
        elif c == 'X':
            and_mask += 1
        else:
            raise ValueError("Unknown bit %s" % c)

    return and_mask, or_mask


mem_re = re.compile(r'mem\[(\d+)\] = (\d+)')
mask_re = re.compile(r'mask = ([01X]+)')


def parse(fn):
    with open(fn, "rt") as f:
        ops = []

        for line in f:
            g = mem_re.fullmatch(line.strip())
            if g:
                op = ("=", int(g.group(1)), int(g.group(2)))
            else:
                g = mask_re.fullmatch(line.strip())
                if g:
                    op = ("mask", g.group(1))

            if not op:
                raise ValueError("Cannot parse: `%s'" % line)

            ops.append(op)

        return ops


def solve1(ops):
    mem = {}
    for op in ops:
        if op[0] == "mask":
            and_mask, or_mask = readmask(op[1])
        elif op[0] == '=':
            # print(np.dtype(arg2), np.dtype(and_mask), np.dtype(or_mask))
            mem[op[1]] = op[2] & and_mask | or_mask
        else:
            raise ValueError("???")

    return sum(mem.values())


def readmask2(mask):
    flip_mask, or_mask = [], 0

    for c in mask:
        flip_mask = [x << 1 for x in flip_mask]
        or_mask <<= 1

        if c == '0':
            pass
        elif c == '1':
            or_mask += 1
        elif c == 'X':
            flip_mask.append(1)
        else:
            raise ValueError("Unknown bit %s" % c)

    return flip_mask, or_mask


def mems(value, flips):
    values = [value]
    for flip in flips:
        values = [x & ~flip for x in values] + [x | flip for x in values]
    return values


def solve2(ops):
    mem = {}
    for op in ops:
        if op[0] == "mask":
            flip_mask, or_mask = readmask2(op[1])
        elif op[0] == '=':
            # print(np.dtype(arg2), np.dtype(and_mask), np.dtype(or_mask))
            for addr in mems(op[1] | or_mask, flip_mask):
                mem[addr] = op[2]
        else:
            raise ValueError("???")

    return sum(mem.values())


if __name__ == '__main__':
    x = parse(sys.argv[1])
    print(solve1(x))
    print(solve2(x))
