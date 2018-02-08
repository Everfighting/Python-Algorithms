#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
"""
import math
# 根据描述可以判断该数不会超过10000
for i in range(10000):
    #math.sqrt开平方
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print(i)
