#!/usr/bin/python
# -*- coding: UTF-8 -*-
n = raw_input('Please enter the number of month!\n')
f1 = 1
f2 = 1
for i in range(1,int(n)):
    print '%12d' % (f2)
    f1 = f1 + f2
    f2 = f1 + f2