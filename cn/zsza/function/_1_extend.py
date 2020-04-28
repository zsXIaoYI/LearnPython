# -*- coding: utf-8 -*-
# _1_extend.py
# 2020/4/27 21:25
# __author__ = 'zs'


class First:

    def setData(self, value):
        self.data = value

    def print(self):
        print('First class data:', self.data)


class Second(First):

    def print(self):
        print('Second class value = %s:' % self.data)


class Third(Second):

    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return Third(self.data + other)

    def __str__(self):
        return '[Third: %s]' % self.data

    def mul(self, other):
        self.data *= other


if __name__ == '__main__':
    third = Third('ab')
    third.print()   # Third继承于Second,由于本身没有覆写父类的print()方法，则调用Second类的print()方法

    add_third = third + 'cc'  # 会调用Third类中的__add__()方法
    add_third.print()
    print(add_third)          # 会调用__str__()方法

    third.mul(2)
    print('after mul third:', third)

    print(Third.__dict__)
    print(list(Third.__dict__.keys()))
