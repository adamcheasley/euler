#!/usr/bin/python
# -*- coding: utf-8 -*-


def step(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1

x = 0
start_number = 0
for i in range(500000, 999999):
    term_count = 1
    n = i
    while n > 1:
        n = step(n)
        term_count += 1
    if term_count > x:
        x = term_count
        start_number = i

print 'start number: %d' % start_number
