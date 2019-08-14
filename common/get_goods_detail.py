#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 13:39
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_goods_detail.py
# @Software: PyCharm

import requests
from common.get_access_token import GetAccessToken
from util.readTxt import OperationIni
from util.Logger import Logger

'''
获取商品详情
'''
class GetGoodsDetail:
    def __init__(self, env='QA'):
        self.log = Logger("debug")
        opera = OperationIni(fileName='config.ini', pathName='config')
        self.env = env
        self.get_access_token = GetAccessToken(env=env)

        # env字符串转小写
        env = env.lower()
        key = env + '_url'
        self.url = opera.read_ini(section='goods', key=key)
        self.path = opera.read_ini(section='goods', key='queryGoodsDetail')

        self.access_token = self.get_access_token.get_ini_access_token()

        # if env == 'QA':
        #     self.access_token = opera.read_ini(section='access_token', key='qa_access_token')
        # if env == 'DEV':
        #     self.access_token = opera.read_ini(section='access_token', key='dev_access_token')


    def get_goods_detail(self, goodsId, storeId=None):
        '''
        获取商品详情
        :param goodsId: 商品id
        :param storeId: 门店id
        :return: rsq, 商品skuId
        '''
        url = self.url.format(self.path, self.access_token)
        # json_data = None
        if storeId == None:
            json_data = {'goodsId': goodsId}
        else:
            json_data = {'goodsId': goodsId, 'storeId': storeId}

        self.log.info('开始：调用get_goods_detail方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url, json=json_data, verify=False)
        # 如果access_token无效
        if r.json()['data'] == 'invalid accesstoken':
            # 获取最新的token并存入ini文件
            self.log.warning('提示：ini文件中的accesstoken失效，开始获取新的accesstoken')
            self.get_access_token.set_access_token()
            # 注意：这里一定要重新获取一次ini文件中的access_token
            new_access_token = self.get_access_token.get_ini_access_token()
            self.log.warning('开始：调用get_goods_detail方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
            url = self.url.format(self.path, new_access_token)
            requests.packages.urllib3.disable_warnings()
            res = requests.post(url=url, json=json_data, verify=False)
            # print(res.json(), url, json_data)
            try:
                skuId = res.json()['data']['goods']['skuList'][0]['skuId']
                self.log.warning('结束：调用get_goods_detail方法，返回数据为:{0}，返回skuId为：{1}'.format(res.json(), skuId))
                return res.json(), skuId
            except Exception as f:
                # print(f)
                self.log.error('调用获取商品详情接口失败，错误日志为：{0}'.format(f))
                # return {'msg': '底层接口请求失败，请检查所传字段的数据是否正确'}
                return res.json()

        elif r.json()['code']['errmsg'] == '根据Pid查询storeId失败,此商家不存在此门店':
            # print(r.json()['code']['errmsg'])
            # return r.json()['code']['errmsg']
            # 获取最新的token并存入ini文件
            self.log.warning('提示：根据Pid查询storeId失败,此商家不存在此门店，尝试开始获取新的accesstoken')
            self.get_access_token.set_access_token()
            # 注意：这里一定要重新获取一次ini文件中的access_token
            new_access_token = self.get_access_token.get_ini_access_token()
            url = self.url.format(self.path, new_access_token)
            self.log.warning('开始：调用get_goods_detail方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
            requests.packages.urllib3.disable_warnings()
            res = requests.post(url=url, json=json_data, verify=False)
            # print(res.json(), url, json_data)
            try:
                skuId = res.json()['data']['goods']['skuList'][0]['skuId']
                self.log.warning('结束：调用get_goods_detail方法，返回数据为:{0}，返回skuId为：{1}'.format(res.json(), skuId))
                return res.json(), skuId
            except Exception as f:
                # print(f)
                self.log.error('调用获取商品详情接口失败，错误日志为：{0}'.format(f))
                # return {'msg': '底层接口请求失败，请检查所传字段的数据是否正确'}
                return res.json()

        else:
            try:
                skuId = r.json()['data']['goods']['skuList'][0]['skuId']
                self.log.info('结束：调用get_goods_detail方法，返回数据为:{0}，返回skuId为：{1}'.format(r.json(), skuId))
                return r.json(), r.json()['data']['goods']['skuList'][0]['skuId']
            except Exception as f:
                # print(f)
                self.log.error('调用获取商品详情接口失败1，错误日志为：{0}'.format(f))
                # return {'msg': '底层接口请求失败，请检查所传字段的数据是否正确'}
                return r.json()




# g = GetGoodsDetail(env='DEV')
# print(g.get_goods_detail('125950117','305017'))
