# Day 1

https://adventofcode.com/2020/day/1

## Extra solution in Whitespace

[sol_a1.ws](sol_a1.ws) and [sol_a2.ws](sol_a2.ws) are the solutions for the problem, written in
[Whitespace](https://esolangs.org/wiki/Whitespace).

Whitespace has no IO error handling, so you must put a `-1` at the end of each file and redirect it to
the program's standard input.

Or, if you have some shell:
```shell
$ (cat test.txt; echo -1) | wspace sol1.ws
```

I've also written an [assembler / disassembler for Whitespace](https://github.com/agobi/whitespace-nd),
and included the assembly: [sol_a1.wss](sol_a1.wss), [sol_a2.wss](sol_a2.wss).

This Whitespace implementation has a couple of extensions to the original language:
 - pushe to push the last IO status to the stack
 - ref i which copies the i-th element of the stack to the top of the stack

I think adding -1 at the end of the file is a bit of cheating, so I have a revised version using the error handling:
 - part1: [source](sol_b1.wss), [whitespace](sol_b1.ws)
 - part2: [source](sol_b2.wss), [whitespace](sol_b2.ws)

