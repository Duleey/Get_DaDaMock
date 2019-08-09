#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 18:09
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_disparate_env_data.py
# @Software: PyCharm

from util.readTxt import OperationIni


opera = OperationIni(fileName='config.ini', pathName='config')

def get_env_access_token(env):
    '''
    通过不同的env来获取不同的access_token
    :param env: 环境
    :return: 返回不同环境的access_token
    '''
    access_token = None

    if env == 'QA':
        opera = OperationIni(fileName='config.ini', pathName='config')
        access_token = opera.read_ini(section='access_token', key='qa_access_token')
    if env == 'DEV':
        # 大坑：一定要在每个if中重新调用读取ini文件的方法，要不然读取的内容不是最新的
        opera = OperationIni(fileName='config.ini', pathName='config')
        access_token = opera.read_ini(section='access_token', key='dev_access_token')

    return access_token


def get_env_authorization(env):
    '''
    通过不同的env来过去不同的ini文件中authorization节点中的数据
    :param env: 环境
    :return: 返回不同环境ini文件中authorization节点中的数据（url, cookie, userName, passWord）
    '''

    url = None
    cookie = None
    userName = None
    passWord = None

    if env == 'QA':
        url = opera.read_ini(section='Authorization', key='qa_url')
        cookie = opera.read_ini(section='Authorization', key='qa_cookie')
        userName = opera.read_ini(section='Authorization', key='qa_username')
        passWord = opera.read_ini(section='Authorization', key='qa_password')
    if env == 'DEV':
        url = opera.read_ini(section='Authorization', key='dev_url')
        cookie = opera.read_ini(section='Authorization', key='dev_cookie')
        userName = opera.read_ini(section='Authorization', key='dev_username')
        passWord = opera.read_ini(section='Authorization', key='dev_password')

    # return多个数据时，类型为tuple
    return url, cookie, userName, passWord


def translate_env_access_token(env):
    '''
    通过不同的env从ini文件拿到对应的clientId、clientSecret
    :param env: 环境
    :return: clientId, clientSecret
    '''

    clientId = None
    clientSecret = None

    if env == 'DEV':
        clientId = opera.read_ini(section='access_token', key='dev_clientId')
        clientSecret = opera.read_ini(section='access_token', key='dev_clientSecret')
        # access_token = opera.read_ini(section='access_token', key='dev_access_token')
    if env == 'QA':
        clientId = opera.read_ini(section='access_token', key='qa_clientId')
        clientSecret = opera.read_ini(section='access_token', key='qa_clientSecret')
        # access_token = opera.read_ini(section='access_token', key='qa_access_token')

    return clientId, clientSecret

# print(get_env_access_token(env='DEV'), type(get_env_access_token(env='DEV')))
