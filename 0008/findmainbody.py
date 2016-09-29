#! python3
# -*- coding: utf-8 -*-
"""寻找html的正文, 可以采用python2下面的goose包进行采集，或者就要采用算法去判断阈值
可以参考这两篇文章:参考http://blog.csdn.net/gzlaiyonghao/article/details/1741185和
http://www.cnblogs.com/jasondan/p/3497757.html的算法思路"""
from goose import Goose
from goose.text import StopWordsChinese

# 要分析的网页url
url = 'http://www.ruanyifeng.com/blog/2015/05/thunk.html'


def extract(url):
    '''
    提取网页正文
    '''
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    return article.cleaned_text

if __name__ == '__main__':
    print(extract(url))