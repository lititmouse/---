####函数定义练习####
###第一种方式#####
def max1(a,b):
    if a>b:
        print ("a")
        return
    elif a<b:
        print("b")
        return
    elif a==b:
        print("ab等大")
        return
####第二种写法##########
def max2(x,y):
    if x>y:
        return x
    elif y>x:
        return y
    elif y==x:
        return "二者等大"
#####测试模块######
a,b = 2,2
max1(a,b)
x,y = 2,2
print(max2(x,y))