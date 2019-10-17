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
        pickNum = request.form.get('pickNum', None)

        if env == None:
            env = "QA"
            print('-------------------------------------------------------')
            print("env参数为空,正在使用默认参数:{0}".format(env))

        if orderNo == None:
            res = {"status":101, "message":"请求参数为空"}
            return Response(json.dumps(res), mimetype='application/json')

        if pid == None:
            if env == 'DEV' or env == 'dev':
                pid = 17
            if env == 'QA' or env == 'qa':
                pid = 1

        # 字符串转大写
        env = env.upper()

        try:
            # 初始化订单抛单类
            mock_order_throw = MockOrderThrow(pid=pid, env=env)
            # 调用订单抛单方法
            result = mock_order_throw.mock_order_throw(orderNo=orderNo, pickNum=pickNum)

            czms = result[1]
            data = result[0]
            if result[0]['successForMornitor'] == True:
                code = 200
                msg = "请求成功"
            else:
                code = -100
                msg = "请求失败"
        except Exception:
            czms = None
            code = -100
            msg = "请求失败"
            data = {'error_msg': '请求错误，请检查参数！'}

        res = {
            "code": code,
            "msg": msg,
            "请求场景": "操作订单拣货",
            "操作模式": czms,
            "data": data
        }
        return Response(json.dumps(res), mimetype='application/json')
    elif request.method == "GET":
        res = {
            "code": -1,
            "msg": '请使用POST请求方式'
        }
        return Response(json.dumps(res), mimetype='application/json')