#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    a = []
    for i in range(10):
        a.append([]) #创建十行
        for j in range(10):
            a[i].append(0) #每行创建i列

    # 杨辉三角边界都为1
    for i in range(10):
        a[i][0] = 1
        a[i][i] = 1

    # 杨辉三角定义，下一行数值为上一行数与上一行前面数之和(除边界）
    for i in range(2,10):
        for j in range(1,i):
            a[i][j] = a[i - 1][j-1] + a[i - 1][j]

    from sys import stdout
    for i in range(10):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print