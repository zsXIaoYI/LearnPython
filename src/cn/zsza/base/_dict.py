# -*- coding: utf-8 -*-
# _dict.py
# 2020/4/24 21:45
# __author__ = 'zs'

# dict学习
# Python内置了dict, 和Java中的Map类似，如果查找的key不存在，则报KeyError
# 正确使用dict非常重要,需要牢记的第一条就是dict的key必须是不可变对象
# 在Python中，字符串、整数都是不可变的

d = {'Jack': 18, 'Amy': 23}
# 用如下方式得到key所对应的value，如果key不存在的话，则报KeyError
print('Jack年龄:', d['Jack'])
print('Amy年龄:', d.get('Amy'))
print('d的长度:', len(d))

# 如下类似于java中的Map的put操作
d['May'] = 25
print('新的dict:', d)
print('May的年龄:', d['May'])

# 如果key存在，则返回该key对应的值；如果key不存在，则返回设定的value
print(d.get('May', 28))

# 判断key是否存在有两种方法
# 1、用in关键字
is_exist = 'David' in d
print('is_exist:', is_exist)

# 2、用get方法，不存在则返回None
res = d.get('Jenny')
print('Jenny是否存在:', res)
print(res is None)

# pop删除dict中的一个键值对，并返回value
v = d.pop('Jack')
print('pop的值:', v)
print('after pop:', d)

print('**************dict迭代*************')

d1 = {'city': '北京', 'area': 200}
# 迭代key
for key in d1.keys():
    print('key:', key)
# 迭代键值对
for key, value in d1.items():
    print('{} : {}'.format(key, value))

# item是tuple类型
for item in d1.items():
    print(item)

