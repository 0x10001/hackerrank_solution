#!/usr/bin/python3
# encoding: utf-8

"""
   @author: Eric Wong
  @license: MIT Licence 
  @contact: ericwong@zju.edu.cn
     @file: main.py
     @time: 2016-06-10 13:53
"""

import sys

DEBUG = 0

if DEBUG:
    handler = open("./input")
else:
    handler = sys.stdin

cases = int(handler.readline())

MAX_N = 40
mem = {}


def count_bricks(n):
    if n in mem:
        return mem[n]

    if n < 4:
        return 1
    mem[n] = count_bricks(n - 1) + count_bricks(n - 4)
    return mem[n]


maximum = count_bricks(MAX_N)
prime_table = [0, 0, 1, 2, 2]
primes = [2, 3]
for i in range(5, maximum + 1):
    for p in primes:
        if p * p > i:
            prime_table.append(prime_table[-1] + 1)
            primes.append(i)
            break
        if i % p == 0:
            prime_table.append(prime_table[-1])
            break

for _ in range(cases):
    n = int(handler.readline())
    print(prime_table[count_bricks(n)])

handler.close()
