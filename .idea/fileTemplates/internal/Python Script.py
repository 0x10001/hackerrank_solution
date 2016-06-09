#!/usr/bin/env python3
# encoding: utf-8

"""
   @author: Eric Wong
  @license: MIT Licence 
  @contact: ericwong@zju.edu.cn
     @file: ${NAME}.py
     @time: ${YEAR}-${MONTH}-${DAY} ${HOUR}-${MINUTE}
"""

import sys

DEBUG = 1

if DEBUG:
    handler = open("./input")
    cases = int(handler.readline())
else:
    handler = sys.stdin
    cases = 1


handler.close()