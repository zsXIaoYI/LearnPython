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

