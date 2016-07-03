#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        for j in range(3):
            a.append(float(raw_input("input num:\n")))

    for i in range(3):
            sum += a[3*i+i]
    #比原来的解法更加容易理解！

    print sum

