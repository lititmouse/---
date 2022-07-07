#coding=utf-8
"""

'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	create a new file and open it for writing
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
################################
"r"打开阅读（默认值）
"w"打开进行编写，首先截断文件
"x"创建新文件并将其打开以供编写
"a"打开以供书写，如果文件存在，则附加到文件的末尾
"b"二进制模式
"t"文本模式（默认值）

写入空文件open(file,w)
写入多行
"""


import os,sys
#
filname = "test.txt"

with open (filname,"w") as file_object:
    file_object.write("i loved you")
