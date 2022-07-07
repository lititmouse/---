#删除特定值得所有列表元素
pets = ['狗','猫','猫','猫',"鸟",'猪']
print(pets)

while "猫" in pets:
    pets.remove("猫")
else:
    print(pets)