#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
列表的顺序是升序排列的，不断从中间取数进行判断。
"""
def binary_search(list, item):
    low = 0 
    high = len(list) - 1

    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

