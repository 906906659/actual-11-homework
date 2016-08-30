#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 4   9 9 乘法表
for i in range(1,10):
	for j in range(1,10):
		if j <= i:
			print "%s x %s = %s" % (i,j,i*j), 
	print '\n'


# while 循环
i  = 1 

while i<10:
    j=1
    while j<=i:
        print "%s x %s = %s" % (i,j,i*j),
        j += 1
    i += 1
    print '\n'
    
