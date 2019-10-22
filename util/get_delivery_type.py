#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 12:07
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_delivery_type.py
# @Software: PyCharm
import requests

from common.get_access_token import GetAccessToken
from util.Logger import logger as log
from util.readTxt import OperationIni


def delivery_type(result, deliveryType):
    '''
    根据配送类型来获取配送id
    :param result: 源数据
    :param deliveryType: 配送类型
    :return: 配送id
    '''
    deliveryTypeName = None
    if deliveryType == 1 or deliveryType == "1":
        deliveryTypeName = '同城限时达'
    if deliveryType == 2 or deliveryType == "2":
        deliveryTypeName = '全城配'
    # 拿到deliveryTypeList列表
    dts = result['data']['deliveryTypeList']
    # print(dts)
    # 循环dts，拿到dict
    for d in dts:
        # print(type(d), d)
        if deliveryTypeName == d['deliveryTypeName']:
            # print(d['deliveryId'])
            # 返回deliveryId
            return d['deliveryId']

    # 支持同时两种配送方式
    if deliveryType == 3 or deliveryType == "3":
        deliveryIds = []
        for d in dts:
            deliveryIds.append(d['deliveryId'])
        return deliveryIds



def get_delivery_type(pid=None, env='QA', storeId=None, deliveryType=1, goodsId=""):
    opera = OperationIni(fileName='config.ini', pathName='config')
    get_access_token = GetAccessToken(env=env, pid=pid)
    # print(pid)
    # env字符串转小写
    x_env = env.lower()
    key = x_env + '_url'
    base_url = opera.read_ini(section='goods', key=key)
    path = opera.read_ini(section='goods', key='deliveryType')
    access_token = get_access_token.get_ini_access_token()
    url = base_url.format(path, access_token)

    json_data={
    "pid": pid,
    "storeId": storeId,
    "goodsId": goodsId
}

    log.info('开始：调用get_delivery_type方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
    requests.packages.urllib3.disable_warnings()
    r = requests.post(url=url, json=json_data, verify=False)

    # 如果access_token无效
    if r.json()['data'] == 'invalid accesstoken':
        # 获取最新的token并存入ini文件
        log.warning('提示：ini文件中的accesstoken失效，开始获取新的accesstoken')
        get_access_token.set_access_token()
        # 注意：这里一定要重新获取一次ini文件中的access_token
        new_access_token = get_access_token.get_ini_access_token()
        url = base_url.format(path, new_access_token)
        log.warning('开始：调用get_delivery_type方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
        requests.packages.urllib3.disable_warnings()
        res = requests.post(url=url, json=json_data, verify=False)
        try:
            deliveryTypeId = delivery_type(result=res.json(), deliveryType=deliveryType)
            log.warning('结束：调用get_delivery_type方法，返回数据为:{0}，返回deliveryTypeId为：{1}'.format(res.json(), deliveryTypeId))
            return res.json(), deliveryTypeId
        except Exception as f:
            log.error('调用查询配送方式接口失败，错误日志为：{0}'.format(f))
            return r.json()


    elif r.json()['code']['errmsg'] == '根据Pid查询storeId失败,此商家不存在此门店':
        # 获取最新的token并存入ini文件
        log.warning('提示：根据Pid查询storeId失败,此商家不存在此门店，尝试开始获取新的accesstoken')
        get_access_token.set_access_token()
        # 注意：这里一定要重新获取一次ini文件中的access_token
        new_access_token = get_access_token.get_ini_access_token()
        url = base_url.format(path, new_access_token)
        log.warning('开始：调用get_delivery_type方法，请求地址为：{0}，入参为：{1}'.format(url, json_data))
        requests.packages.urllib3.disable_warnings()
        res = requests.post(url=url, json=json_data, verify=False)
        try:
            deliveryTypeId = delivery_type(result=res.json(), deliveryType=deliveryType)
            log.warning('结束：调用get_delivery_type方法，返回数据为:{0}，返回deliveryTypeId为：{1}'.format(res.json(), deliveryTypeId))
            return res.json(), deliveryTypeId
        except Exception as f:
            log.error('调用查询配送方式接口失败，错误日志为：{0}'.format(f))
            # return res.json()
            raise Exception("调用查询配送方式接口失败!")

    else:
        deliveryTypeId = delivery_type(result=r.json(), deliveryType=deliveryType)
        log.info('结束：调用get_delivery_type方法，返回数据为:{0}，返回deliveryTypeId为：{1}'.format(r.json(), deliveryTypeId))
        return r.json(), deliveryTypeId


# print(get_delivery_type(pid=1, env='QA',storeId=2001,deliveryType=1)[1])

