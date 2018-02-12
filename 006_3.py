#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""题目：输出斐波那契数列指定序号的值"""
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

# 输出前 10 个斐波那契数列
print fib(10)[9]
