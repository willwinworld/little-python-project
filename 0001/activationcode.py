#! python3
# -*- coding: utf-8 -*-
"""生成16位激活码，数量200个，由大写字母和数字组成，不能有重复"""
import string
import random


def activation(size, chars=string.ascii_uppercase+string.digits):
    res = {}
    for i in range(1, 201):
        activation_code = ''.join(random.choice(chars) for _ in range(size))
        res.setdefault(i, activation_code)
    return res


result = activation(16)
print(result)

