#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 13:00
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_access_token.py
# @Software: PyCharm

import requests
from util.get_disparate_env_data import translate_env_access_token, get_env_access_token
from util.readTxt import OperationIni
from util.Logger import Logger

'''
获取access_token
'''
class GetAccessToken:
    def __init__(self, env='QA'):
        self.log = Logger("debug")

        self.opera = OperationIni(fileName='config.ini', pathName='config')

        # 获取鉴权参数
        self.clientId = translate_env_access_token(env=env)[0]
        self.clientSecret = translate_env_access_token(env=env)[1]

        self.env = env
        # env字符串转小写
        self.l_env = env.lower()

        self.key = self.l_env + '_url'

        # 获取ini文件中的base_url
        base_url = self.opera.read_ini(section='access_token', key=self.key)
        self.url = base_url.format(self.clientId, self.clientSecret)


        # if env == 'DEV':
        #     self.clientId = self.opera.read_ini(section='access_token', key='dev_clientId')
        #     self.clientSecret = self.opera.read_ini(section='access_token', key='dev_clientSecret')
        #     self.access_token = self.opera.read_ini(section='access_token', key='dev_access_token')
        # if env == 'QA':
        #     self.clientId = self.opera.read_ini(section='access_token', key='qa_clientId')
        #     self.clientSecret = self.opera.read_ini(section='access_token', key='qa_clientSecret')
        #     self.access_token = self.opera.read_ini(section='access_token', key='qa_access_token')

    def get_access_token(self):
        '''
        通过clientId、clientSecret参数请求鉴权接口,获取最新的access_token
        :return: access_token
        '''

        self.log.info('开始：调用access_token接口，请求地址为：{0}'.format(self.url))

        r = requests.post(url=self.url)
        access_token = r.json()['access_token']
        self.log.info('结束：调用access_token接口，获取的access_token为：{0}'.format(access_token))
        return access_token


    def set_access_token(self):
        '''
        把最新的access_token存入ini文件,自动覆盖旧的access_token
        :return:
        '''
        key = self.l_env + '_access_token'
        access_token = self.get_access_token()
        # 保存最新获取的access_token，存入ini文件
        self.opera.write_ini(section='access_token', data=access_token, key=key)
        self.log.info('成功写入最新的access_token到ini文件中，子节点为：access_token，key为：{0}，写入的access_token为：{1}'.format(access_token,key))


    def get_ini_access_token(self):
        '''
        获取ini文件中已有的access_token
        :return:
        '''
        # 获取ini文件中已有的access_token
        access_token = get_env_access_token(env=self.env)
        self.log.info('获取到ini文件中已有的access_token为：{0}'.format(access_token))
        return access_token


# g = GetAccessToken(env='DEV')
# print(g.set_access_token())
