#encoding:utf-8

numlist = [1,2,3,4,5,6,7,8,9]
for i in range(1,10):
    x = ''
    # print i
    for j in range(1,i+1):
        # print j
        x = x + str(j) + '*'  + str(i) + '=' + str(i * j) +' '
    print x



for x in range(1,10):
    for y in range(1,x + 1):
        # z = x * y
        print '%s * %s = %s' %(x,y,x*y)
    print '\n'

