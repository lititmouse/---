#使用用户输入填充词典
#创建空的调查问卷
likeed_food_dict ={}
#设置一个标志检查是否继续
Judgment_point = True

while Judgment_point:
    name = input("你的名字:\n:")
    food = input("你喜欢的食物\n:")
    #将输入的"food"储存到词典中"
    likeed_food_dict[name] = food
    #判断是否继续询问
    reply = input("是否愿意接受调查(yes/no)")
    if reply == 'no':
        Judgment_point = False
else:
    print(likeed_food_dict.items())