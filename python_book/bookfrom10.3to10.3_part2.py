"""
使用异常来避免崩溃try-except
else代码隐藏traceback:try-except-else
"""

print("give me two number,and I`ll divide them.")
print("enter'q'to quit")

while True:
    first_number = input("\n Frist number:")
    if first_number == "q":
        break
    second_number = input("\n second number:")
    if second_number == "q":
        break
    try:
         answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can not divide by '0'")
    else:
        print(answer)
