#!/usr/bin/python

#homeowrk_one:
num1 = [1,23,99,45,100,3,65536,4000,5000]
max1=num1[0]
max2=num1[0]
for i in num1:
    if i > max1:
        max1=i
print max1
for i in num1:
    if i > max2 and i < max1:
        max2=i
print max2

#homework_two
for i in range(1,10):
    for j in range(1,10):
        ji=i * j
        print '%s * %s = %s' % (i,j,ji)
