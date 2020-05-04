# -*- coding: utf-8 -*-
# person.py
# 2020/4/30 17:38
# __author__ = 'zs'


class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_str):
        print('cls:', cls)     # cls返回<class '__main__.Person'>, 是指类对象
        if not cls.check_full_name(name_str):
            raise Exception()
        first_name, last_name = map(str, name_str.split(' '))
        per = cls(first_name, last_name)
        return per

    @staticmethod
    def check_full_name(name_str):
        names = name_str.split(' ')
        return len(names) > 1

    def display(self):
        print('FirstName is:%s, and LastName is %s'
              % (self.first_name, self.last_name))


if __name__ == '__main__':
    person = Person('Michael', 'Jack')
    print('person:', person)
    person.display()
    print('-----------------------')
    # 上面person对象的创建,可用如下代码
    person1 = Person.from_string('Michael Jack')
    print('person1:', person1)
    person1.display()
