# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2020/4/24 17:16

print(type(2 ** 64))


# 打印小小九
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = %d\t' % (i, j, i*j), end='')
    print()
