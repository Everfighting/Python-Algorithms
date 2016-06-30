#!/usr/bin/python
# -*- coding: UTF-8 -*-

from math import sqrt
from sys import stdout

h = 0
leap = 1
# 不是素数标记为0
for m in range(101,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    # 根据素数标记统计素数个数，并按照10个一组显示
    if leap == 1:
        print '%-4d' % m
        h += 1
        if h % 10 == 0:
            print ''
    leap = 1
print 'The total is %d' % h