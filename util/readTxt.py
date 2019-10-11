#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 14:44
# @Author  : Weiqiang.long
# @Site    : 
# @File    : readTxt.py
# @Software: PyCharm

import configparser
from util import findPath
from util.Logger import logger as log



class OperationIni:
    log = log

    def __init__(self, fileName='ip.ini', pathName='data'):
        self.file_name = findPath.data_dir(fileName, pathName=pathName)
        # 记录坑:如果对应ini文件中有%号的话，使用ConfigParser类会报错，所以在这里使用RawConfigParser类代替，详见下方地址
        self.config = configparser.RawConfigParser()   # https://www.itread01.com/content/1544587395.html
        self.config.read(self.file_name, encoding="utf-8")

    def write_ini(self, section, data, key='ip'):
        '''
        写入ini
        :param section: 节点
        :param data: 写入的数据
        :param key: 要写入数据的key
        :return:
        '''
        try:
            self.config.set(section, key, data)
            self.config.write(open(self.file_name, "w"))
            # self.log.info("成功将数据写入ini文件,子节点为:{0},key为:{1},写入的数据为:{2}".format(section, key, data))
        except Exception as f:
            self.log.error('找不到对应的key,错误信息为:{0}'.format(f))
            return '找不到对应的key,错误信息为:{0}'.format(f)

    def read_ini(self, section, key="ip"):
        '''
        打开ini
        :param section: 要获取的数据的节点
        :param key: 要获取的数据的key
        :return:
        '''
        try:
            # self.log.info('开始读取ini文件中的数据,子节点为:{0},key为:{1}'.format(section, key))
            db = self.config.get(section, key)
            # self.log.info("成功获取到ini文件中的数据,子节点为:{0},key为:{1},获取到的数据为:{2}".format(section, key, db))
            return db
        except Exception as f:
            self.log.error('找不到对应的key,错误信息为:{0}'.format(f))
            return '找不到对应的key,错误信息为:{0}'.format(f)

# opera = OperationIni(fileName='config.ini', pathName='config')
# print(opera.write_ini('DEV','127.0.0.2'))
# print(opera.read_ini(key='access_token', data='url'))

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

