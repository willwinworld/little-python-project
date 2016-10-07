#! python2
# -*- coding: utf-8 -*-
"""http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests"""
import shutil
import requests
from pyquery import PyQuery as pq


def get_pics():
    r = requests.get('http://tieba.baidu.com/p/2166231880')
    html = r.text
    d = pq(html)
    main_body = d('.content.clearfix img')
    res = [pq(node).attr('src') for node in main_body]
    return res


def save_to_local():
    pics = get_pics()
    for index, i in enumerate(pics, start=1):
        r = requests.get(i, stream=True)
        if r.status_code == 200:
            with open('%s.jpg' % index, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

if __name__ == '__main__':
    print(get_pics())
    print(len(get_pics()))
    save_to_local()
