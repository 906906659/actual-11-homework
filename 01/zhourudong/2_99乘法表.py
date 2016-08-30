#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 4   9 9 乘法表
for i in range(1,10):
	for j in range(1,10):
		if j <= i:
			print "%s x %s = %s" % (i,j,i*j), 
	print '\n'
