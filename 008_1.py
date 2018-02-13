#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""九九乘法表打印"""
for i in range(1, 10):
    print
    for j in range(1, i+1):
        print("%d*%d=%d" % (i, j, i*j),)
