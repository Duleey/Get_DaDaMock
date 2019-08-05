#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 14:44
# @Author  : Weiqiang.long
# @Site    : 
# @File    : readTxt.py
# @Software: PyCharm

import configparser

class OperationIni:

    def __init__(self):
        self.file_name = 'ip.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.file_name)

    def write_ini(self, env, data):
        # 写入ini
        self.config.set(env, 'ip', data)
        self.config.write(open(self.file_name, "w"))

    def read_ini(self, env, data="ip"):
        # 打开ini
        ip = self.config.get(env, data)
        return ip

# file_name = 'ip.txt'

# def write_txt(data):
#     # 写入txt
#     with open(file_name, 'w') as file_obj:
#         file_obj.write(data)
#         file_obj.close()


# def read_txt():
#     # 打开txt
#     r = open(file_name, 'r')
#     f = r.read()
#     r.close()
#     return f


# print(write_txt('111'))
# print(read_txt())

# opera = OperationIni()
# print(opera.write_ini('DEV','127.0.0.2'))
# print(opera.read_ini('DEV'))