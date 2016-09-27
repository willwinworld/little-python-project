#! python3
# -*- coding: utf-8 -*-
import os
import re
import sys

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))
print('@@')
print(os.path)
print(os.path.realpath(__file__))
print(os.path.split(os.path.realpath(__file__))[0])
print(os.path.split(os.path.realpath(__file__))[1])
print('@@')
for root, dirs, files in os.walk('test'):
    print(root)
    print(dirs)
    print(files)