#!/usr/bin/env python3
# encoding: utf-8

"""
   @author: Eric Wong
  @license: MIT Licence 
  @contact: ericwong@zju.edu.cn
     @file: main.py
     @time: 2016-06-08 12:42
"""

import sys
from functools import reduce

DEBUG = 1

if DEBUG:
    handler = open("./input")
else:
    handler = sys.stdin

cases = int(handler.readline())
MOD = 1000000007

for _ in range(cases):
    dimensions, steps = map(int, handler.readline().split())
    start = tuple(map(int, handler.readline().split()))
    limits = tuple(map(int, handler.readline().split()))

    buf = {limits: 1}
    '''
    grid = []
    num_grid = reduce(lambda x, y: x * y, limits, 1)
    for grid_id in range(num_grid):
        for limit in limits:
            grid.append(grid_id % limit + 1)
            grid_id //= limit
        buf[tuple(grid)] = 0
        grid.clear()
    '''

    grid = [1] * dimensions
    while tuple(grid) < limits:
        buf[tuple(grid)] = 1
        grid[0] += 1
        for d in range(dimensions):
            if grid[d] > limits[d]:
                grid[d] = 1
                grid[d + 1] += 1
            else:
                break


    def calc(g):
        ret = 0
        for d in range(dimensions):
            front_slice, end_slice = g[:d], g[d + 1:]
            upper = front_slice + (g[d] + 1,) + end_slice
            lower = front_slice + (g[d] - 1,) + end_slice
            if 1 < g[d]:
                ret += buf[lower]
            if g[d] < limits[d]:
                ret += buf[upper]
        return ret % MOD


    for move in range(steps):
        data = {}
        if move == steps - 1:
            print(calc(start))
            break

        for grid in buf:
            data[grid] = calc(grid)
        buf = data

handler.close()
