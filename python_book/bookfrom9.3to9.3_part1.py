"""
继承
子类的方法__init__
"""


class Car:
    #模拟车及其属性
    def __init__(self,maker,displacement,year):
        #属性初始化
        self.maker = maker
        self.displacement = displacement
        self.year = year
        #设置默认值
        self.mileage = 0
    
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


class electric_car(Car):
    def __init__(self,maker,displacement,year):
        super().__init__(maker,displacement,year)

now_car = electric_car("小米","四川",2020)

print(now_car.informations())