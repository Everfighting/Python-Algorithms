#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 使用递归
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

# 输出了第10个斐波那契数列
print fib(10)