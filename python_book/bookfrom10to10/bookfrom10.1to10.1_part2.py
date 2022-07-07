"""
逐行读取
"""


with open("python_book\yuanzhoulu.txt") as onefile:
    for line in onefile:
        print (line.rstrip())