#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 22:04
# @Author  : Weiqiang.long
# @Site    : 
# @File    : getGoodsDetail.py
# @Software: PyCharm

import json
from flask import Flask, Response, request
from flask import Blueprint
from common.get_goods_detail import GetGoodsDetail

app = Flask(__name__)
getGoodsDetail = Blueprint('getGoodsDetail', __name__)

@getGoodsDetail.route('/getGoodsDetail', methods=['POST', 'GET'])
def get_goods_detail():

    if request.method == "POST":
        env = request.form.get('env', None)
        pid = request.form.get('pid', None)
        goodsId = request.form.get('goodsId', None)
        storeId = request.form.get('storeId', None)

        if goodsId == "" or storeId == "":
            res = {"status":101, "message":"参数value为空"}
            return Response(json.dumps(res), mimetype='application/json')
        if goodsId == None:
            res = {"status":102, "message":"请求参数为空"}
            return Response(json.dumps(res), mimetype='application/json')

        if env == None:
            env = "QA"
            print('-------------------------------------------------------')
            print("env参数为空,正在使用默认参数:{0}".format(env))

        # 字符串转大写
        env = env.upper()
        # 初始化修改商品价格类
        get_goods_detail = GetGoodsDetail(env=env, pid=pid)
        # 调用修改商品价格方法
        result = get_goods_detail.get_goods_detail(goodsId=goodsId, storeId=storeId)
        res = {
            "code": 1,
            "msg": "请求成功",
            "请求场景": "查询商品详情",
            "data": result
        }
        return Response(json.dumps(res), mimetype='application/json')
    elif request.method == "GET":
        res = {
            "code": -1,
            "msg": '请使用POST请求方式'
        }
        return Response(json.dumps(res), mimetype='application/json')

