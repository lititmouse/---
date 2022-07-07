"""
将实例作用属性
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
        long_name = f"制造厂家:\n{self.maker}\n产地:\n{self.displacement}\n生产日期:\n{self.year},\n里程:\n{self.mileage}\n"
        return long_name


class Battery():
    def __init__(self,battery = 75):
        self.battery =battery

    def discribe_battery(self):
        print(f'剩余电量{self.battery}')

class eletriccar(Car):
    def __init__(self,maker,displacement,year):
        super().__init__(maker,displacement,year)
        self.battery = Battery()

mynowcare = eletriccar('小米',"上海",2020)

print(mynowcare.informations())
print(mynowcare.battery.discribe_battery())