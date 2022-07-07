# -*- coding: UTF-8 -*-

"""
创建一个包含文件各行的  列表   
"""

with open("python_book\yuanzhoulu.txt") as onefile:
    lines = onefile.readlines()

for line in lines:
    print(line.strip())