#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = ['one', 'two', 'three']
for i in a[::-1]:
	print i

for m in range(0,10,2):
	print m


# for n in range(0,10,-2):
# 		print n
# 错误之处：[::-1]可以完全倒置列表，但是range（0,10，-2）不可以。

for m in range(10,0,-2):
	print m




