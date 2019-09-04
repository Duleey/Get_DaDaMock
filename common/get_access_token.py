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
    def __init__(self, pid, env='QA'):
        self.log = Logger("debug")

        # 判断pid
        if pid == None:
            if env == 'QA':
                self.pid = 1
            if env == 'DEV':
                self.pid = 17
            # TODO 预留prod环境
            if env == 'PROD':
                self.pid = 17
        else:
            self.pid = pid

        self.opera = OperationIni(fileName='config.ini', pathName='config')

        # 获取鉴权参数
        try:
            self.clientId = translate_env_access_token(env=env, pid=self.pid)[0]
            self.clientSecret = translate_env_access_token(env=env, pid=self.pid)[1]
        except Exception as f:
            self.log.error("获取鉴权参数失败，检查pid是否正确，错误日志：{0}".format(f))

        self.env = env
        # env字符串转小写
        self.l_env = env.lower()

        self.key = self.l_env + '_url'

        # 获取ini文件中的base_url
        base_url = self.opera.read_ini(section='access_token', key=self.key)
        self.url = base_url.format(self.clientId, self.clientSecret)

    def get_access_token(self):
        '''
        通过clientId、clientSecret参数请求鉴权接口,获取最新的access_token
        :return: access_token
        '''

        self.log.info('开始：调用access_token接口，请求地址为：{0}'.format(self.url))
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=self.url, verify=False)
        access_token = r.json()['access_token']
        self.log.info('结束：调用access_token接口，获取的access_token为：{0}'.format(access_token))
        return access_token


    def set_access_token(self):
        '''
        把最新的access_token存入ini文件,自动覆盖旧的access_token
        :return:
        '''
        key = self.l_env + '_{0}_access_token'.format(self.pid)
        access_token = self.get_access_token()
        # 保存最新获取的access_token，存入ini文件
        self.opera.write_ini(section='access_token', data=access_token, key=key)
        self.log.info('成功写入最新的access_token到ini文件中，子节点为：access_token，key为：{0}，写入的access_token为：{1}'.format(key, access_token))


    def get_ini_access_token(self):
        '''
        获取ini文件中已有的access_token
        :return:
        '''
        # 获取ini文件中已有的access_token
        access_token = get_env_access_token(env=self.env, pid=self.pid)
        self.log.info('获取到ini文件中已有的access_token为：{0}'.format(access_token))
        return access_token


# g = GetAccessToken(env='DEV', pid=17)
# print(g.set_access_token())
