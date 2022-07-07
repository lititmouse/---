import math
basemuber,times,mode,rate = float(input()),int(input()),str(input()),float(input())
x = 0
if mode == 'AC' or mode == 'ac':
    li = []
    for i in range(times):
        repayemnt = basemuber / times + (basemuber/times)*(times-i)*rate
        li.append (round(repayemnt,2) )
    print(li)
elif mode == 'ACPI' or mode == 'acpi':
    repayment = basemuber * rate * (1 + rate) ** times /((1 + rate) ** times - 1)
    
    print(round(repayment,2) )
else:
    print("还款方式输入错误")