#encoding: utf-8

print '*'*60
print '\n'

for i in range(1,10):
    for j in range(1,i+1):
        print '%s*%s=%s'%(j,i,j*i),
    print '\n'
print '\n'
print '*'*60