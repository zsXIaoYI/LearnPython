# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/6/20 下午5:34


# write函数
# a为追加,如果要写入的文件不存在,则会创建
with open('prime.txt', 'a', encoding='utf-8') as f:
    f.write('美利坚合众国\n')
    for num in range(2, 10):
        f.write(str(num) + '\n')
print('写入完成')

