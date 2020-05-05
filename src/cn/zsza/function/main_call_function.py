# -*- coding: utf-8 -*-
# main_call_function.py
# 2020/5/5 18:01
# __author__ = 'zs'

from cn.zsza.function.my_function import *

print(my_abs(12))
# 返回结果为tuple类型
print(move(2, 3, 5))
print(move(2, 3, 5, math.pi / 6))  # 传参加上默认参数
print('4的平方:', power(4))

print('4的3次方:', power_n(4, 3))

print(add_end())  # 返回['end']
print(add_end())  # 在调用第二次将返回['end', 'end']

# 如下方法不管调用多少次,都只返回['end']
print(add_end_none())

# 求nums中所有元素的平方和
nums = [1, 2, 3]
print(calc(nums))

# 传入的2, 3, 4为可变参数
print(calc_2(2, 3, 4))
# nums是一个list,作为一个可变参数传入calc_2()方法中,记住*不能省略
print(calc_2(*nums))

# 带有关键字参数的函数调用
print_one('小A', 18, city='Beijing')
# 如下调用,双星号不能省略
extra = {'city': 'bj', 'job': 'engineer'}
print_one('Amy', 20, **extra)

print_two('Jack', city='Tokyo', job='Engineer')

print_three('John', 'hobby', 'running', city='London')
