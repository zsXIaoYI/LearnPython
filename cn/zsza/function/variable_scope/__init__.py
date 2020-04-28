# -*- coding: utf-8 -*-
# __init__.py.py
# 2020/4/25 18:46
# __author__ = 'zs'


# 1、变量的作用域指的是变量的有效范围
# 2、在Python中,没有块级作用域,比如if语句、for语句、with上下文等是不存在作用域的,
#  这和Java是不一样的,如下面示例代码,x在if代码块后,仍可以被访问到
"""
if True:
    x = 2
    print(x)
print('x:', x)
"""
# 3、函数是有作用域的,在函数内部定义的局部变量,在函数外面是访问不到的
# 4、Python作用域一共分为4层,查找的时候先从L查起
#  L （Local） 局部作用域
#  E （Enclosing） 闭包函数外的函数中
#  G （Global） 全局作用域
#  B （Built-in） 内建作用域


def func(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    return a + b
