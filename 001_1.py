#!/usr/bin/python
# -*- coding: UTF-8 -*-
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print 100*i+10*j+k
