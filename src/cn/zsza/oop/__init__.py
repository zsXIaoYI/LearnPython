# -*- coding: utf-8 -*-
# __init__.py.py
# 2020/4/27 17:07
# __author__ = 'zs'

# 最简单的python类
class ClassTest:
    pass


class Student(object):
    # __init__：构造函数
    # 两个下划线开头的变量是私有的
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
