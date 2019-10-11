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
from util.Logger import logger as log

'''
获取后端token
'''
class GetAuth:
    def __init__(self, env='QA'):
        self.log = log
        self.opera = OperationIni(fileName='config.ini', pathName='config')
        self.key = env.lower() + '_token'
        d = get_env_authorization(env=env)
        self.base_url = d[0]
        # self.cookie = d[1]
        self.userName = d[2]
        self.passWord = d[3]

    def get_platform_cookies(self):
        '''
        获取b端cookies
        :return: cookie
        '''
        _path = '/website/saas/account/api2/user/getCodeRs'
        _url = self.base_url + _path
        _data = {'zone': '0086','phoneNumber': self.userName,'pagename': 'login'}
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=_url, data=_data, verify=False)
        # getCodeRs返回的cookies
        _cookies = r.cookies['saas.console.session']
        # 组装cookie
        _cookie = {"saas.console.session": _cookies}
        return _cookie

    def get_platform_token(self):
        '''
        获取后台token
        :return: rsp, 登录后的token
        '''
        path = '/website/saas/account/api2/user/login'
        url = self.base_url + path
        cookies = self.get_platform_cookies()
        data = {
            'zone': '0086',
            'phone': self.userName,
            'password': self.passWord
        }
        self.log.info('开始：调用获取B端后台token接口，请求地址为：{0}，入参为：{1}，请求头为：{2}'.format(url, data, cookies))
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url, data=data, cookies=cookies, verify=False)
        try:
            token = r.json()['data']['token']
            self.log.info('结束：调用获取B端后台token接口，获取到token为：{0}'.format(token))
            return token, r.json()
        except Exception as f:
            self.log.error('获取B端后台token失败，错误日志为：{0}'.format(f))
            print(f)
    
    def set_token(self):
        '''
        存储最新的后端token
        :return:
        '''
        token = self.get_platform_token()[0]
        self.opera.write_ini(section='Authorization', data=token, key=self.key)


# g = GetAuth(env='DEV')
# print(g.get_platform_token())
# g.set_token()
