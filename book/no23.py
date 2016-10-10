#! python3
# -*- coding: utf-8 -*-
"""python有许多内置API，都允许调用者传入函数，以定制其行为。
API在执行的时候，会通过这些挂钩函数（hook），回调函数内的代码,
函数充当挂钩因为它是一级对象，可以像语言中的其它值一样传递和引用"""
from collections import defaultdict
# names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
# names.sort(key=lambda x: len(x))
# print(names)
#
#
# def log_missing():
#     print('Key added')
#     return 0
#
#
# current = {'green': 12, 'blue': 3}
# increments = [('red', 5), ('blue', 17), ('orange', 9)]
# result = defaultdict(log_missing, current)
#
#
# def increment_with_report(current, increments):
# food_list = 'spam spam spam spam spam spam eggs spam'.split()
# food_count = defaultdict(int)
# print(food_count)
# for food in food_list:
#     food_count[food] += 1
# print(food_count)

# ice_cream = defaultdict(lambda: 'Vanilla')
# ice_cream['Sarah'] = 'Chunky Monkey'
# ice_cream['Abdul'] = 'Butter Pecan'
# print(ice_cream['Sarah'])
# print(ice_cream['Joe'])

# somedict = {}
# print(somedict[3])

# somedict = defaultdict(int)
# print(somedict[3])


# city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'),
#              ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
# cities_by_state = defaultdict(list)  # 创建的默认字典的值是一个列表，同理可推其它
# for state, city in city_list:
#     cities_by_state[state].append(city)
# # print(cities_by_state)
#
# for state, cities in cities_by_state.items():
#     print(state, ','.join(cities))
"""defaultdict(int), defaultdict(list) defaultdict(lambda: xxx), defaultdict(function_name)
Be sure to pass the function object to defaultdict().
Do not call the function, i.e. defaultdict(func), not defaultdict(func())."""


def log_missing():
    print('key added')
    return 0


current = {'green': 12, 'blue': 3}
increments = [('red', 5), ('blue', 17), ('orange', 9)]
result = defaultdict(log_missing)
print('Before:', dict(result))
for key, amount in increments:
    result[key] += amount
print('After:', dict(result))
