#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：输出斐波那契数列指定序号的值
"""
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

# 输出了第10个斐波那契数列
print(fib(10))
