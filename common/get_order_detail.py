#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 13:58
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_order_detail.py
# @Software: PyCharm
import json
import itertools
import requests
from common.get_access_token import GetAccessToken
from util.readTxt import OperationIni
from util.Logger import logger as log

'''
获取订单详情
'''
class GetOrderDetail:
    def __init__(self, pid, env='QA'):
        self.log = log
        opera = OperationIni(fileName='config.ini', pathName='config')
        self.env = env
        self.get_access_token = GetAccessToken(env=env, pid=pid)

        # env字符串转小写
        env = env.lower()
        key = env + '_url'
        self.url = opera.read_ini(section='goods', key=key)
        self.path = opera.read_ini(section='goods', key='queryOrderDetail')

        self.access_token = self.get_access_token.get_ini_access_token()


    def get_order_detail(self, orderNo):
        '''
        获取订单详情
        :param orderNo: 订单id
        :return: rsq
        '''
        url = self.url.format(self.path, self.access_token)
        json_data = {'orderNo': orderNo}

        self.log.info('开始：调用get_order_detail方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url, json=json_data, verify=False)
        # 如果access_token无效
        if r.json()['data'] == 'invalid accesstoken':
            # 获取最新的token并存入ini文件
            self.log.warning('提示：ini文件中的accesstoken失效，开始获取新的accesstoken')
            self.get_access_token.set_access_token()
            # 注意：这里一定要重新获取一次ini文件中的access_token
            new_access_token = self.get_access_token.get_ini_access_token()
            self.log.warning('开始：调用get_order_detail方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
            url = self.url.format(self.path, new_access_token)
            requests.packages.urllib3.disable_warnings()
            res = requests.post(url=url, json=json_data, verify=False)
            # print(res.json(), url, json_data)
            try:
                self.log.warning('结束：调用get_order_detail方法，返回数据为:{0}'.format(res.json()))
                return res.json()
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
            self.log.warning('开始：调用get_order_detail方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
            requests.packages.urllib3.disable_warnings()
            res = requests.post(url=url, json=json_data, verify=False)
            # print(res.json(), url, json_data)
            try:
                self.log.warning('结束：调用get_order_detail方法，返回数据为:{0}'.format(res.json()))
                return res.json()
            except Exception as f:
                # print(f)
                self.log.error('调用获取商品详情接口失败，错误日志为：{0}'.format(f))
                # return {'msg': '底层接口请求失败，请检查所传字段的数据是否正确'}
                return res.json()

        else:
            try:
                self.log.info('结束：调用get_order_detail方法，返回数据为:{0}'.format(r.json()))
                return r.json()
            except Exception as f:
                # print(f)
                self.log.error('调用获取商品详情接口失败1，错误日志为：{0}'.format(f))
                # return {'msg': '底层接口请求失败，请检查所传字段的数据是否正确'}
                return r.json()

    def get_order_item_id_skuNum(self, orderNo):
        '''
        获取订单pickingPackageList,storeId,wid
        :param orderNo: 订单号
        :return: 返回pickingPackageList,storeId,wid
        '''
        # 调用get_order_detail方法获取返回订单详情数据
        result = self.get_order_detail(orderNo=orderNo)

        try:
            itemList = result['data']['itemList']
            # 获取该笔订单下的storeId
            storeId = result['data']['merchantInfo']['storeId']
            # 获取该笔订单下的wid
            wid = result['data']['buyerInfo']['wid']

            pickingPackageList = []
            for i in itemList:
                # 获取itemId
                itemId = i['id']
                # 获取pickSkuNum
                pickSkuNum = i['skuNum']
                d = {"itemId": itemId, "pickSkuNum": pickSkuNum}
                pickingPackageList.append(d)
            return pickingPackageList, storeId, wid
        except Exception as f:
            self.log.error('获取订单详情中的字段失败，错误日志为：{0}'.format(f))

    def get_order_item_id_skuNum_section(self, orderNo, pickSkuNum):
        '''
        通过传入的pickSkuNum(商品拣货数量)来获取订单pickingPackageList,storeId,wid
        :param orderNo: 订单号
        :param pickSkuNum 商品拣货数量列表
        :return: 返回pickingPackageList,storeId,wid
        '''
        # 调用get_order_detail方法获取返回订单详情数据
        result = self.get_order_detail(orderNo=orderNo)

        try:
            itemList = result['data']['itemList']
            # 获取该笔订单下的storeId
            storeId = result['data']['merchantInfo']['storeId']
            # 获取该笔订单下的wid
            wid = result['data']['buyerInfo']['wid']

            pickingPackageList = []
            # 此处业务调用方要确保两个list的长度一致，否则会产生None
            # itertools.zip_longest函数使用方法：https://www.cnblogs.com/imageSet/p/7473326.html
            for i,j in itertools.zip_longest(itemList,pickSkuNum):
                # 获取itemId
                itemId = i['id']
                # 获取pickSkuNum
                # pickSkuNum = i['skuNum']
                d = {"itemId": itemId, "pickSkuNum": j}
                pickingPackageList.append(d)
            print(pickingPackageList)
            return pickingPackageList, storeId, wid
        except Exception as f:
            self.log.error('获取订单详情中的字段失败，错误日志为：{0}'.format(f))


# g = GetOrderDetail(env='QA',pid=1)
# print(g.get_order_detail('10078010113'))
