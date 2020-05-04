# -*- coding: utf-8 -*-
# _list.py
# 2020/4/28 15:32
# __author__ = 'zs'

# >>>>>>>>>>>>>>>>Python中的list学习<<<<<<<<<<<<<<<<<<
# list是一个可变的有序列表，类似于Java中的list
# list可用-1位置取最后一个元素
# reverse():逆序排列

stu = ['Amy', 'Jack', 'Bob']
print('stu:', stu)

l1 = len(stu)
print('list的长度:', l1)

# list中可以按下标进行数组的访问,当索引超出范围时，Python会报一个IndexError
st1 = stu[0]
print('stu中第一个学生:', st1)

st_last = stu[-1]
print('stu中最后一个学生:', st_last)

stu.append('Honey')
print('追加后的stu:', stu)

# 在指定位置插入元素
stu.insert(1, 'David')
print('在指定位置插入元素后:', stu)

# 删除list末尾的元素,并返回该元素
stu_pop = stu.pop()
print('pop:', stu_pop)
print('after pop() stu:', stu)

# pop()可以删除指定位置的元素
p1 = stu.pop(1)
print('删除位置1上的元素:', p1)
print(stu)

print('************************\n')

stu_1 = ['Amy', 'Jack', 'Bob']
stu_1[0] = 'Star'    # 可以替换指定位置上的元素
print('替换后的stu_1:', stu_1)

# list中的元素类型可以不同
L1 = ['Apple', 123, True]
print(L1)

# list中还可以嵌套一个子list
L2 = ['java', ['php', 'C++'], '.Net']
print('L2', L2)
print('L2的长度:', len(L2))  # L2的长度为3

empty_L = []   # 声明一个空的list,其长度为0

_L4 = ['Hello', 'Apple', 18, 'World', None]
# 过滤出上述list中的字符串，并并字符串都改成小写，最后组装成一个新的list
_L5 = [i.lower() for i in _L4 if isinstance(i, str)]
print('过滤后:', _L5)

print(['-' * 3 for i in range(3)])
