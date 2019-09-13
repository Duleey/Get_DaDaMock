#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 16:12
# @Author  : Weiqiang.long
# @Site    : 
# @File    : updateStoreGoodsDeliveryType.py
# @Software: PyCharm

import json
from flask import Flask, Response, request
from flask import Blueprint
from common.update_store_goods_delivery_type import updateStoreGoodsDeliveryType

app = Flask(__name__)
updateDeliveryType = Blueprint('updateStoreGoodsDeliveryType', __name__)

@updateDeliveryType.route('/updateStoreGoodsDeliveryType', methods=['POST', 'GET'])
def update_store_goods_delivery_type():

    if request.method == "POST":
        env = request.form.get('env', None)
        pid = request.form.get('pid', None)
        storeId = request.form.get('storeId', None)
        goodsId = request.form.get('goodsId', None)
        deliveryType = request.form.get('deliveryType', None)

        if storeId == "" or goodsId == "" or deliveryType == "":
            res = {"status":101, "message":"参数value为空"}
            return Response(json.dumps(res), mimetype='application/json')
        if storeId == None or goodsId == None or deliveryType == None:
            res = {"status":102, "message":"请求参数为空"}
            return Response(json.dumps(res), mimetype='application/json')
        if deliveryType != "1" and deliveryType != "2":
            res = {"status":103, "message":"配送类型只能传1或2；1：同城限时达，2：全城配"}
            return Response(json.dumps(res), mimetype='application/json')

        if env == None:
            env = "QA"
            print('-------------------------------------------------------')
            print("env参数为空,正在使用默认参数:{0}".format(env))

        # 字符串转大写
        env = env.upper()
        # 初始化修改商品配送类型
        update_stock = updateStoreGoodsDeliveryType(env=env, pid=pid)
        # 调用修改商品配送类型
        result = update_stock.update_store_goods_delivery_type(goodsIdList=goodsId, deliveryType=deliveryType, storeId=storeId)
        res = {
            "code": 1,
            "msg": "请求成功",
            "请求场景": "修改商品配送类型",
            "data": result
        }
        return Response(json.dumps(res), mimetype='application/json')
    elif request.method == "GET":
        res = {
            "code": -1,
            "msg": '请使用POST请求方式'
        }
        return Response(json.dumps(res), mimetype='application/json')