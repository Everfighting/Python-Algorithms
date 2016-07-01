#!/usr/bin/python
# -*- coding: UTF-8 -*-

x2 = 1
for day in range(9,0,-1):
# for day in range(0,9,1):本质上一样，控制倒推的次数。
    x1 = (x2 + 1) * 2
    x2 = x1
print x1