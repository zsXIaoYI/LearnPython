# -*- coding: utf-8 -*-
# advanced_list_dict.py
# 2020/4/24 22:27
# __author__ = 'zs'

# list和dict的一些高级操作
# DIAL_CODES是一个list，其元素为一个个tuple
DIAL_CODES = [(86, 'China'), (91, 'India'), (36, 'Brazil')]
country_code = {country: code for code, country in DIAL_CODES}
print('country_code:', country_code)

new_country_code = {code: country.upper() for country, code in country_code.items() if code > 50}
print('new_country_code:', new_country_code)
