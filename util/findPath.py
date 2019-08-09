#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 16:45
# @Author  : Weiqiang.long
# @Site    : 
# @File    : findPath.py
# @Software: PyCharm


import os
from util.Logger import Logger

log = Logger("debug")

def data_dir(fileName=None,pathName='data'):
    """
    查找文件绝对路径
    :param fileName:文件名称
    :param pathName:目录名称
    :return:对应文件的绝对路径
    """
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)),pathName,fileName)
    # log.info("成功通过文件名获取到绝对路径，路径为：{0}".format(path))
    return path




def folder_data_dri(pathName='log'):
    '''
    查找文件夹绝对路径
    :param pathName: 文件夹名称
    :return: 对应文件夹的绝对路径
    '''
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)),pathName)
    # log.info("成功通过文件夹名称获取到绝对路径，路径为：{0}".format(path))
    return path

# print(data_dir(fileName='config.ini', pathName='config'))
# print(folder_data_dri(pathName='log'))



