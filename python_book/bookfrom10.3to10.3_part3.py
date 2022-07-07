import os

import os

"""
处理FileNotFountError异常
"""
"""
filename = "ali.txt"

with open(filename,"r") as f:\
    content = f.read()

"""

filename = "ali.txt"
try:
    with open(filename,"r") as f:\
    content = f.read()
except FileNotFoundError:
    print("File not found")