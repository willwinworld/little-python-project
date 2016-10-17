# python2
# -*- coding: utf-8 -*-
"""https://github.com/Show-Me-the-Code/python/blob/master/Liez-python-code/0020/0020.py
或者最简单的统计总通话时间,现在画图一般采用JavaScript的ECharts去画
matplotlib在虚拟环境中有问题,用python2.7非虚拟环境下即可
http://blog.topspeedsnail.com/archives/836"""
from openpyxl import load_workbook
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal
# 统计话费，统计被叫主叫次数，统计通话时间，统计通话时长，通话次数统计图，根据被叫主叫次数作饼图


def get_data_from_one_column(filename, coordinate_tuple, res_list):
    wb = load_workbook(filename)
    ws = wb.get_sheet_by_name('Sheet1')
    min_col, min_row, max_col, max_row = coordinate_tuple
    for col in ws.get_squared_range(min_col, min_row, max_col, max_row):
        for cell in col:
            res_list.append(cell.value)
    return res_list


def organize_data_structure():
    start_time = get_data_from_one_column('statistic.xlsx', (2, 2, 2, 107), [])  # 起始时间
    call_type = get_data_from_one_column('statistic.xlsx', (3, 2, 3, 107), [])  # 通话类型
    call_time = get_data_from_one_column('statistic.xlsx', (4, 2, 4, 107), [])  # 通话时长
    total_fee = get_data_from_one_column('statistic.xlsx', (5, 2, 5, 107), [])  # 总话费
    long_distance_type = get_data_from_one_column('statistic.xlsx', (6, 2, 6, 107), [])  # 长途类型
    call_location = get_data_from_one_column('statistic.xlsx', (7, 2, 7, 107), [])  # 话单位置
    roam_type = get_data_from_one_column('statistic.xlsx', (8, 2, 8, 107), [])  # 漫游类型
    total = zip(start_time, call_type, call_time, total_fee, long_distance_type, call_location, roam_type)
    raw = list(total)
    res = []
    for i in raw:
        res.append({'start_time': i[0], 'call_type': i[1], 'call_time': int(i[2]),
                    'total_fee': Decimal(i[3]), 'long_distance_type': i[4], 'call_location': i[5],
                    'roam_type': i[6]})
    return res


def count_fee():  # 统计总费用
    data = organize_data_structure()
    total_fees = Decimal(0.00)
    for i in data:
        total_fees += i['total_fee']
    return float(total_fees)


def count_calling_called():  # 统计主叫，被叫次数, 通话总次数
    data = organize_data_structure()
    calling = 0
    called = 0
    for i in data:
        if i['call_type'] == u'主叫':
            calling += 1
        else:
            called += 1
    total = calling + called
    return calling, called, total


def count_time():  # 统计主叫总时间，被叫总时间，通话总时间
    data = organize_data_structure()
    calling_time = 0
    called_time = 0
    for i in data:
        if i['call_type'] == u'主叫':
            calling_time += i['call_time']
        else:
            called_time += i['call_time']
    total_time = calling_time + called_time
    return calling_time, called_time, total_time


def draw_one_column_bar_chart():
    objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    y_pos = np.arange(len(objects))
    performance = [10, 8, 6, 4, 2, 1]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Programming language usage')

    plt.show()


def fee():  # 总费用
    month = 'March'
    ind = np.arange(1)
    performance = count_fee()

    plt.bar(ind, performance, align='center', width=0.001, alpha=0.5)
    plt.xticks(ind, month)
    plt.ylabel('total fee')
    plt.title('Monthly cellphone fee')

    plt.show()


def time():  # 总时间
    month = 'March'
    ind = np.arange(1)
    calling_time, called_time, total_time = count_time()

    plt.bar(ind, total_time, align='center', width=0.001, alpha=0.5)
    plt.xticks(ind, month)
    plt.ylabel('total time')
    plt.title('Monthly cellphone fee')

    plt.show()


def call():  # 总通话次数
    month = 'March'
    ind = np.arange(1)
    calling, called, total = count_calling_called()

    plt.bar(ind, total, align='center', width=0.001, alpha=0.5)
    plt.xticks(ind, month)
    plt.ylabel('total call time')
    plt.title('Monthly cellphone fee')

    plt.show()


def pie_chart_1():  # 主叫时间, 被叫时间
    calling_time, called_time, total_time = count_time()

    plt.pie(
        (calling_time, called_time),
        labels=('calling_time', 'called_time'),
        shadow=True,
        colors=('yellowgreen', 'lightskyblue'),
        explode=(0, 0.15),
        startangle=90,
        autopct='%1.1f%%'
    )
    plt.legend(fancybox=True)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


def pie_chart_2():  # 主叫次数, 被叫次数
    calling_count, called_count, total = count_calling_called()

    plt.pie(
        (calling_count, called_count),
        labels=('calling_count', 'called_count'),
        shadow=True,
        colors=('yellowgreen', 'lightskyblue'),
        explode=(0, 0.15),
        startangle=90,
        autopct='%1.1f%%'
    )
    plt.legend(fancybox=True)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    draw_one_column_bar_chart()
    fee()
    time()
    call()
    pie_chart_1()
    pie_chart_2()




