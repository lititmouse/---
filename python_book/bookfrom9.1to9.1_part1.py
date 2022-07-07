#创建DOg类

class Dog:
    def __init__(self, name,age):
        self._name = name
        self._age = age

    def sit (self):
        print(f"{self.name}坐下了")
    def roll_over (self):
        print(f"{self.name}打滚了")


    
my_dogs =  Dog("xiaoming",6)

my_dogs.roll_over()
my_dogs.sit()