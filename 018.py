#!/usr/bin/python
# -*- coding: UTF-8 -*-

Tn = 0
Sn = []
n = int(raw_input('n = \n'))
a = int(raw_input('a = \n'))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn

Sn = reduce(lambda x,y : x + y,Sn)
print Sn

# reduce 方法将Sn列表中的数据逐个累加使用lambda函数。
# map 逐个应用fn函数，但是不累加。
# filter 对sequence中的元素进行过滤，返回符合条件的元素。
