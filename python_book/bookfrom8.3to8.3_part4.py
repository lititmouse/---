

def get_complete(f_name,l_name):
    full_name = f"{f_name}{l_name}" 
    return full_name .title()

active = True

while active: 
    print("\n请告诉我你的名字")
    print("(按q清除\n按exit结束循环)")


    f_name = input("请输入你的姓")
    if f_name=="q":
        continue
    elif f_name == "exit":
        break

    l_name = input("请输入你的名字")
    if l_name=="q":
        continue
    elif l_name == "exit":
        break

    formatted_name = get_complete(f_name,l_name)
    print(f"\n\t欢迎!\n\t{formatted_name}来到本店!")