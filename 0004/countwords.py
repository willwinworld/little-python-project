#! python3
# -*- coding: utf-8 -*-

line_counts = 0  # 有多少行
word_counts = 0  # 有多少个单词
character_counts = 0  # 一行有多少个字节，包括空格

with open('words.txt', 'r') as f:
    for line in f:
        print(line)
        words = line.split()

        line_counts += 1
        word_counts += len(words)
        character_counts += len(line)

print("line_counts ", line_counts)
print("word_counts ", word_counts)
print("character_counts ", character_counts)