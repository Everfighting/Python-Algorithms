#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 创建字典
i = ['a', 'b']
l = [1, 2]

# 观察两者的差别，注意zip的用法
print dict([i,l])
print dict(zip(i,l))


