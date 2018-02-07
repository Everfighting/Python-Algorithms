#!/usr/bin/env python3
# conding:utf-8


"""
有1、2、3、4个数字，
能组成多少个互不相同且无重复数字的三位数？
都是多少？
"""
# 法一:字符串连接
def gen_num_1():
    count = 0
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i != j and j != k and k != i:
                    print("".join(map(str, [i,j,k])))
                    count += 1
    print(count)

gen_num_1()


# 法二:列表推导
print(["".join(map(str, [x,y,z])) for x in range(1, 5) for y in range(1,5) for z in range(1, 5) if x != y and x != z and y != z])


# 法三:数值计算
def get_num_2():
    count = 0 
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i != j and j != k and k != i:
                    print(i*100+j*10+k)
                    count += 1
    print(count)
get_num_2()
