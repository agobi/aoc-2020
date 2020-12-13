# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/11

>>> data = parse("day12/test.txt")
>>> solve(Ship(), data)
25
>>> solve(Ship2(), data)
286
"""

import sys, math
from collections import namedtuple

def parse(fn):
    ret = []
    with open(fn, "rt") as f:
        for l in f:
            ret.append((l[0], int(l[1:])))

    return ret  

# x: E-W, y: N-S, direction = 0: East
RAD = math.pi / 180.0

class Ship:
    def __init__(self):
        self._x, self._y, self._direction = 0, 0, 0

    def move(self, direction, units):
        if direction == 'F':
            self._x += math.cos(RAD * self._direction) * units
            self._y -= math.sin(RAD * self._direction) * units
        elif direction == 'N':
            self._y += units
        elif direction == 'S':
            self._y -= units
        elif direction == 'E':
            self._x += units
        elif direction == 'W':
            self._x -= units
        elif direction == 'R':
            self._direction += units
        elif direction == 'L':
            self._direction -= units

    def distance(self):
        return int(abs(self._x) + abs(self._y))

    def __str__(self):
        return "Ship(%f, %f, %f)" % (self._x, self._y, self._direction)


class Ship2:
    def __init__(self):
        self._x, self._y, self._wp_x, self._wp_y = 0, 0, 10, 1

    def rotate(self, units):
        self._wp_x, self._wp_y = (
            math.cos(RAD * units) * self._wp_x + math.sin(RAD * units) * self._wp_y,
            -math.sin(RAD * units) * self._wp_x + math.cos(RAD * units) * self._wp_y
        )

    def move(self, direction, units):
        if direction == 'F':
            self._x += self._wp_x * units
            self._y += self._wp_y * units
        elif direction == 'N':
            self._wp_y += units
        elif direction == 'S':
            self._wp_y -= units
        elif direction == 'E':
            self._wp_x += units
        elif direction == 'W':
            self._wp_x -= units
        elif direction == 'R':
            self.rotate(units)
        elif direction == 'L':
            self.rotate(-units)

    def distance(self):
        return int(abs(self._x) + abs(self._y))

    def __str__(self):
        return "Ship2(%f, %f, %f, %f)" % (self._x, self._y, self._wp_x, self._wp_y)


def solve(ship, directions):
    for (d, v) in directions:
        ship.move(d, v)
        # print(ship)
    return ship.distance()

if __name__ == '__main__':
    data = parse(sys.argv[1])
    print(solve(Ship(), data))
    print(solve(Ship2(), data))
