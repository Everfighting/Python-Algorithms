#!/usr/bin/python
# -*- coding: UTF-8 -*-
# join 和 split方法的使用,join用来连接字符串，split恰好相反，拆分字符串的。
L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print s1

s2 = ' '.join('12345')
print s2

s3 = '*'.join(['1','2','3','4','5'])
print s3

s4 = s3.split('*')
print s4
s5 = s2.split(" ")
print s5
s6 = s1.split(",", 0)
print s6
s7 = s1.split(",", 1)
print s7
s8 = s1.split(",", -1)
print s8
