# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/78

>>> input = parse("day08/test.txt")
>>> solve1(input)
5
>>> solve2(input)
8
"""

import sys


def parse(fn):
    with open(fn, "r") as f:
        code = []
        for l in f:
            q = l.strip().split(" ")
            code.append((q[0], int(q[1])))
    return code


def run(code, ip=0, ips=None, acc=0, e_ip=-1, e_code=None):
    ips = ips or set()

    while ip not in ips:
        if ip == len(code):
            return acc, e_ip, e_code
        elif ip > len(code) or ip < 0:
            return None

        opcode, arg = code[ip]
        if e_ip == ip:
            opcode = e_code

        if opcode == "nop":
            if e_ip is None:
                ret = run(code, ip, ips.copy(), acc, e_ip=ip, e_code="jmp")
                if ret:
                    return ret
            ips.add(ip)
            ip += 1
        elif opcode == "acc":
            acc += arg
            ips.add(ip)
            ip += 1
        elif opcode == "jmp":
            if e_ip is None:
                ret = run(code, ip, ips.copy(), acc, e_ip=ip, e_code="nop")
                if ret:
                    return ret
            ips.add(ip)
            ip += arg
            
    if e_ip == -1:
        return acc
    else:
        return None


def solve1(code):
    return run(code)


def solve2(code):
    return run(code, e_ip = None)[0]


if __name__ == "__main__":
    code = parse(sys.argv[1])
    print("part1 %d" % solve1(code))
    print("part2 %d (changed line %d to %s)" % solve2(code))
