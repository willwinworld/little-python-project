#! python3
# -*- coding: utf-8 -*-
# from openpyxl import load_workbook
#
#
# wb2 = load_workbook('student.txt')
# print(wb2.data_only)


# def log(message, values):
#     if not values:
#         print(message)
#     else:
#         values_str = ','.join(str(x) for x in values)
#         print('%s: %s' % (message, values_str))
#
#
# log('My numbers are', [1, 2])
# log('Hi there', [])

# def my_generator():
#     for i in range(10):
#         yield i
#
# def my_func(*args):
#     print(args)
#
# it = my_generator()
# my_func(*it)


# def log(sequence, message, *values):
#     if not values:
#         print('%s: %s' % (sequence, message))
#     else:
#         values_str = ','.join(str(x) for x in values)
#         print('%s: %s: %s' % (sequence, message, values_str))
# from datetime import datetime
# import time, json
# def log(message, when=None):
#     when = datetime.now() if when is None else when
#     print('%s: %s' % (when, message))
#
# log('Hi there!')
# time.sleep(0.1)
# log('Hi again!')
#
# def decode(data, default=None):
#     if default is None:
#         default = {}
#     try:
#         return json.loads(data)
#     except ValueError:
#         return default
#
# foo = decode('bad data')
# print(type(foo))
# foo['stuff'] = 5
# print('Foo:', foo)
class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}  # {'name':[score1, score2]}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


class BySubjectGradebook(object):
    def __init__(self):
        self._grades = {}  # {'_grades': {'Albert Einstein': {'Math': [75], 'Gym': [90]}}}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]  # 就是一个字典
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

# book = BySubjectGradebook()
# book.add_student('Albert Einstein')
# book.report_grade('Albert Einstein', 'Math', 75)
# book.report_grade('Albert Einstein', 'Gym', 90)
# print(book.__dict__)  # 看内部的字典信息
import collections


Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()  # 竟然这样实例化，将字典的值作为实例
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]

