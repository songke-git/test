#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 18:48
# @Author  : sk
# @Site    : 
# @File    : 算法训练：密码传纸条.py
# @Software: PyCharm

a = [["A", "B", "C", "D", "E", "F", "G", "H", "I"],["J", "K", "L", "M", "N", "O", "P", "Q", "R"],["S", "T", "U", "V", "W", "X", "Y", "Z", "*"]]

input1 = input(':::::::').split(' ')
input2 = input('______')

m = (int(input1[0]) - 1)%3
n = (int(input1[1]) - 1)%9
result = []
a = a[m:] + a[:m]
a[0],a[1],a[2] = a[0][n:] + a[0][:n],a[1][n:] + a[1][:n],a[2][n:] + a[2][:n]
for x in input2:
    for i in range(1,4):
        if x in a[i-1]:
            for j in range(1,10):
                if x == a[i-1][j-1]:
                    result.append(str(i) + str(j))
print(' '.join(result))






