#!/usr/bin/python
# -*- coding: UTF-8 -*-

Sn = 100.0
Hn = Sn

for n in range(2,11):
    Hn /= 2
    # 单程距离为原高度的1/2
    Sn += 2 * Hn
    # 弹跳往返一次距离为2Hn

print 'Total of road is %f' % Sn
print 'The tenth is %f meter' % Hn