"""
使用文件的内容

"""
from os import linesep



with open("python_book\yuanzhoulu.txt") as onefile:
    lines = onefile.readlines()

pi_string = " "
for line in lines:
    pi_string += line.rstrip()


print (pi_string)
print (len(pi_string))