#! python3
# -*- coding: utf-8 -*-


def filter_words():
    with open('filtered_words.txt', 'r') as f:
        content = f.read()
        sensitive_words = content.split('\n')
        word = input('Please input a word: ')
        if word in sensitive_words:
            print('Freedom')
        else:
            print('Human Rights')


if __name__ == '__main__':
    filter_words()