#! python3
# -*- coding: utf-8 -*-
"""大概思路就是这样"""
import requests
from pyquery import PyQuery as pa

r = requests.get('https://www.zhihu.com')
html = r.text
d = pq(html)
urls = d('').attr('href')