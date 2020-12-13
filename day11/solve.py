# Copyright (c) 2020 Attila Gobi
# SPDX-License-Identifier: BSD-3-Clause

"""
Solution for https://adventofcode.com/2020/day/11

>>> data = parse("day11/test.txt")
>>> State(data).solve()
37
>>> State2(data).solve()
26
"""

import sys


def parse(fn):
    with open(fn, "rt") as f:
        return [s.strip() for s in f]


class State:
    def __init__(self, state):
        self._state = [[x for x in line] for line in state]
        self._n, self._m = len(state), len(state[0])

    def adjacent_rule(self, x, y):
        count = 0
        for xx in range(x - 1, x + 2):
            for yy in range(y - 1, y + 2):
                if (xx == x and yy == y) or \
                  xx < 0 or xx >= self._n or yy < 0 or yy >= self._m:
                    continue
                if self._state[xx][yy] == '#':
                    count += 1

        if count >= 4:
            return 1
        elif count == 0:
            return -1
        else:
            return 0

    def new_seat_state(self, x, y):
        s = self._state[x][y]
        if s == '#':
            return 'L' if self.adjacent_rule(x, y) > 0 else '#'
        elif s == 'L':
            return '#' if self.adjacent_rule(x, y) < 0 else 'L'
        else:
            return s

    def new_state(self):
        self._state = [
            "".join(self.new_seat_state(x, y) for y in range(self._m))
            for x in range(self._n)
        ]

    def state(self):
        return self._state

    def print_state(self):
        for line in self._state:
            print(line)
        print

    def solve(self):
        # self.print_state(self._state)
        old_state = self._state
        self.new_state()
        # self.print_state(self._state)
        while self._state != old_state:
            old_state = self._state
            self.new_state()
            # self.print_state(self._state)

        return sum(line.count('#') for line in self._state)


class State2(State):
    def adjacent_rule(self, x, y):
        count = 0
        for xd in [-1, 0, 1]:
            for yd in [-1, 0, 1]:
                if (xd == 0 and yd == 0):
                    continue
                xx, yy = x + xd, y + yd
                while xx >= 0 and xx < self._n and yy >= 0 and yy < self._m:
                    if self._state[xx][yy] == '#':
                        count += 1
                        break
                    if self._state[xx][yy] == 'L':
                        break
                    xx += xd
                    yy += yd

        if count >= 5:
            return 1
        elif count == 0:
            return -1
        else:
            return 0


if __name__ == '__main__':
    data = parse(sys.argv[1])
    print(State(data).solve())
    print(State2(data).solve())
