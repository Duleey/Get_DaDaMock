#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 21:51
# @Author  : Weiqiang.long
# @Site    : 
# @File    : updateGoodsStock.py
# @Software: PyCharm

import json
from flask import Flask, Response, request
from flask import Blueprint
from common.update_goods_stock import updateGoodsStock

app = Flask(__name__)
updateStock = Blueprint('updateGoodsStock', __name__)

@updateStock.route('/updateGoodsStock', methods=['POST', 'GET'])
def update_goods_stock():

    if request.method == "POST":
        env = request.form.get('env', None)
        pid = request.form.get('pid', None)
        storeId = request.form.get('storeId', None)
        goodsId = request.form.get('goodsId', None)
        editStockNum = request.form.get('editStockNum', None)
        # batchExecution = request.form.get('batchExecution', None)

        if storeId == "" or goodsId == "" or editStockNum == "":
            res = {"status":101, "message":"参数value为空"}
            return Response(json.dumps(res), mimetype='application/json')
        if storeId == None or goodsId == None or editStockNum == None:
            res = {"status":102, "message":"请求参数为空"}
            return Response(json.dumps(res), mimetype='application/json')

        if env == None:
            env = "QA"
            print('-------------------------------------------------------')
            print("env参数为空,正在使用默认参数:{0}".format(env))

        # 字符串转大写
        env = env.upper()

        result = None
        try:
            # 初始化修改商品价格类
            update_stock = updateGoodsStock(env=env, pid=pid)
            # 调用修改商品价格方法
            result = update_stock.update_goods_stock(goodsId=goodsId, editStockNum=editStockNum, storeId=storeId)
            # print(result)
            if result['code']['errcode'] == "0":
                code = 200
                msg = "请求成功"
            else:
                code = -100
                msg = "请求失败"
        except Exception:
            code = -100
            msg = "请求失败"
            result = result

        res = {
            "code": code,
            "msg": msg,
            "请求场景": "修改商品库存",
            "data": result
        }
        return Response(json.dumps(res), mimetype='application/json')
    elif request.method == "GET":
        res = {
            "code": -1,
            "msg": '请使用POST请求方式'
        }
        return Response(json.dumps(res), mimetype='application/json')