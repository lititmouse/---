"""
创建DOg类
"""

class Dog:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def sit (self):
        print(f"{self.name}坐下了")
    def roll_over (self):
        print(f"{self.name}打滚了")

my_dog =  Dog("xiaoming",6)
#访问属性
print(f"我的狗的名字是{my_dog.name}")
#调用方法
my_dog.roll_over()
my_dog.sit()
#创建多个实例

dog_1 = Dog("xiaohua",1)
dog_2 = Dog("wangcai",1)

dog_1.sit()
dog_2.sit()