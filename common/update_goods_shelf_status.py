#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 20:24
# @Author  : Weiqiang.long
# @Site    : 
# @File    : update_goods_shelf_status.py
# @Software: PyCharm

import requests
from common.get_goods_detail import GetGoodsDetail
from common.get_access_token import GetAccessToken
from util.readTxt import OperationIni
from util.Logger import Logger

'''
修改商品上下架状态
'''
class updateGoodsShelfStatus:
    def __init__(self, env='QA'):
        self.log = Logger("debug")
        opera = OperationIni(fileName='config.ini', pathName='config')
        self.get_skuId = GetGoodsDetail(env=env)
        self.get_access_token = GetAccessToken(env=env)

        # env字符串转小写
        env = env.lower()
        key = env + '_url'

        self.base_url = opera.read_ini(section='goods', key=key)
        self.path = opera.read_ini(section='goods', key='updateGoodsShelfStatus')

        self.access_token = self.get_access_token.get_ini_access_token()

    def update_goods_shelf_status(self, goodsIdList, isPutAway, storeId=None):
        '''
        批量修改商品上下架状态
        :param goodsIdList: 商品id，限制50个，list类型
        :param isPutAway: 商品上、下架0：上架 1:下架
        :param storeId: 门店id
        :return: rsq
        '''

        url = self.base_url.format(self.path, self.access_token)

        # 把goodsIdList中的多个goodsId转成list类型，并保证list中的元素类型为int
        goodsIdLists = list(map(int, goodsIdList.split(',')))

        json_data = {
            'storeId': storeId,
            'goodsIdList': goodsIdLists,
            'isPutAway': isPutAway
        }

        self.log.info('开始：调用update_goods_shelf_status方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
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
            self.log.warning('开始：调用update_goods_shelf_status方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
            requests.packages.urllib3.disable_warnings()
            res = requests.post(url=url, json=json_data, verify=False)
            self.log.warning('结束：调用update_goods_shelf_status方法，返回数据为:{0}'.format(res.json()))
            return res.json()
        else:
            self.log.info('结束：调用update_goods_shelf_status方法，返回数据为:{0}'.format(r.json()))
            return r.json()




