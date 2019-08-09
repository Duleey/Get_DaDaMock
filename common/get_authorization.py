#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 12:36
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_authorization.py
# @Software: PyCharm

import requests

from util.get_disparate_env_data import get_env_authorization
from util.readTxt import OperationIni
from util.Logger import Logger

'''
获取后端token
'''
class GetAuth:
    def __init__(self, env='QA'):
        self.log = Logger("debug")
        self.opera = OperationIni(fileName='config.ini', pathName='config')
        path = '/website/saas/account/api2/user/login'
        self.key = env.lower() + '_token'
        d = get_env_authorization(env=env)
        self.url = d[0] + path
        self.cookie = d[1]
        self.userName = d[2]
        self.passWord = d[3]

        # if env == 'QA':
        #     self.url = self.opera.read_ini(section='Authorization', key='qa_url') + path
        #     self.cookie = self.opera.read_ini(section='Authorization', key='qa_cookie')
        #     self.userName = self.opera.read_ini(section='Authorization', key='qa_username')
        #     self.passWord = self.opera.read_ini(section='Authorization', key='qa_password')
        # if env == 'DEV':
        #     self.url = self.opera.read_ini(section='Authorization', key='dev_url') + path
        #     self.cookie = self.opera.read_ini(section='Authorization', key='dev_cookie')
        #     self.userName = self.opera.read_ini(section='Authorization', key='dev_username')
        #     self.passWord = self.opera.read_ini(section='Authorization', key='dev_password')

        self.headers = {'Cookie':self.cookie,'Content-Type':'application/x-www-form-urlencoded'}

    def get_auth(self):
        '''
        获取token
        :return: rsp, 登录后的token
        '''
        data = {
            'zone': '0086',
            'phone': self.userName,
            'password': self.passWord,
            'remember': False,
            'passwordType': 'new'
        }
        self.log.info('开始：调用获取B端后台token接口，请求地址为：{0}，入参为：{1}，请求头为：{2}'.format(self.url, data, self.headers))
        r = requests.post(url=self.url, data=data, headers=self.headers)
        try:
            token = r.json()['data']['token']
            self.log.info('结束：调用获取B端后台token接口，获取到token为：{0}'.format(token))
            return token, r.json()
        except Exception as f:
            self.log.error('获取B端后台token失败，错误日志为：{0}'.format(f))
            print(f)
    
    def set_auth(self):
        '''
        存储最新的后端Authorization
        :return:
        '''
        token = self.get_auth()[0]
        self.opera.write_ini(section='Authorization', data=token, key=self.key)


# g = GetAuth()
# print(g.get_auth())
