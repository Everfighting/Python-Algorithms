#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = raw_input("请输入一个数字:\n")
flag = True

for i in range(len(x)/2):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print "%s 是一个回文数!" % x
else:
    print "%s 不是一个回文数!" % x