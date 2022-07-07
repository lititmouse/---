import re
try:
    temp = input()
    unit= re.findall (r'[a-zA-Z]{1,}$',temp)

    number = re.findall(r'[0-9]{0,} *[0-9]{0,}',temp)
    x = float(number[0])



    if str(unit[0]) not in ["C","c","F","f"]:
        print("输入错误，末位只能是'C','c','F','f'")
    else:
        if str(unit[0])  in ["C","c"]:
            transformed_mubner = x*1.8 + 32
            print(f'{transformed_mubner}f')       
        elif str(unit[0]) in ["F",'f']:
            transformed_mubner =(x-32)/1.8
            print(f'{transformed_mubner:.2f}c')           
except ValueError:
    print("试图访问的变量名不存在")