#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 18:09
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_disparate_env_data.py
# @Software: PyCharm

from util.readTxt import OperationIni


opera = OperationIni(fileName='config.ini', pathName='config')

def get_env_access_token(env, pid):
    '''
    通过不同的env来获取不同的access_token
    :param env: 环境
    :param pid: 商家id
    :return: 返回不同环境的access_token
    '''

    if pid == None:
        if env == 'QA':
            pid = 1
        if env == 'DEV':
            pid = 17
        # TODO 预留prod环境
        if env == 'PROD':
            pid = 17

    access_token = None
    if env == 'QA':
        opera = OperationIni(fileName='config.ini', pathName='config')
        access_token = opera.read_ini(section='access_token', key='qa_{0}_access_token'.format(pid))
    if env == 'DEV':
        # 大坑：一定要在每个if中重新调用读取ini文件的方法，要不然读取的内容不是最新的
        opera = OperationIni(fileName='config.ini', pathName='config')
        access_token = opera.read_ini(section='access_token', key='dev_{0}_access_token'.format(pid))
    if env == 'PROD':
        opera = OperationIni(fileName='config.ini', pathName='config')
        access_token = opera.read_ini(section='access_token', key='prod_{0}_access_token'.format(pid))

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


def translate_env_access_token(env, pid):
    '''
    通过不同的env从ini文件拿到对应的clientId、clientSecret
    :param env: 环境
    :param pid: 商家id
    :return: clientId, clientSecret
    '''
    if pid == None:
        if env == 'QA':
            pid = 1
        if env == 'DEV':
            pid = 17
        # TODO 预留prod环境
        if env == 'PROD':
            pid = 17

    clientId = None
    clientSecret = None
    if env == 'DEV':
        clientId = opera.read_ini(section='access_token', key='dev_{0}_clientId'.format(pid))
        clientSecret = opera.read_ini(section='access_token', key='dev_{0}_clientSecret'.format(pid))
        # access_token = opera.read_ini(section='access_token', key='dev_access_token')
    if env == 'QA':
        clientId = opera.read_ini(section='access_token', key='qa_{0}_clientId'.format(pid))
        clientSecret = opera.read_ini(section='access_token', key='qa_{0}_clientSecret'.format(pid))
        # access_token = opera.read_ini(section='access_token', key='qa_access_token')
    if env == 'PROD':
        clientId = opera.read_ini(section='access_token', key='prod_{0}_clientId'.format(pid))
        clientSecret = opera.read_ini(section='access_token', key='prod_{0}_clientSecret'.format(pid))

    return clientId, clientSecret

def get_env_config(section, key, env=None):
    '''
    获取config.ini文件中的配置数据
    :param env: 环境
    :param section: 节点
    :param key: key
    :return: 对应配置数据
    '''
    if env == None:
        config_data = opera.read_ini(section=section, key=key)
        return config_data
    else:
        # 环境转小写
        lower_env = env.lower()
        config_data = opera.read_ini(section=section, key='{0}_{1}'.format(lower_env, key))
        return config_data

# print(get_env_config(section='Oms', key='username'))
# print(get_env_config(env='QA', section='access_token', key='url'))

# print(translate_env_access_token(env='QA', pid=2), type(get_env_access_token(env='DEV', pid=2)))
