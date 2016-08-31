#-*- encoding: utf-8 -*-
'''
Created on 2016/8/30 0030
@author: dongange
题目：打印乘法口诀表
'''
for i in range(10):
    for j in range(i):
        Num = int(i) * int(j+1)
        print '%s*%s=%s  ' % (j+1, i, Num),
    print '\n'
