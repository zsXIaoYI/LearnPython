# -*- coding: utf-8 -*-
# _list_slice.py
# 2020/4/28 15:54
# __author__ = 'zs'


# list可以进行切片操作,list[start:end],从start开始，不包括end
list_one = [0, 1, 2, 3, 4, 5, 6, 7]
print('第2至第5个元素:', list_one[2:5])

# 对切片的赋值会改变原来的list
list_one[2: 5] = [20, 30, 40]
print(list_one)

list2 = [3, [66, 55, 44], (7, 8, 9)]

# list3生成以了一个新的对象,对list2的操作并不会影响list3
list3 = list(list2)
list2.append(100)

print('list2:', list2)
print('list3:', list3)

# 移除55对两者都有影响，两者中的第二个list元素都指向同一个list
# list3[1] += [33, 22],也会改变list2
list2[1].remove(55)
print('after remove list2:', list2)
print('after remove list3:', list3)


# 下面操作生成了新的tuple对象，tuple的 += 操作会生成新的tuple
list3[2] += (10, 11)
print('after tuple list2:', list2)
print('after tuple list3:', list3)





