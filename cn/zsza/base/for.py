# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/11/27 下午3:18

# for循环
stu = ['Jack', 'Honey', 'Amy']
for name in stu:
    print(name)

# 计算List中所有元素的和
total = 0
for x in [1, 2, 3, 4, 5]:
    total += x
print('total:', total)

sn = 0
for i in range(101):
    sn += i
print(sn)

# 计算小于9的奇数之和
res = 0
n = 9
while n > 0:
    res += n
    n = n - 2
print('res:', res)

# break语句
n1 = 1
while n1 < 100:
    if n1 > 10:
        break
    print('n1:', n1)
    n1 += 1
print('END')

# continue语句
n2 = 0
while n2 < 10:
    n2 += 1
    if n2 % 2 == 0:
        continue
    print('n2:', n2)
