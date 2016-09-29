#! python3
# -*- coding: utf-8 -*-


def filter_sentences():
    words_string = ''
    with open('filtered_words.txt', 'r') as f:
        content = f.read()
        sensitive_words = content.split('\n')
        sentence = input('Please input a sentence: ')
        sentence_words = sentence.split()
        for word in sentence_words:
            if word in sensitive_words:
                word = '*'*len(word)
            words_string += word + ' '
        print(words_string)


if __name__ == '__main__':
    filter_sentences()