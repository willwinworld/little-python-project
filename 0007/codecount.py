#! python3
# -*- coding: utf-8 -*-
"""统计写过多少行代码，包括空行和注释"""
import os
import sys
import re


def each(path):
    All = []
    for root, dirs, files in os.walk(path):  # 根目录, 文件夹名, 文件
        for name in files:
            All.append(root+"/"+name)
    return All

# print(each(os.path.abspath('.')))
# ['D:\\show-me-the-code\\0007/codecount.py']


def deal(input):
    if os.path.splitext(input)[1] in [".py", ".pyw"]:
        # print('@@')
        # print(os.path.splitext(input))  # ('D:\\show-me-the-code\\0007\\test/test', '.py')
        # print('@@')
        total, comment, empty = 0, 0, 0  # 总行数，评论，空白
        with open(input, "r", encoding='utf8') as f:
            in_comment = False  # 是否在注释里面
            for line in f:
                total += 1
                if re.findall("\"\"\"$", line):  # 找到一行文本是否有以"""结尾, 匹配字符串的结束
                    if in_comment:
                        in_comment = False
                    else:
                        in_comment = True
                if not re.findall("\S", line):  # \S匹配任意不是空白符的字符
                    empty += 1
                if line[0] == '#' or in_comment:
                    comment += 1
            return total, comment, empty
    else:
        return 0, 0, 0

if len(sys.argv) <= 1:  # LOC意思是代码行
    print("The Script will calculate the LOC of the file in " + os.path.split(os.path.realpath(__file__))[0]+"/")
    path = os.path.split(os.path.realpath(__file__))[0] + "/"
else:
    print("calculating the file in "+sys.argv[1])
    if os.path.isdir(sys.argv[1]):
        path = sys.argv[1]
    else:
        print("Path Error! use this script as"+os.path.split(os.path.realpath(__file__))[1]+"[path]")

t, c, e = 0, 0, 0
for i in each(os.path.abspath('test')):
    t_a, c_a, e_a = deal(i)
    t += t_a
    c += c_a
    e += e_a
print("Total lines: %s, Empty lines: %s. Comment Lines: %s." % (t, e, c))

