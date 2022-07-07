"""
使用try-except代码块
"""


try:
    print(5/0)
except ZeroDivisionError:
    print("不能除以0")