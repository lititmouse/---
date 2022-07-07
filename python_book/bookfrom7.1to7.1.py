#使用int()获取整数输入
#判断X是不是N的整数
x = int(input("输入被判断的值\n"))
N = int(input("输入整数值\n30"))

if x % N == 0:
    print(f"{x}是{N}的整数倍")
else:
    print(f"{x}不是{N}的整数倍")
