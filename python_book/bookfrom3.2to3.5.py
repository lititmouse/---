member1 = ["七星","路迪乌斯","希露菲","洛琪希","夏爱","诺论","莉莉娅","塞尼丝"]
print(member1)
#修改名字
member1[1] = "希露菲叶特"
print(member1)
#添加爱丽丝
member1.append("爱丽丝")
print(member1)
#插入 "露西"
member1.insert(-1,'露西')
print(member1)
#删除七星
del member1[0]

print(member1)
#弹出爱丽丝
member3 = member1.copy()

ppoped_member = member3.pop()

print(member1)

print(member3)

print(ppoped_member)
#删除露西
member3.remove("露西")

print(member3)
