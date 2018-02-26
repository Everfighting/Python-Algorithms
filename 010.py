#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import time

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# time.strftime将时间转成需要的格式
