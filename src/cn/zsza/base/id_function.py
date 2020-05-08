# -*- coding: utf-8 -*-
# id_function.py
# 2020/5/8 15:34
# __author__ = 'zs'

# Python中小整数的范围为[-5, 256],但PyCharm对小整数范围范围做了
# 进一步扩大和优化,如下的代码,在Python Shell中与在PyCharm运行结果是不一样的
a = 1000
b = 1000

print(a is b)  # 返回True
print(id(a), id(b))
