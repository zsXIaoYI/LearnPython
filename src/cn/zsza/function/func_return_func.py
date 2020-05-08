# -*- coding: utf-8 -*-
# func_return_func.py
# 2020/5/8 16:54
# __author__ = 'zs'


# python函数支持函数返回函数操作
def print_msg():
    msg = ' the function of python'

    def printer(inner_str):
        print(inner_str + msg)

    return printer


def adder(x):
    def inner_add(y):
        return x + y
    return inner_add


if __name__ == '__main__':
    # 调用print_msg(),返回一个函数对象
    func = print_msg()
    print(func)

    # 调用func函数,并传入参数:Test:
    func('Test:')
    # 所有函数都有一个 __closure__属性,如果这个函数是一个闭包的话,那么它返回的是一个
    # 由cell对象组成的元组
    print(func.__closure__[0].cell_contents)
    # 下面将打印5
    print(adder(5).__closure__[0].cell_contents)
