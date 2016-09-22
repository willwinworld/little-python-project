#! python3
# -*- coding: utf-8 -*-
"""生成16位激活码，数量200个，由大写字母和数字组成，不能有重复"""
import string
import random


def activation(size, chars=string.ascii_uppercase+string.digits):
    res = {}
    for i in range(start=1, stop=200):
        activation_code = ''.join(random.choice(chars) for _ in range(size))
        res.setdefault()

print(activation(16))


