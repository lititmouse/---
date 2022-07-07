#while 循环处理列表和字典
#在列表中移动元素
#已经验证空列表和未验证的非空列表
unconfidented_user = ["xiaoming","xiaohua","xiaozhao"]
confidented_user = []

while len(unconfidented_user) > 0:
    curent_user =unconfidented_user.pop()
    print(curent_user)
    confidented_user.append(curent_user)
else:
    for user in confidented_user:
        print(f"confidented_user包括{user}")
