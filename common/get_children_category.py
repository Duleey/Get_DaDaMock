#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 15:41
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_children_category.py
# @Software: PyCharm
# @Description: 查询商品类目
import requests

from common.get_access_token import GetAccessToken
from util.Logger import logger as log
from util.readTxt import OperationIni


class getChildrenCategory:
    def __init__(self, pid, env='QA'):
        self.log = log
        self.opera = OperationIni(fileName='config.ini', pathName='config')
        self.get_access_token = GetAccessToken(env=env, pid=pid)

        # env字符串转小写
        env = env.lower()
        key = env + '_url'

        self.base_url = self.opera.read_ini(section='goods', key=key)
        self.path = self.opera.read_ini(section='goods', key='queryChildrenCategory')

        self.access_token = self.get_access_token.get_ini_access_token()


    def get_children_category(self, categoryId):
        '''
        查询商品类目
        :param categoryId: 一级类目id
        :return:
        '''

        url = self.base_url.format(self.path, self.access_token)
        json_data = {'categoryId': categoryId}

        self.log.info('开始：调用get_children_category方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url, json=json_data, verify=False)
        # 如果access_token无效
        if r.json()['data'] == 'invalid accesstoken':
            self.log.warning('提示：ini文件中的accesstoken失效，开始获取新的accesstoken')
            # 获取最新的token并存入ini文件
            self.get_access_token.set_access_token()
            # 注意：这里一定要重新获取一次ini文件中的access_token
            new_access_token = self.get_access_token.get_ini_access_token()
            url = self.base_url.format(self.path, new_access_token)
            self.log.warning('开始：调用update_goods_price方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
            requests.packages.urllib3.disable_warnings()
            res = requests.post(url=url, json=json_data, verify=False)
            self.log.warning('结束：调用get_children_category方法，返回数据为:{0}'.format(res.json()))
            return res.json()
        else:
            self.log.info('结束：调用get_children_category方法，返回数据为:{0}'.format(r.json()))
            return r.json()

if __name__ == '__main__':
    g = getChildrenCategory(pid=3, env='QA')
    print(g.get_children_category(categoryId=0))
