"""
给子类定义属性和方法
重写父类
"""



class Car:
    #模拟车及其属性
    def __init__(self,maker,displacement,year=2019,):
        #属性初始化
        self.maker = maker
        self.displacement = displacement
        self.year = year
        #设置默认值
        self.mileage = 0
        self.oll= 100
    
    def informations(self):
        #返回汽车所有的属性
        long_name = f"制造厂家:\n{self.maker}\n产地:\n{self.displacement}\
            \n生产日期:\n{self.year},\n里程:\n{self.mileage}\n"
        return long_name

    def update_mileage(self,now_mileage):
        #通过方法修改属性的值
        #静止将里程表回调
        if now_mileage >= self.mileage:
            self.mileage = now_mileage
        else:
            print("\n里程表禁止回调\n里程表禁止回调\n里程表禁止回调")
    
    def ascending_mileage(self,now_mileage):
        #里程表读数增加指定的量
        self.mileage += now_mileage

       
   
    def Oil_quantity(self):
        print(f"剩余油量为{self.oll}")

oll_car = Car("小米","四川")

print(oll_car.informations())


# 重写父类# 

class electric_car(Car):
    def __init__(self,maker,displacement,year):
        super().__init__(maker,displacement,year)
        #给子类定义属性和方法
        self.battery = 70
    def show_battery(self):
        print(f"剩余电量为{self.battery}.")

    def Oil_quantity(self):
        print(f"电动车不烧油")

now_car = electric_car("小米","四川",2020)

print(now_car.informations())

now_car.show_battery()
now_car.Oil_quantity()

