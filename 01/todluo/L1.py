#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import sys
count = 0
while True:
print u'选择你要暂停的行：'
print_num = input('')
while count < 500:
if print_num == count: #判断输入的行数与当前行数是否相等 
   print u'你要暂停的行为 ',print_num
   print u'是否要继续(y|n)',
   choie = raw_input('')
   if choie == 'n':
      sys.exit()
   else:
      break
if print_num < count:#判断输入的行数是否小于当前行数 
           print u'已经过去了'
   break
else:
   count+=1
   print '现在是第%d行 ' % count