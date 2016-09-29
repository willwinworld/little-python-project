#! python3
# -*- coding: utf-8 -*-
"""用pandas去导入数据"""
import pandas


def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


def normalize_func(get_iter):
    total = sum(get_iter)
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result






