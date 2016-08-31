#-*- encoding: utf-8 -*-
'''
Created on 2016/8/29 0029
@author: dongange
题目：计算列表中最大的数字和第二大的数字
'''
ListTest = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]

for i in range(len(ListTest)):
    for j in range(i):
        if ListTest[j] > ListTest[i]:
            ListTest[j], ListTest[i] = ListTest[i], ListTest[j]

MaxNum = ListTest[len(ListTest)-1]
for i in range(len(ListTest))[::-1]:
    if ListTest[i] < MaxNum:
        SecondMaxNum = ListTest[i]
        break

print '最大的数字：%s, 第二大的数字：%s' % (MaxNum, SecondMaxNum)
