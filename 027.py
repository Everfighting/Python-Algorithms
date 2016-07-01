#!/usr/bin/python
# -*- coding: UTF-8 -*-

def output(s, l):
	if l == 0:
		return
	print (s[l - 1]),
	# 调用打印出最后一个输入的字符
	output(s, l - 1) #递归调用output函数

s = raw_input('Input a string:')
l = len(s)
output(s, l)