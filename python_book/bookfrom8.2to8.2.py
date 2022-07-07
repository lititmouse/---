#传递参数的几种方法
##def appoint_food (mane,food,number):
 #   print(f'{mane}\t 点了 \t{number}个{food}\n')
 #默认值number="3"
def appoint_food (mane,food,number="3"):
    print(f'{mane}\t 点了 \t{number}个{food}\n')


#输入位置参数
appoint_food("xiaoming","包子","1")
#输入关键字参数
appoint_food(mane="xiaoming",food="包子",number="1")
#默认值
appoint_food(mane="小赵",food="馒头")