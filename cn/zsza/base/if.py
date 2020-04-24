# -*- coding: utf-8 -*-
# if.py
# 2020/4/24 21:06
# __author__ = 'zs'


x = 1
# if语句没有作用域,所以最下面的print(z)仍然可以访问到if和else中的z
if x > 3:
    z = 2
else:
    z = 12
print(z)

age = int(input('输入你的年龄:'))
if age >= 18:
    print('adult!')
elif age >= 12:
    print('teenager!')
else:
    print('child')

# 只要x是非零数值、非空字符、非空list，就判断为True
x = 1
if x:
    print(True)
