#在循环中使用continue
#找出奇数
x =  int(input('输入正整数'))
recycle_number = 0
while recycle_number<x:
    recycle_number += 1
    if recycle_number%2 == 0:
        continue    
    print(recycle_number)   
else:
    print("end")