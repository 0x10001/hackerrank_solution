#!/usr/bin/env python3
# encoding: utf-8

"""
   @author: Eric Wong
  @license: MIT Licence 
  @contact: ericwong@zju.edu.cn
     @file: main.py
     @time: 2016-06-09 18:40
"""

import sys

DEBUG = 0

if DEBUG:
    handler = open("./input")
else:
    handler = sys.stdin

cases = int(handler.readline())
MOD = 1000000007


def mirror(grid, upper_bound):
    ret = list(grid)
    for i in range(len(grid)):
        if ret[i] * 2 > upper_bound[i] + 1:
            ret[i] = upper_bound[i] + 1 - grid[i]
    return tuple(ret)


mem_1 = {}
mem_2 = {}
cache = {}


# 1 Compute the number of different ways in 0~M steps in each single dimension
# For each dimension (`d`), `pos` means `starting_point[d]` and `upper_bound` means `limits[d]`
def calc_single(pos, upper_bound, moves):
    if (pos, upper_bound, moves) in mem_1:
        return mem_1[pos, upper_bound, moves]
    if moves == 0:
        return 1

    ret = 0
    if pos > 1:
        tmp = pos - 1
        if tmp * 2 > upper_bound + 1:
            tmp = upper_bound + 1 - tmp
        ret += calc_single(tmp, upper_bound, moves - 1)
    if pos < upper_bound:
        tmp = pos + 1
        if tmp * 2 > upper_bound + 1:
            tmp = upper_bound + 1 - tmp
        ret += calc_single(tmp, upper_bound, moves - 1)
    mem_1[pos, upper_bound, moves] = ret % MOD
    return ret


# 2 In M steps, there may be k steps choosing the same dimension to form a legal walk
# here we count C(M, k) to calculate the number of ways choosing one dimension in M steps
def cmb(n, k):
    if k * 2 > n:
        k = n - k
    if k == 0:
        return 1
    if (n, k) in mem_2:
        return mem_2[n, k]

    mem_2[n, k] = (cmb(n - 1, k - 1) + cmb(n - 1, k)) % MOD
    return mem_2[n, k]


# 3 Now come to the final part.
# Denote the vector of starting point by `s`, the vector of upper bounds by `l`,
# the number of dimensions by `d` and the number of steps by `m`.
# Assume we have a function `f(s, l, d, m)` to compute the total number of different legal walks
# from `s` in a `d`-dimension space with upper bound `l` in `m` moves.
# Then we have
# `f(s, l, d, m) = sum(i from 0 to m)(single(s, l, d - 1, i) * cmb(m, i) * f(s, l, d - 1, m - i)`,
# which describes that each time we pick `i` from the `m` steps to move on `d`th dimension,
# the result in this case would be that of `m-i` steps from the previous `d-1` dimensions,
# multiplied by that of the moves on `d`th dimension.
# Well, don't forget the ways of picking `i` from the `m` steps (`cmb(m, i)`).
def calc_total(start, limits, steps):
    dimensions = len(start)
    if (dimensions, steps) in cache:
        return cache[dimensions, steps]
    if dimensions == 1:
        ret = calc_single(start[0], limits[0], steps) % MOD
        cache[dimensions, steps] = ret
        return ret

    ret = 0
    for s in range(steps + 1):
        single = calc_single(start[-1], limits[-1], s)
        combination = cmb(steps, s)
        ret += combination * single * calc_total(start[:-1], limits[:-1], steps - s)
        ret %= MOD
    cache[dimensions, steps] = ret
    return cache[dimensions, steps]

for _ in range(cases):
    dimensions, steps = map(int, handler.readline().split())
    start = tuple(map(int, handler.readline().split()))
    limits = tuple(map(int, handler.readline().split()))
    start = mirror(start, limits)

    print(calc_total(start, limits, steps))
    cache.clear()

handler.close()
