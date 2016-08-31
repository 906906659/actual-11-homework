#coding: utf-8

nums = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]

new_nums = set(nums)
max_num = max(new_nums)

new_nums.remove(max_num)
sec_num = max(new_nums)

print max_num, sec_num

print "==========="

new_nums = sorted(nums, reverse = True)
max_num = new_nums[0]

for i in new_nums:
    if i != max_num:
        sec_num = i
        break

print max_num, sec_num

