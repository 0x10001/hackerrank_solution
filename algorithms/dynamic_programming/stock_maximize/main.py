#!/usr/bin/env python3
# encoding: utf-8

"""
   @author: Eric Wong
  @license: MIT Licence 
  @contact: ericwong@zju.edu.cn
     @file: main_bak.py
     @time: 2016-06-07 23:12
"""

import sys

DEBUG = 0

if DEBUG:
    handler = open("./input")
else:
    handler = sys.stdin

cases = int(handler.readline())

for _ in range(cases):
    handler.readline()
    prices = list(map(int, handler.readline().split()))[::-1]
    peak = 0
    profit = 0
    for price in prices:
        if peak < price:
            peak = price
        else:
            profit += peak - price
    print(profit)

handler.close()
