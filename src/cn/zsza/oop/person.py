# -*- coding: utf-8 -*-
# person.py
# 2020/4/30 17:38
# __author__ = 'zs'


class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print('FirstName is:%s, and LastName is %s'
              % (self.first_name, self.last_name))


if __name__ == '__main__':
    person = Person('Michael', 'Jack')
    person.display()
