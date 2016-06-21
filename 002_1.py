#!/usr/bin/python
# -*- coding: UTF-8 -*-
i = int(raw_input('input gain:\n'))
if i <= 100000:
    bonus = i * 0.1
    print 'bonus = ',bonus
elif i <= 200000:
    bonus = 10000 + (i - 100000) * 0.075
    print 'bonus = ',bonus
elif i <= 400000:
    bonus= 17500 + (i - 200000) * 0.05
    print 'bonus = ',bonus
elif i <= 600000:
    bonus= 27500 + (i - 400000) * 0.03
    print 'bonus = ',bonus
elif i <= 1000000:
    bonus = 33500 + (i - 600000) * 0.015
    print 'bonus = ',bonus
else:
    bonus = 39500 +(i - 1000000) * 0.01
    print 'bonus = ',bonus