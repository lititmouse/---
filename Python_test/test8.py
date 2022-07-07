# -*- coding: utf-8 -*-

s1 = 72
s2 = 85
inprive =  ((s2-s1)/s1)
precent = inprive * 100

print("小明成绩提升的百分点是{0:2f}%".format(precent)) #format方法
print(f"小明成绩提升的百分点是{precent:2f}%")#f—string化
print("小明成绩提升的百分点是%2f" %(precent) ,"%")#格式化字符