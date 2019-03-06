#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 20:41
# @Author  : sk
# @Site    : 
# @File    : 面试算法题：输入金额.py
# @Software: PyCharm
n = int(input('输入上限：'))
m = input('输入单价：')
m = '999 1'.split(' ')
m.sort(key=lambda x:int(x) if x else 0)
for i in m:
    if not i:
        continue
    if n >= int(i):
        n -= int(i)
    else:
        break
print(1000 - n)