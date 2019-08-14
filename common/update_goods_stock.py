#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 16:21
# @Author  : Weiqiang.long
# @Site    : 
# @File    : update_goods_stock.py
# @Software: PyCharm

import requests
from common.get_access_token import GetAccessToken
from common.get_goods_detail import GetGoodsDetail
from util.readTxt import OperationIni
from util.Logger import Logger

'''
修改商品库存
'''
class updateGoodsStock:
    def __init__(self, env='QA'):
        self.log = Logger("debug")
        opera = OperationIni(fileName='config.ini', pathName='config')
        self.get_skuId = GetGoodsDetail(env=env)
        self.get_access_token = GetAccessToken(env=env)

        # env字符串转小写
        env = env.lower()
        key = env + '_url'

        self.base_url = opera.read_ini(section='goods', key=key)
        self.path = opera.read_ini(section='goods', key='wholeUpdateStock')


        self.access_token = self.get_access_token.get_ini_access_token()

        # if env == 'QA':
        #     self.access_token = opera.read_ini(section='access_token', key='qa_access_token')
        # if env == 'DEV':
        #     self.access_token = opera.read_ini(section='access_token', key='dev_access_token')


    def update_goods_stock(self, goodsId, editStockNum, storeId=None):
        '''
        修改商品库存
        :param goodsId: 商品id
        :param editStockNum: 需要修改的库存
        :param storeId: 门店id
        :return: rsq
        '''

        url = self.base_url.format(self.path, self.access_token)
        # 获取skuId
        try:
            self.skuId = self.get_skuId.get_goods_detail(goodsId, storeId)[1]
            json_data = {
                'goodsId': goodsId,
                'storeId': storeId,
                'skuList': [
                    {
                       'skuId': self.skuId,
                        'editStockNum': editStockNum
                    }
                ]
            }
            self.log.info('开始：调用update_goods_stock方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
            requests.packages.urllib3.disable_warnings()
            r = requests.post(url=url, json=json_data, verify=False)
            # 如果access_token无效
            if r.json()['data'] == 'invalid accesstoken':
                # 获取最新的token并存入ini文件
                self.log.warning('提示：ini文件中的accesstoken失效，开始获取新的accesstoken')
                self.get_access_token.set_access_token()
                # 注意：这里一定要重新获取一次ini文件中的access_token
                new_access_token = self.get_access_token.get_ini_access_token()
                url = self.base_url.format(self.path, new_access_token)
                self.log.warning('开始：调用update_goods_stock方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
                requests.packages.urllib3.disable_warnings()
                res = requests.post(url=url, json=json_data, verify=False)
                self.log.warning('结束：调用update_goods_stock方法，返回数据为:{0}'.format(res.json()))
                return res.json()
            else:
                self.log.info('结束：调用update_goods_stock方法，返回数据为:{0}'.format(r.json()))
                return r.json()
        except Exception as f:
            self.log.error('调用获取商品详情接口失败，错误日志为：{0}'.format(f))
            return {'msg': '底层接口请求失败，请检查所传字段的数据是否正确'}


