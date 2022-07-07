#
prompt = '\n你输入什么我打印什么\n输入quit退出\n输入内容:'
massage = " "
#标记active
active = True

while active :
    massage = input(prompt)
    if massage == "quit":
        active = False
        print (massage)
    else:
        print (massage)
