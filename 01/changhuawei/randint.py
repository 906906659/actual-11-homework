#encoding:utf-8

import random

nums1 = random.randint(0, 100)
while True:
    pass
    nums2 = int(raw_input('please input num:'))
    if nums1 == nums2:
        print '输入匹配正确'
        break
    else:
        print '输入不匹配再接再厉'
print  'done'
