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

DEBUG = 1

if DEBUG:
    handler = open("./input")
else:
    handler = sys.stdin

cases = int(handler.readline())
MOD = 1000000007

for _ in range(cases):
    dimensions, steps = map(int, handler.readline().split())
    start = list(map(int, handler.readline().split()))
    limits = list(map(int, handler.readline().split()))

    print(limits)
