# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/4

>>> passports = parse("day04/test.txt")
>>> solve1(passports)
2
>>> solve2(passports)
2
"""


import sys
import re


def parse(fn):
    ret = []
    current = {}
    with open(fn, "rt") as f:
        for line in f:
            line = line.strip()

            if line == "":
                ret.append(current)
                current = {}
            else:
                for k, v in [x.split(":") for x in line.split(" ")]:
                    current[k] = v

    ret.append(current)
    return ret


def solve1(data):
    fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    count = 0

    for passport in data:
        if not fields - set(passport.keys()):
            count += 1

    return count


def solve2(data):
    pid_re = re.compile(r'\d{9}')
    hcl_re = re.compile(r'#[0-9a-f]{6}')
    ecl_set = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

    def valid_hgt(x):
        try:
            int_x = int(x[:-2])
            if x.endswith("in"):
                return int_x >= 59 and int_x <= 76
            elif x.endswith("cm"):
                return int_x >= 150 and int_x <= 193
        except ValueError:
            pass
        return False

    fields = {
        "byr": lambda x: int(x) >= 1920 and int(x) <= 2002,
        "iyr": lambda x: int(x) >= 2010 and int(x) <= 2020,
        "eyr": lambda x: int(x) >= 2020 and int(x) <= 2030,
        "hgt": valid_hgt,
        "hcl": lambda x: hcl_re.fullmatch(x),
        "ecl": lambda x: x in ecl_set,
        "pid": lambda x: pid_re.fullmatch(x)
    }

    def validate(x):
        for k, v in fields.items():
            if k not in passport or not v(passport[k]):
                # print("ERROR:", k, passport)
                return False
        return True

    count = 0

    for passport in data:
        if validate(passport):
            count += 1

    return count


if __name__ == '__main__':
    data = parse(sys.argv[1])
    print(solve1(data))
    print(solve2(data))
