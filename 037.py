#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
    # get the number of the number
    N = int(raw_input("Please input the number of the number:\n"))
    print 'begin>>>>>>>>>'
    l = []
    for i in range(N):
        l.append(int(raw_input('input a number:\n')))
    print 'end>>>>>>>>>'
    print 'the original numbers are:'
    for i in range(N):
        print l[i],
    print ">>>>>>>>"

    # sort num
    for i in range(N - 1):
        min = i
        for j in range(i + 1,N):
            if l[min] > l[j]:min = j
        l[i],l[min] = l[min],l[i]
    print 'after sorted>>>>>>'
    for i in range(N):
        print l[i],