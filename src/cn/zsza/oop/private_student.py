# -*- coding: utf-8 -*-
# private_student.py
# 2020/5/5 16:22
# __author__ = 'zs'


class Student(object):

    # 属性名以双下划线开头的,则称为对象的私有属性,对外不能直接访问
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


if __name__ == '__main__':
    stu = Student('小明', 88)
    print(stu.get_name())
