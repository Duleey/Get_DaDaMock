#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 15:43
# @Author  : Weiqiang.long
# @Site    : 
# @File    : update_store_goods_delivery_type.py
# @Software: PyCharm

import requests
from common.get_access_token import GetAccessToken
from util.get_delivery_type import get_delivery_type
from util.readTxt import OperationIni
from util.Logger import Logger

'''
修改门店下商品的配送属性
'''
class updateStoreGoodsDeliveryType:
    def __init__(self, pid, env='QA'):
        self.log = Logger("debug")
        opera = OperationIni(fileName='config.ini', pathName='config')
        self.get_access_token = GetAccessToken(env=env, pid=pid)

        self.pid = pid
        self.env = env

        # env字符串转小写
        env = env.lower()
        key = env + '_url'

        self.base_url = opera.read_ini(section='goods', key=key)
        self.path = opera.read_ini(section='goods', key='updateStoreGoodsDeliveryType')
        self.access_token = self.get_access_token.get_ini_access_token()

    def update_store_goods_delivery_type(self, goodsIdList, deliveryType, storeId=None):
        '''
        修改门店下商品的配送属性
        :param goodsIdList: 商品id，str类型
        :param deliveryType: 配送类型，传1或2
        :param storeId: 门店id
        :return: rsq
        '''
        url = self.base_url.format(self.path, self.access_token)
        # 把goodsIdList中的多个goodsId转成list类型，并保证list中的元素类型为int
        goodsIdLists = list(map(int, goodsIdList.split(',')))

        # 获取配送Id
        delivery_id = get_delivery_type(pid=self.pid, env=self.env, storeId=storeId, deliveryType=deliveryType)[1]

        try:
            json_data = {
                "goodsIdList": goodsIdLists,
                "deliveryId": delivery_id,
                "storeId":storeId
            }

            self.log.info('开始：调用update_store_goods_delivery_type方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
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
                self.log.warning('开始：调用update_store_goods_delivery_type方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
                requests.packages.urllib3.disable_warnings()
                res = requests.post(url=url, json=json_data, verify=False)
                self.log.warning('结束：调用update_store_goods_delivery_type方法，返回数据为:{0}'.format(res.json()))
                return res.json()
            else:
                self.log.info('结束：调用update_store_goods_delivery_type方法，返回数据为:{0}'.format(r.json()))
                return r.json()
        except Exception as f:
            self.log.error('调用获取商品详情接口失败，错误日志为：{0}'.format(f))
            return {'msg': '底层接口请求失败，请检查所传字段的数据是否正确'}

# u = updateStoreGoodsDeliveryType(pid=1,env='QA')
# print(u.update_store_goods_delivery_type(goodsIdList='172700101',deliveryType=2,storeId=2001))

