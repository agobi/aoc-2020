# Day 1

https://adventofcode.com/2020/day/1

## Extra solution in Whitespace

sol1.ws and sol2.ws are the solutions for the problem, written in
[Whitespace](https://esolangs.org/wiki/Whitespace).

Whitespace has no IO error handling, so you must put a `-1` at the end of each file and redirect it to
the program's standard input.

Or, if you have some shell:
```shell
$ (cat test.txt; echo -1) | wspace sol1.ws
```

I've written an [assembler / disassembler for Whitespace](https://github.com/agobi/whitespace-nd).