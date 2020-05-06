# -*- coding: utf-8 -*-
# demo.py
# 2020/5/5 23:16
# __author__ = 'zs'


# 实现去除首位空格
def str_trim(s):
    le = len(s)
    begin = 0
    end = le - 1
    if le == 0:
        return 'empty str'
    elif begin == end:
        return 'length is 1'
    else:
        while begin < end:
            if s[begin:begin + 1] == ' ':
                begin += 1
            elif s[end:end + 1] == ' ':
                end -= 1
            else:
                print('end....')
                break
        return s[begin:end + 1]


def find_max_and_min(param_list):
    """
    查找list中最大和最小的元素
    :param param_list:
    :return:
    """
    if not isinstance(param_list, list):
        raise TypeError('error type')
    elif len(param_list) == 0:
        raise ValueError('empty list')
    elif param_list is None:
        raise TypeError('list is None')
    ma = param_list[0]
    mi = param_list[0]
    for li in param_list:
        if li > ma:
            ma = li
        elif li < mi:
            mi = li
    return mi, ma


# 求二进制数的十进制
def binary_to_decimal(in_binary):
    res = 0
    while in_binary != '':
        res = res * 2 + (ord(in_binary[0]) - ord('0'))
        in_binary = in_binary[1:]
    return res


if __name__ == '__main__':
    s1 = '  abc '
    print(len(s1))
    s1 = str_trim(s1)
    print('after trim, s1 length:', len(s1))
    print(find_max_and_min([6, 4, 12, 3, 9, 20]))

    print('1011转10进制:', binary_to_decimal('1101'))



