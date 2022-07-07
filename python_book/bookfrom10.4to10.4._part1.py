"""
存储数据
使用json.dump()和json.load()
数据共享的简单方式
"""

import json

numbers = [2,3,4,5,6,7,8,9,10,11,12,13]

filename = "numbers.json"
with open(filename,"w") as f:
    json.dump(numbers,f)


with open(filename,"r") as l:
    number1 = json.load(l)

print(number1)