#使用break退出函数
prompt = '\n你输入什么我打印什么\n输入quit退出\n输入内容:'
massage = " "

active = True

while active :
    massage = input(prompt)
    if massage == "quit":
      # active = False
        print (massage)
        break
    else:
        print (massage)
