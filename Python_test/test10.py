#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
#用if-elif判断并打印结果：

# -*- coding: utf-8 -*-

height = 1.75
weight = 1.5

bmi = weight / (height**2)
if bmi>32:
    print("小明严重肥胖")
elif bmi >= 28:
     print("小明肥胖")
elif bmi>= 25:
    print("小明过重")
elif bmi>+18.5:
    print("小明正常")
elif bmi<18.5:
    print("小明过轻")
