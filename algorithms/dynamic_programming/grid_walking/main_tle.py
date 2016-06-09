#!/usr/bin/env python3
# encoding: utf-8

"""
   @author: Eric Wong
  @license: MIT Licence 
  @contact: ericwong@zju.edu.cn
     @file: main.py
     @time: 2016-06-09 16:33
"""

import sys

DEBUG = 0

if DEBUG:
    handler = open("./input")
else:
    handler = sys.stdin

"""
This is a TLE version to solve the Grid Walking problem.
It just simply does additions from top to bottom, which takes much more time than
I could imagine. The last test case provided in the file "input" tells that.
"""

cases = int(handler.readline())
MOD = 1000000007

mem = {}


def mirror(grid, upper_bound):
    ret = list(grid)
    for i in range(len(grid)):
        if ret[i] * 2 > upper_bound[i] + 1:
            ret[i] = upper_bound[i] + 1 - grid[i]
    return tuple(ret)


def calc(grid, moves, upper_bound):
    if moves == 0:
        return 1

    grid = mirror(grid, upper_bound)
    if (moves, grid) in mem:
        return mem[moves, grid]

    ret = 0
    for i in range(len(grid)):
        front_slice, end_slice = grid[:i], grid[i + 1:]
        if 1 < grid[i]:
            ret += calc(front_slice + (grid[i] - 1,) + end_slice,
                        moves - 1, upper_bound)
        if grid[i] < upper_bound[i]:
            ret += calc(front_slice + (grid[i] + 1,) + end_slice,
                        moves - 1, upper_bound)

    ret %= MOD
    mem[moves, grid] = ret
    return ret


for _ in range(cases):
    dimensions, steps = map(int, handler.readline().split())
    start = tuple(map(int, handler.readline().split()))
    limits = tuple(map(int, handler.readline().split()))
    print(calc(start, steps, limits))
    mem.clear()

handler.close()
