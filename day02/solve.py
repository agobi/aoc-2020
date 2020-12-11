# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/2

>>> pwds = parse("day02/test.txt")
>>> solve1(pwds)
2
>>> solve2(pwds)
1
"""

import re, sys


parse_re = re.compile(r'(\d+)-(\d+) (\w): (.*)')
def parse(fn):
    with open(fn, "rt") as f:
        ret = []
        for l in f:
            m = parse_re.fullmatch(l.strip())
            ret.append((int(m.group(1)), int(m.group(2)), m.group(3)[0], m.group(4)))
        return ret
    


def solve1(data):
    ret = 0
    for (min, max, chr, pwd) in data:
        cnt = pwd.count(chr)
        if cnt >= min and cnt <= max:
            ret += 1
    return ret


def solve2(data):
    ret = 0
    for (min, max, chr, pwd) in data:
        if (pwd[min-1] == chr) != (pwd[max-1] == chr):
            ret += 1
           
    return ret


if __name__ == '__main__':
    pwds = parse(sys.argv[1])
    print(solve1(pwds))
    print(solve2(pwds))