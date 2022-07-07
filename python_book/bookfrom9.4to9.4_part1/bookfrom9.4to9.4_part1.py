"""
导入类
导入单个类from Car import Car
导入多个类from Car import Car,Electric_car
导热所有的类from Car import *
使用别名from Car import Car as KAR
"""
#导入单个类
from Car import Car
#导入多个类
from Car import Car,Electric_car
my_now_car = Car("长城","重庆",2018)
my_Electric_car = Electric_car("长城","四川")

#print(my_now_car.informations())
#my_now_car.Oil_quantity()
print(my_Electric_car.informations())
my_Electric_car.Oil_quantity()




