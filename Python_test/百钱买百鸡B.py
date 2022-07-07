import math

number,money = map ( int ,input().split(sep = ' '))
#Rooster 公鸡 |hen 母鸡 |chick 小鸡
flag = 0 

for  Rooster in range(1,math.ceil( money / 5)):
    for hen in range(1,math.ceil( money / 3)):
        chick = number - hen - Rooster
        if chick % 3 == 0 and chick > 0 and 5 * Rooster + 3 * hen + chick // 3 == money:
            print(Rooster,hen,chick)
            flag = 1 
if flag== 0:
    print("无解")
