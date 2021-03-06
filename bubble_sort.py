#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 算法描述
# 它重复地走访过要排序的数列，依次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

# 代码描述：
def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i],lists[j] = lists[j],lists[i]
            return lists
