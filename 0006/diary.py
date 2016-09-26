#! python3
# -*- coding: utf-8 -*-
import json
from glob import glob


def census():
    count = 1
    for file in glob('diary/*.txt'):
        res = {}  # 每篇文章的统计的词频结果保存在一个结果,所以在内部创建结果
        with open(file, 'r') as f:
            for line in f:  # 一篇文章中的每行
                words = line.split()
                for word in words:  # 每行中每个单词
                    res.setdefault(word, words.count(word))

        sorted_res = dict(sorted(res.items(), key=lambda d: d[1], reverse=True))
        save_format = json.dumps(sorted_res, sort_keys=True, indent=4)
        with open('res/res_%s.txt' % count, 'w') as ff:
            ff.write(save_format)

        count += 1


if __name__ == '__main__':
    census()
