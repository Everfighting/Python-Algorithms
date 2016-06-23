#!/usr/bin/python
# -*- coding: UTF-8 -*-

year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

#将之前月份和当月天数，分开计算，减少不必要的if...else的判断。
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print 'data error'
sum += day
#使用leap来标记是否是闰年
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
#对是闰年且月份大约2月的天数增加一天
if (leap == 1) and (month > 2):
    sum += 1
print 'it is the %dth day.' % sum

#与002题思路较相似，利用数组来表示每个月对应的天数，通过月份与当月天数的分离，使得计算更为清晰。
#判断闰年中使用了leap作为标志符，与C语言中的flag用法较为相似