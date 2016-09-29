#! python3
# -*- coding: utf-8 -*-


with open('filtered_words.txt', 'r') as f:
    words = list(map(lambda i: i.strip('\n'), f.readlines()))
    print(words)
