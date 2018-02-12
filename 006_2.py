#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
"""题目：输出斐波那契数列指定序号的值"""
fib = lambda n: 1 if n == 1 else 1 if n == 2 else fib(n-2)+fib(n-1)

print(fib(10))
