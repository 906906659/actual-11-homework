#encoding: utf-8

import random

secret = random.randint(1, 100)
guess = 0
tries = 0

print ("唔哈！！ 我是可怕的海盗罗伯茨，我有一个秘密！")
print ("这是一个从1到99的数字，我只会给你6次机会。")

while guess != secret and tries <6:
    guess = int(raw_input("你猜这个数是多少?  "))
    if guess < secret:
        print ("太低了，你这只笨狗熊!  ")
    elif guess > secret:
        print ("太高了, 你这只笨狗熊!  ")
    tries = tries +1
if guess == secret:
    print ("我的上帝！你居然发现了我的秘密!")
else:
    print ("你唯一的机会已被你用完了！伙计!你就是只愚蠢的笨狗熊！")
    print ("还是让我告诉你吧！这个数字是:%s" % secret)