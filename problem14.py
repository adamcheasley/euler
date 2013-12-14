#!/usr/bin/python
# -*- coding: utf-8 -*-

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Which starting number, under one million, produces the longest chain?


def step(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1

n = 13
while n > 1:
    print n
    n = step(n)

print 1
