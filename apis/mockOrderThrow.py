#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 15:27
# @Author  : Weiqiang.long
# @Site    : 
# @File    : mockOrderThrow.py
# @Software: PyCharm

import json
from flask import Flask, Response, request
from flask import Blueprint
from common.mock_order_throw import MockOrderThrow

app = Flask(__name__)
mockOrderThrow = Blueprint('mockOrderThrow', __name__)

@mockOrderThrow.route('/mockOrderThrow', methods=['POST', 'GET'])
def mock_order_throw():

    if request.method == "POST":
        env = request.form.get('env', None)
        pid = request.form.get('pid', None)
        orderNo = request.form.get('orderNo', None)

        if env == None:
            env = "QA"
            print('-------------------------------------------------------')
            print("env参数为空,正在使用默认参数:{0}".format(env))

        if orderNo == None:
            res = {"status":101, "message":"请求参数为空"}
            return Response(json.dumps(res), mimetype='application/json')

        if pid == None:
            if env == 'DEV':
                pid = 3017
            if env == 'QA':
                pid = 1

        # 字符串转大写
        env = env.upper()
        # 初始化订单抛单类
        mock_order_throw = MockOrderThrow(pid=pid, env=env)
        # 调用订单抛单方法
        try:
            result = mock_order_throw.mock_order_throw(orderNo=orderNo)
        except Exception as f:
            result = {'error_msg':'请求错误，请检查参数！错误日志为：{0}'.format(f)}
        res = {
            "code": 1,
            "msg": "请求成功",
            "请求场景": "操作订单拣货",
            "data": result
        }
        return Response(json.dumps(res), mimetype='application/json')
    elif request.method == "GET":
        res = {
            "code": -1,
            "msg": '请使用POST请求方式'
        }
        return Response(json.dumps(res), mimetype='application/json')