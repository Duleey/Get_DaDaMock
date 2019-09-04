#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 9:39
# @Author  : Weiqiang.long
# @Site    : 
# @File    : mockOrderThrow.py
# @Software: PyCharm

import requests

from common.get_order_detail import GetOrderDetail
from util.Logger import Logger
from util.get_soa_server_ip import GetSoaServerIp
from util.get_vpn import start_vpn, stop_vpn
from util.readTxt import OperationIni

"""
模拟订单抛出
"""

class MockOrderThrow:

    def __init__(self, pid, env):
        self.log = Logger("debug")
        self.pid = pid
        self.env = env
        self.opera = OperationIni()
        self.get_order_detail = GetOrderDetail(pid=pid, env=env)

    def mock_order_throw(self, orderNo, pickNum):
        url = self.opera.read_ini(self.env, key='mock_order_throw_ip')
        mock_url = 'http://' + url + ':8080/service'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        if pickNum != None:
            # 根据逗号拆分字符串，并通过map函数对字符串进行迭代，存入list列表，且确保列表中的元素为int类型
            pickNums = pickNum.split(",")
            pickNum_list = list(map(int, pickNums))
            self.log.info("当前模式为部分/整单缺货模式，商品发货数量列表为：{0}".format(pickNum_list))
            order_detail = self.get_order_detail.get_order_item_id_skuNum_section(orderNo=orderNo,pickSkuNum=pickNum_list)
            pickingPackageList = order_detail[0]
            if len(pickNum_list) != len(pickingPackageList):
                return {"errcode": -100, "errmsg": "pickNum参数数量与订单商品数量不一致，请检查pickNum参数长度"}
        else:
            self.log.info("当前模式为整单发货模式")
            order_detail = self.get_order_detail.get_order_item_id_skuNum(orderNo=orderNo)
            pickingPackageList = order_detail[0]
        storeId = order_detail[1]
        wid = order_detail[2]

        # 组装paramterInput参数
        paramterInput = [
    {
        "markNo": "111",
        "orderNo": orderNo,
        "pickingPackageList": pickingPackageList,
        "pid": self.pid,
        "storeId": storeId,
        "wid": wid
    }
]
        # 组装参数
        data = {'serviceName': 'orderCenterUpdateExportService', 'methodName': 'pickingAndDelivery', 'paramterInput': '{0}'.format(paramterInput)}

        # 连接VPN
        start_vpn()

        code = None
        try:
            self.log.info("开始:调用订单抛出服务接口，请求地址为：{0}，入参为：{1}，请求头为：{2}".format(mock_url, data, headers))
            r = requests.post(url=mock_url, data=data, headers=headers, timeout=3)
            code = r.status_code
            result = r.json()
            print('我要看:{0}'.format(result))
            self.log.info("结束:调用订单抛出服务接口，返回数据打印:{0}".format(result))
            # 关闭VPN
            stop_vpn()
            return result
        except Exception as f:
            print(f)
            status = False

            # print(status)
            if status == False or code != 200:
                self.log.warning('IP已失效，重新获取IP')
                url = GetSoaServerIp(env=self.env, serviceName='mock_order_throw_servicename').get_soa_url()
                self.log.warning("获取的新IP为:{0}".format(url))
                self.opera.write_ini(section=self.env, data=url, key='mock_order_throw_ip')
                mock_url = 'http://' + url + ':8080/service'
                self.log.warning("请求url为:{0}，请求data为:{1}，请求头为:{2}".format(mock_url, data, headers))
                try:
                    self.log.warning("开始:调用订单抛出服务接口，请求地址为：{0}，入参为：{1}，请求头为：{2}".format(mock_url, data, headers))
                    r = requests.post(url=mock_url, data=data, headers=headers)
                    result = r.json()
                    self.log.warning("结束:调用订单抛出服务接口，返回数据打印:{0}".format(result))
                    # 关闭VPN
                    stop_vpn()
                    return result
                except Exception as f:
                    msg = {'msg':'发生未知错误,请联系管理员,错误日志为:{0}'.format(f)}
                    self.log.error('发生未知错误,请联系管理员,错误日志为:{0}'.format(f))
                    # 关闭VPN
                    stop_vpn()
                    return msg



# g = MockOrderThrow(pid=1,env='QA')
# g.mock_order_throw(orderNo='10094010113')