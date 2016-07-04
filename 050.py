#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

# 用于生成一个0到1的随机符点数: 0 <= n < 1.0
print random.random()

#生成 10 到 20 之间的随机数
print random.uniform(10, 20)

# 用于生成一个10到50之间的随机整数。
print random.randint(10,50)

# 从序列中获取一个随机元素。
print random.choice([1,2,3,4,5,6,7,8])

# 用于将一个列表中的元素打乱。
p=['This','is','python']
random.shuffle(p)
print p

# 从指定序列中随机获取指定长度的片断。
print random.sample([1,2,3,4,5,6,7,8],3)

# 从指定范围内,按指定基数递增的集合中获取一个随机数r
print random.randrange(10,100,2)



