import math
#输入
number = input()
#空集合
number_string = list(number)
x= 0
for i in  number_string:
    y = int(i)
    x += math.factorial(y)

if x == int(number):
    print("YES")
else:
    print("NO")
