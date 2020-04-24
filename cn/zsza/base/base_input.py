# -*- coding: utf-8 -*-
# base_input.py
# 2020/4/24 21:26
# __author__ = 'zs'

#  input返回的类型是字符串，不能直接和整型比较

# 摄氏温度和华氏温度的转换
# F = 1.8C + 32

f = float(input('请输入华摄氏度:\n'))
c = (f - 32) / 1.8

print('%.1f华摄氏度=%.1f摄氏度' % (f, c))

"""
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
x = float(input('x: \n'))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3

print('f(%.2f) = %.2f' % (x, y))
