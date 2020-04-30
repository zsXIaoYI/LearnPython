# -*- coding: utf-8 -*-
# _generator.py
# 2020/4/28 15:10
# __author__ = 'zs'

# 列表生成式

g1 = (x ** 2 for x in range(1, 3))
print(g1)   # g1返回列表生成式对象

# 可以通过next()函数获得generator对象的下一个值
# 当迭代到最后一个元素,再次调用next()函数时,则会报StopIteration
print(next(g1))
print(next(g1))


