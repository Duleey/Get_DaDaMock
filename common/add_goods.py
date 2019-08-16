#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 12:17
# @Author  : Weiqiang.long
# @Site    : 
# @File    : add_goods.py
# @Software: PyCharm

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 13:39
# @Author  : Weiqiang.long
# @Site    :
# @File    : get_goods_detail.py
# @Software: PyCharm
import time

import requests
from common.get_access_token import GetAccessToken
from util.get_delivery_type import get_delivery_type
from util.readTxt import OperationIni
from util.Logger import Logger

'''
新增商品
'''
class addGoods:
    def __init__(self, pid, env='QA'):
        self.log = Logger("debug")
        opera = OperationIni(fileName='config.ini', pathName='config')
        self.env = env
        self.pid = pid
        self.get_access_token = GetAccessToken(env=env, pid=pid)

        # env字符串转小写
        env = env.lower()
        key = env + '_url'
        self.url = opera.read_ini(section='goods', key=key)
        self.path = opera.read_ini(section='goods', key='addgoods')

        self.access_token = self.get_access_token.get_ini_access_token()


    def add_goods(self, storeId=None, outerGoodsCode=None, outerSkuCode=None, deliveryTypeIdList=None, title=None, salePrice=None, originalPrice=None,
                  adviseSalePriceMin=None, adviseSalePriceMax=None, goodsImageUrl=None):
        """
        新增商品
        :param storeId: 门店id
        :param outerGoodsCode: 外部spu编码
        :param outerSkuCode: 商家编码
        :param deliveryTypeIdList: 配送类型列表，可传多个配送类型，用,隔开（1.同城限时达;2.全城配;3.包含1和2）
        :param title: 商品标题
        :param salePrice: 售价
        :param originalPrice: 市场价
        :param adviseSalePriceMin: 门店售价范围开始值
        :param adviseSalePriceMax: 门店售价范围结束值
        :param goodsImageUrl: 商品图片
        :return:
        """
        url = self.url.format(self.path, self.access_token)

        pid = self.pid
        if self.pid == None:
            if self.env == 'QA':
                pid = 1
            if self.env == 'DEV':
                pid = 17
            # TODO 预留prod环境
            if self.env == 'PROD':
                pid = 17
        # print(pid)

        if storeId == None:
            if self.env == "QA":
                storeId = 1001
            if self.env == "DEV":
                storeId = 3017
            # TODO 预留prod环境
            if self.env == "PROD":
                storeId = 3017

        if outerGoodsCode == None:
            # 使用秒级时间戳自动拼接spu
            t = int(time.time())
            d = 'spu' + str(t)
            outerGoodsCode = d

        # 商家编码
        if outerSkuCode != None:
            outerSkuCode = outerSkuCode

        deliveryTypeId = None
        if deliveryTypeIdList != None:
            if deliveryTypeIdList == '3':
                deliveryTypeId = get_delivery_type(env=self.env, pid=pid, storeId=storeId, deliveryType=int(deliveryTypeIdList))[1]
                if deliveryTypeId == None:
                    return {"status": 103, "message": "当前门店该配送方式不存在"}
                elif len(deliveryTypeId) < 2:
                    return {"status": 104, "message": "当前门店只有一种配送方式,请重新传递配送方式ID"}
                else:
                    deliveryTypeId = deliveryTypeId
            else:

                deliveryType = get_delivery_type(env=self.env, pid=self.pid, storeId=storeId, deliveryType=int(deliveryTypeIdList))[1]
                if deliveryType == None:
                    return {"status": 103, "message": "当前门店该配送方式不存在"}
                else:
                    deliveryTypeId=[]
                    deliveryTypeId.append(deliveryType)

        if deliveryTypeIdList == None:
            if self.env == "QA":
                deliveryTypeId = [2]
            if self.env == "DEV":
                deliveryTypeId = [209435]
            # TODO 预留prod环境
            if self.env == "PROD":
                deliveryTypeId = [209435]

        if salePrice == None:
            salePrice = 0.01
        # if originalPrice == None:
        #     originalPrice = 1
        if adviseSalePriceMin == None:
            adviseSalePriceMin = 0.01
        if adviseSalePriceMax == None:
            adviseSalePriceMax = 1
        if goodsImageUrl == None:
            goodsImageUrl = "https://image-c.weimobmxd.com/saas-wxbiz/a016cb2de441406289433fd0c71c56bd.png"




        json_data = {
    "storeId": storeId,
    "goods": {
        "b2cGoods": {
            "deliveryTypeIdList": deliveryTypeId,
            "b2cGoodsType": 0
        },
        "categoryId": 274,
        "title": title,
        "isMultiSku": 0,
        "outerGoodsCode": outerGoodsCode,
        "goodsTagId": "",
        "goodsDesc": "",
        "goodsTemplateId": -1,
        "isMemberShipDiscount": 0,
        "deductStockType": 1,
        "isCanSell": 1,
        "isAutoCanSell": 0,
        "isAutoForbidSell": 0,
        "startSellTime": None,
        "startForbidTime": None,
        "categoryNameTree": "食品,零食/坚果/特产,其他休闲零食",
        "skuList": [
            {
                "outerSkuCode": outerSkuCode,
                "productType": 1,
                "singleProductId": 116130117,
                "combineProduct": {},
                "salePrice": salePrice,
                "adviseSalePriceMin": adviseSalePriceMin,
                "adviseSalePriceMax": adviseSalePriceMax,
                "originalPrice": originalPrice,
                "b2cSku": {
                    "weight": None,
                    "volume": None
                },
                "isDisabled": False,
                "editStockNum": 0
            }
        ],
        "selectedGoodsAttrList": [],
        "selectedSaleAttrList": [],
        "goodsVideoUrl": None,
        "goodsVideoImageUrl": None,
        "limitBuyNum": 0,
        "isPutAway": 0,
        "saleChannelType": 3,
        "selectedGoodsPropList": [],
        "selectedInnerGoodsPropList": [],
        "goodsImageUrl": [
            goodsImageUrl
        ],
        "goodsBrandId": ""
    }
}


        self.log.info('开始：调用add_goods方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url, json=json_data, verify=False)
        # print(r.json())

        # 如果access_token无效
        if r.json()['data'] == 'invalid accesstoken':
            # 获取最新的token并存入ini文件
            self.log.warning('提示：ini文件中的accesstoken失效，开始获取新的accesstoken')
            self.get_access_token.set_access_token()
            # 注意：这里一定要重新获取一次ini文件中的access_token
            new_access_token = self.get_access_token.get_ini_access_token()
            url = self.url.format(self.path, new_access_token)
            self.log.warning('开始：调用add_goods方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
            requests.packages.urllib3.disable_warnings()
            res = requests.post(url=url, json=json_data, verify=False)
            # print(res.json(), url, json_data)
            try:
                goodsId = res.json()['data']['goodsId']
                skuId = res.json()['data']['skuList'][0]['skuId']
                self.log.warning('结束：调用add_goods方法，返回数据为:{0}，返回goodsId为：{1}，返回skuId为：{2}'.format(res.json(),goodsId,skuId))
                return res.json(), goodsId, skuId
            except Exception as f:
                # print(f)
                self.log.error('调用新增商品接口失败，错误日志为：{0}'.format(f))
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
            self.log.warning('开始：调用add_goods方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
            requests.packages.urllib3.disable_warnings()
            res = requests.post(url=url, json=json_data, verify=False)

            # print(res.json(), url, json_data)
            try:
                goodsId = res.json()['data']['goodsId']
                skuId = res.json()['data']['skuList'][0]['skuId']
                self.log.warning('结束：调用add_goods方法，返回数据为:{0}，返回goodsId为：{1}，返回skuId为：{2}'.format(res.json(),goodsId,skuId))
                return res.json(), goodsId, skuId
            except Exception as f:
                # print(f)
                self.log.error('调用新增商品接口失败，错误日志为：{0}'.format(f))
                return {'msg': '根据Pid查询storeId失败,此商家不存在此门店,请检查storeId是否正确'}

        else:
            try:
                goodsId = r.json()['data']['goodsId']
                skuId = r.json()['data']['skuList'][0]['skuId']
                self.log.warning('结束：调用add_goods方法，返回数据为:{0}，返回goodsId为：{1}，返回skuId为：{2}'.format(r.json(), goodsId, skuId))
                return r.json(), goodsId, skuId
            except Exception as f:
                # print(f)
                self.log.error('调用新增商品接口失败1，错误日志为：{0}'.format(f))
                # return {'msg': '底层接口请求失败，请检查所传字段的数据是否正确'}
                return r.json()




# g = AddGoods(env='DEV')
# print(g.add_goods(title='自动增加商品'))
