#!/usr/bin/env python3
# encoding: utf-8

"""
   @author: Eric Wong
  @license: MIT Licence
  @contact: ericwong@zju.edu.cn
     @file: the_coin_change_problem.py
     @time: 2016-06-07 22:23
"""

import sys

DEBUG = 0

if DEBUG:
    handler = open("./input")
    cases = int(handler.readline())
else:
    handler = sys.stdin
    cases = 1

mem = {}


def calc(target, coins):
    if (target, coins) in mem:
        return mem[target, coins]

    if target == 0:
        return 1
    if target < 0 or len(coins) == 0:
        return 0

    coin_tuple = ()
    cnt = 0
    for coin in coins:
        coin_tuple += (coin,)
        tmp = calc(target - coin, coin_tuple)
        if target - coin > 0:
            mem[target - coin, coin_tuple] = tmp
        cnt += tmp

    return cnt


for _ in range(cases):
    n = next(map(int, handler.readline().split()))
    coin_collection = sorted(list(map(int, handler.readline().split())))
    print(calc(n, tuple(coin_collection)))

handler.close()
