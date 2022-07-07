from typing import Counter
#遍历字典

user = {
    "xiangxing":"123",
    "xiaohong":"4567",
    "xianghuang":"2223333",
    "xiaoli":"2223333",
    "xuaitian":"838338",   
}
#空集合
ste_1 = set()
#遍历所有的键值对用方法dict.item()
for Counter , keys in user.items():
    print(f"\n账户:{Counter}")
    print(f"密码:{keys}")

#遍历所有的键:dict.keys()
for Counter in user.keys():
    print(f"\n账户:{Counter}")

#遍历所有的值:dict.value()
for keys in user.values():
     print(f"密码:{keys}")
     #集合去重(方法一)
     ste_1.add(keys)
print(ste_1)
#集合去重(方法二)
for keys_2 in set(user.values()):
    print(keys_2)