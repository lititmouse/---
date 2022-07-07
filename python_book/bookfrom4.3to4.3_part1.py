from typing import List
##############################简单的统计计算
list_1=list(range(1,101))
for x in list_1:
    print(x)
print(sum(list_1))
###############################
list_2=list(range(1,101,2))
print(list_2)
################################
list_3 = list(range(0,100,3))
print(list_3)
#################################p51使用range()创建数字列表
list_4 = [value**3 for value in range(1,11) ]
print(list_4)
#################################列表解析
list_5 = []
for value in range(0,11):
    complist = value**3
    list_5.append(complist)
print(list_5)
