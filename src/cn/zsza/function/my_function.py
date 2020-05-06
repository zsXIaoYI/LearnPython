# -*- coding: utf-8 -*-
# my_function.py
# 2020/5/5 17:59
# __author__ = 'zs'


import math


def my_abs(x):
    """
    求一个整数的绝对值
    :param x:
    :return:
    """
    if not isinstance(x, int):
        raise TypeError('输入不是整数')
    if x > 0:
        return x
    else:
        return -x


# Python函数返回多个值,angle为默认参数,不传该参数默认为0
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step + math.sin(angle)
    return nx, ny


# 求解一元二次方程,a、b、c为三个系数
def quadratic(a, b, c):
    sq_b = b ** 2
    temp = 4 * a * c
    if sq_b < temp:
        return '方程组无解'
    elif sq_b == temp:
        s1 = -b / 2 * a
        s2 = s1
        return s1, s2
    else:
        s1 = (-b + math.sqrt(sq_b - temp)) / (2 * a)
        s2 = (-b - math.sqrt(sq_b - temp)) / (2 * a)
        return s1, s2


# 对于power()方法而言,参数x是一个位置参数
def power(x):
    if not isinstance(x, (int, float)):
        raise TypeError("only support int or float")
    return x ** 2


# 求x的n次幂，x和n也称作位置参数
# n声明为2，则称为默认参数,默认参数必须在位置参数后面
def power_n(x, n=2):
    result = 1
    while n > 0:
        n -= 1
        result = result * x
    return result


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
# 定义默认参数要牢记一点：默认参数必须指向不变对象
def add_end(L=[]):
    L.append('end')
    return L


def add_end_none(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


# 求一系列数的平方和
# 调用的时候，需要先组装出一个list或tuple
def calc(numbers):
    result = 0
    for i in numbers:
        result += i * i
    return result


# 带有可变参数的函数
# *numbers为可变参数, numbers是个tuple类型
def calc_2(*numbers):
    result = 0
    for i in numbers:
        result += i * i
    return result


# 带有关键字参数的函数
# 参数kw被解析成dict类型
def print_one(name, age, **kw):
    # print(isinstance(kw, dict))
    print('name:', name, 'age:', age, 'other:', kw)


# 带有命名关键字参数的函数
# 后面必须跟city和job参数
# city或job参数也可以写成默认形式,比如city='堪培拉'
def print_two(name, *, city, job):
    print('My name\'s is %s, and from %s, and job is %s'
          % (name, city, job))


# 带有可变参数，命名关键字的函数
# *args的参数后面为命名关键字的参数，args是个tuple类型
# 调用的时候"city="不能省略
def print_three(name, *args, city):
    print(name, args, city)
