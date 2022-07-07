import os
"""
从文件中读取数据
读取整个文件

"""


with open("python_book\yuanzhoulu.txt") as onefile:
    conrents = onefile.read()
    print(conrents.rstrip())
    
 

