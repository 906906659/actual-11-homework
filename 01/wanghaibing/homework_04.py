#!/usr/bin/env pythyon
#9*9 multiplication table
for i in range(1,10):
    for j in range(1,i+1):
        pro=j*i
        print '%s*%s=%s' % (j,i,pro) ,
    print "\n"
