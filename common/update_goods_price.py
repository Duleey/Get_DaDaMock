#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 19:48
# @Author  : Weiqiang.long
# @Site    : 
# @File    : update_goods_price.py
# @Software: PyCharm

import requests
from common.get_goods_detail import GetGoodsDetail
from util.readTxt import OperationIni
from common.get_access_token import GetAccessToken
from util.Logger import Logger

'''
修改商品价格
'''
class updateGoodsPrice:
    def __init__(self, env='QA'):
        self.log = Logger("debug")
        self.opera = OperationIni(fileName='config.ini', pathName='config')
        self.get_skuId = GetGoodsDetail(env=env)
        self.get_access_token = GetAccessToken(env=env)

        # env字符串转小写
        env = env.lower()
        key = env + '_url'

        self.base_url = self.opera.read_ini(section='goods', key=key)
        self.path = self.opera.read_ini(section='goods', key='updatePrice')

        self.access_token = self.get_access_token.get_ini_access_token()


    def update_goods_price(self, storeId, goodsId, originalPrice, salePrice):
        '''
        修改商品价格
        :param storeId: 门店id
        :param goodsId: 商品id
        :param originalPrice: 市场价
        :param salePrice: 商家统一价
        :return: rsq
        '''

        url = self.base_url.format(self.path, self.access_token)

        # 获取skuId
        try:
            self.skuId = self.get_skuId.get_goods_detail(goodsId, storeId)[1]
            json_data = {
                'goodsId': goodsId,
                'skuList': [
                    {
                        'skuId': self.skuId,
                        'originalPrice': originalPrice,
                        'salePrice': salePrice,
                    }
                ],
                'storeId': storeId
            }

            self.log.info('开始：调用update_goods_price方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
            r = requests.post(url=url, json=json_data)
            # 如果access_token无效
            if r.json()['data'] == 'invalid accesstoken':
                self.log.warning('提示：ini文件中的accesstoken失效，开始获取新的accesstoken')
                # 获取最新的token并存入ini文件
                self.get_access_token.set_access_token()
                # 注意：这里一定要重新获取一次ini文件中的access_token
                new_access_token = self.get_access_token.get_ini_access_token()
                url = self.base_url.format(self.path, new_access_token)
                self.log.warning('开始：调用update_goods_price方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
                res = requests.post(url=url, json=json_data)
                self.log.warning('结束：调用update_goods_price方法，返回数据为:{0}'.format(res.json()))
                return res.json()
            else:
                self.log.info('结束：调用update_goods_price方法，返回数据为:{0}'.format(r.json()))
                return r.json()
        except Exception as f:
            self.log.error('修改商品失败，错误日志为：{0}'.format(f))
            return {'msg': '底层接口请求失败，请检查所传字段的数据是否正确'}


# g = updateGoodsPrice()
# print(g.update_goods_price())

