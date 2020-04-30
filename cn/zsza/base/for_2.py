# -*- coding: utf-8 -*-
# for_2.py
# 2020/4/28 14:33
# __author__ = 'zs'

symbols = 'ABD'
codes = []
for sym in symbols:
    codes.append(ord(sym))    # ord函数,求字符的ASCII码值
print('codes:', codes)

# 上述代码也可以写成如下
code2 = [ord(sym) for sym in symbols]
print('code2:', code2)

# 在上述基础上添加过滤
code3 = [ord(sym) for sym in symbols if ord(sym) > 65]
print('code3:', code3)

# 用lambda表达式处理
code4 = list(filter(lambda c: c > 65, map(ord, symbols)))
print('code4:', code4)

# 笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
t_shirts = [(color, size) for color in colors for size in sizes]
print('t_shirts:', t_shirts)


# 用生成器表达式之后，内存里不会留下一个有6个组合的列表，因为生成器表达式会在
# 每次for循环运行时才产生一个组合
for t_shirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    # t_shirt为字符串
    print('t_shirt:', t_shirt)

# for循环可以分别提取元组里的元素，也叫作拆包(unpacking)
# 因为元组中第二个元素对我们没有什么用，所以它赋值给"_"占位符
country = [('China', '北京'), ('Japan', '东京'), ('SK', '首尔')]
country_list = []
for cy, _ in country:
    country_list.append(cy)
print('country_list:', country_list)

L6 = [m + n for m in 'ABC' for n in 'XY']
print('L6:', L6)

suits = 'spades diamonds clubs hearts'.split()
print(suits)
