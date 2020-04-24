# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/11/28 下午9:26

# set类似于Java中的HashSet
# 多次对一个key放入value,会覆盖之前的value
# 在Python中，字符串、整数都是不可变的

print('>>>>>>>>>>>>>>>>>> set集合 <<<<<<<<<<<<<<<<<<<\n')
# set集合元素不能重复,要创建一个set，需要提供一个list作为输入集合
# 1、可以用add()方法添加元素
# 2、可以用remove()方法删除元素
s = set([1, 2, 4])
print('s:', s)

s.add(3)
print('after add s:', s)

s.remove(4)
print('after remove s:', s)

# set集合可以做交集和并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print('s1于s2的交集:', s1 & s2)
print('s1与s2的并集:', s1 | s2)

# list作为一个参数传入update方法，合并成一个新的set
s1.update([3, 5])
print('after update:', s1)

# Python中dict的key不支持list或dict类型，因为list和dict类型是unhashable的
# 因为Python的list和dict都是可变对象，可以动态地添加或删除元素,以下两行代码会报unhashable type: 'list'
# _s2 = set([(1, 2, [1, 2]), (2, 3, [6, 8])])
# print('_s2:', _s2)

_s1 = set([(1, 2, 3), (2, 3, 4)])
print('_s1:', _s1)


