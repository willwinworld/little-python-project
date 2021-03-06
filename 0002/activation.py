#! python3
# -*- coding: utf-8 -*-
"""生成16位激活码，数量200个，由大写字母和数字组成，不能有重复"""
import string
import random
from peewee import IntegrityError
from fnvhash import fnv1a_32
from activation_model import Activation

res = set()  # 不能将res这个元祖放在函数里面，这样每次去调用函数时，由于python是创建的貌似是动态变量，
# 每次调用函数完后res就消失了，所以可以看到如果写在函数里面，res的长度始终是1，
# 所以最终会超过python的最大递归深度999，从而导致错误


def activation(size, chars=string.ascii_uppercase+string.digits):  # 通过元祖去重，通过递归达到数量
    activation_code = ''.join(random.choice(chars) for _ in range(size))
    res.add(activation_code)
    if len(res) == 200:
        return res
    # activation(16) 直接这样写是没有返回值的
    return activation(16)


def organize_data_structure():
    receive = activation(16)
    count = 1
    result = {}
    while True:
        result.setdefault(count, receive.pop())
        count += 1
        if len(receive) == 0:
            break
    return result


def save():
    receive = organize_data_structure()
    keys = sorted(receive.keys(), reverse=True)
    values = sorted(receive.values(), reverse=True)
    while True:
        try:
            key = keys.pop()
            value = values.pop()
            Activation.create(serial_number=key,
                              activation_code=value)
        except IndexError as err:
            break
    # try:
    #     Activation.create(serial_number=fnv1a_32(repr('实验012')),
    #                       activation_code='a')  # python3中貌似这个fnv1a_32有问题
    # except IntegrityError as err:
    #     print(err)

save()