#!/usr/bin/python3
# encoding: utf-8

"""
   @author: Eric Wong
  @license: MIT Licence 
  @contact: ericwong@zju.edu.cn
     @file: main.py
     @time: 2016-06-07 23:44
"""

import sys

DEBUG = 0

if DEBUG:
    handler = open("./input")
else:
    handler = sys.stdin

n = int(handler.readline())
ranking = []

for _ in range(n):
    ranking.append(int(handler.readline()))

candies = [1]
for i in range(1, n):
    if ranking[i] > ranking[i - 1]:
        val = candies[-1] + 1
    else:
        val = 1
    candies.append(val)

for i in range(n - 2, -1, -1):
    if ranking[i] > ranking[i + 1]:
        val = candies[i + 1] + 1
    else:
        val = 1
    candies[i] = max(candies[i], val)

print(sum(candies))

handler.close()
