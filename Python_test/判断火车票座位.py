import re

seat = input()

if re.match(r"^[0-17]{1,2}[AF]$",seat):
    print("窗口")
elif re.match(r"^[0-17]{1,2}[CD]$",seat):
    print("过道")
elif re.match(r"^[0-17]{1,2}[B]$",seat):
    print("中间")
else:
    print("座位不存在")
