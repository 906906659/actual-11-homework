#encoding:utf-8
#Time:2016-08-29
#Author:宋亚龙
#Name:homework01

'''作业
1. 整理课堂内容 FreeMind/xmind
2. github => 发给我
    https://github.com/51reboot/actual-11-homework

3. 计算[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45] 最大的两个数字(两个数字不能重复)

4. 打印乘法口诀

5. 猜数字游戏
    系统生成一个随机的数字
    import random
    random.randint(0, 100)
    '''
'''计算列表中最大的两个数字'''
# num01 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
# for i in range(len(num01)-1,-1,-1):
#     for j in range(i):
#         if num01[j] > num01[j+1]:
#             num01[j],num01[j+1] = num01[j+1],num01[j]
# print '排序后的列表num01为：%s ' % num01
# max_num=num01.pop() #删除最后的一个大值并把返回值赋给变量
# while True:#如果列表里的最后一个最大值等于max_num的话则继续删除尾部元素，如果不等于的话，就把最后一个赋给secondMax_num
#     if num01[-1] == max_num:
#         num01.pop()
#     else:
#         secondMax_num = num01[-1]
#         break
# print '最大数为：%s；第二大的数为：%s；' % (max_num,secondMax_num)

'''乘法口诀'''
# for i in range(1, 10):
#     for j in range(1,i+1):
#         sum01 = i * j
#         print '%s X %s = %s' % (j,i,sum01)

'''随机数'''
# import random
# while True:
#     random01 = random.randint(0, 3)
#     num02 = int(raw_input('请输入你心中0-100的数字: '))
#     if num02==random01:
#         print '恭喜你猜对了，猜中的数字为：%s;' % (num02)
#         break
#     if num02 >100:
#         print '不在范围内，请输入0-100的数字！'
#     elif num02<0:
#         print '不在范围内，请输入大于0的数字！'
#     else:
#         print '你猜错了，数字是：%s ；请继续！！！' % (random01)


'''练习'''
# nums=range(1,5)
# print nums
# b=0
# for i in nums:
#     b = b+i
# print b