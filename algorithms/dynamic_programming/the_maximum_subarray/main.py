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
    cont_sum = 0
    non_cont_sum = 0
    cont_sum_tmp = 0
    maximum = None

    for elm in map(int, handler.readline().split()):

        if maximum is None or maximum < elm:
            maximum = elm

        if elm >= 0:
            non_cont_sum += elm

        cont_sum_tmp += elm
        if cont_sum_tmp < 0:
            cont_sum_tmp = 0
        if cont_sum_tmp > cont_sum:
            cont_sum = cont_sum_tmp

    if maximum < 0:
        cont_sum = maximum
        non_cont_sum = maximum

    print(cont_sum, non_cont_sum)

handler.close()
