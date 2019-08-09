#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 11:25
# @Author  : Weiqiang.long
# @Site    : 
# @File    : updateGoodsPrice.py
# @Software: PyCharm

import json
from flask import Flask, Response, request
from flask import Blueprint
from common.update_goods_price import updateGoodsPrice

app = Flask(__name__)
updatePrice = Blueprint('updateGoodsPrice', __name__)

@updatePrice.route('/updateGoodsPrice', methods=['POST', 'GET'])
def update_goods_price():

    if request.method == "POST":
        env = request.form.get('env', None)
        storeId = request.form.get('storeId', None)
        goodsId = request.form.get('goodsId', None)
        originalPrice = request.form.get('originalPrice', None)
        salePrice = request.form.get('salePrice', None)

        if storeId == "" or goodsId == "" or originalPrice == "" or salePrice == "":
            res = {"status":101, "message":"参数value为空"}
            return Response(json.dumps(res), mimetype='application/json')

        if storeId == None or goodsId == None or originalPrice == None or salePrice == None:
            res = {"status":102, "message":"请求参数为空"}
            return Response(json.dumps(res), mimetype='application/json')

        if env == None:
            env = "QA"
            print('-------------------------------------------------------')
            print("env参数为空,正在使用默认参数:{0}".format(env))

        # 字符串转大写
        env = env.upper()
        # 初始化修改商品价格类
        update_price = updateGoodsPrice(env=env)
        # 调用修改商品价格方法
        result = update_price.update_goods_price(storeId=storeId, goodsId=goodsId, originalPrice=originalPrice, salePrice=salePrice)
        # print(result)
        res = {
            "code": 1,
            "msg": "请求成功",
            "请求场景": "修改商品价格",
            "data": result
        }
        return Response(json.dumps(res), mimetype='application/json')
    elif request.method == "GET":
        res = {
            "code": -1,
            "msg": '请使用POST请求方式'
        }
        return Response(json.dumps(res), mimetype='application/json')


