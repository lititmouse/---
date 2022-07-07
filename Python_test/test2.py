### coding: utf-8



Counter = int(input("你的输入"))
number = 0
###计算循环超过1000的次数
while number <= 1000 :
    Counter = Counter+number
    number = number + 1
else:
    print("Counter等于 %s nmber等于 %s " %(Counter,number))
