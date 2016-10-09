#! python3
# -*- coding: utf-8 -*-
"""python有许多内置API，都允许调用者传入函数，以定制其行为。
API在执行的时候，会通过这些挂钩函数（hook），回调函数内的代码,
函数充当挂钩因为它是一级对象，可以像语言中的其它值一样传递和引用"""
from collections import defaultdict
names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)


def log_missing():
    print('Key added')
    return 0


current = {'green': 12, 'blue': 3}
increments = [('red', 5), ('blue', 17), ('orange', 9)]
result = defaultdict(log_missing, current)


def increment_with_report(current, increments):
