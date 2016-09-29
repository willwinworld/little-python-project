#! python3
# -*- coding: utf-8 -*-
import os
import re
import sys

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))
# print('@@')
# print(os.path)
# print(os.path.realpath(__file__))
# print(os.path.split(os.path.realpath(__file__))[0])
# print(os.path.split(os.path.realpath(__file__))[1])
# print('@@')
# for root, dirs, files in os.walk('test'):
#     print(root)
#     print(dirs)
#     print(files)


# def sort_priority(values, group):
#     def helper(x):
#         if x in group:
#             return 0, x
#         return 1, x
#     values.sort(key=helper)


# def sort_priority2(numbers, group):
#     found = False
#     def helper(x):
#         if x in group:
#             found = True
#             return 0, x
#         return 1, x
#     numbers.sort(key=helper)
#     return found
#
#
# found = sort_priority2([8, 3, 1, 2, 5, 4, 7, 6], {2, 3, 5, 7})
# print('Found:', found)
#
#
# def sort_priority3(numbers, group):
#     found = False
#     def helper(x):
#         nonlocal found
#         if x in group:
#             found = True
#             return 0, x
#         return 1, x
#     numbers.sort(key=helper)
#     return found


# class Sorter(object):
#     def __init__(self, group):
#         self.group = group
#         self.found = False
#
#     def __call__(self, x):
#         if x in self.group:
#             self.found = True
#             return 0, x
#         return 1, x



# sorter = Sorter(group1)
# numbers1.sort(key=sorter)
# assert sorter.found is True


# def sort_priority(numbers, group):
#     found = [False]
#     def helper(x):
#         if x in group:
#             found[0] = True
#             return 0, x
#         return 1, x
#     numbers.sort(key=helper)
#     return found
#
#
# group1 = {2, 3, 5, 7}
# numbers1 = [8, 3, 1, 2, 5, 4, 7, 6]
# print(sort_priority(numbers1, group1))
# def index_words(text):
#     if text:
#         yield 0
#     for index, letter in enumerate(text):
#         if letter == ' ':
#             yield index + 1
#
#
# address = 'Four score and seven years ago...'
# result = index_words(address)
# def index_file(handle):
#     offset = 0
#     for line in handle:
#         if line:
#             yield offset
#         for letter in line:
#             offset += 1
#             if letter == ' ':
#                 yield offset
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)