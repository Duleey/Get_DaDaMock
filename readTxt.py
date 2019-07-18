#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 14:44
# @Author  : Weiqiang.long
# @Site    : 
# @File    : readTxt.py
# @Software: PyCharm


file_name = 'ip.txt'

def write_txt(data):
    # 写入txt
    with open(file_name, 'w') as file_obj:
        file_obj.write(data)
        file_obj.close()


def read_txt():
    # 打开txt
    r = open(file_name, 'r')
    f = r.read()
    r.close()
    return f

# print(write_txt('111'))
# print(read_txt())