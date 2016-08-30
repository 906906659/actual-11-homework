#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
random_num = random.randint(0, 100)
user_input = int(raw_input('please input a number:'))

while user_input != random_num:
    print 'Error,try again:',
    user_input = int(raw_input())
print 'Good!数字为:%s,你猜对了,但是没有奖励' % (user_input)