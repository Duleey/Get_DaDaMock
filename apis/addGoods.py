#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 13:19
# @Author  : Weiqiang.long
# @Site    : 
# @File    : addGoods.py
# @Software: PyCharm

import json
from flask import Flask, Response, request
from flask import Blueprint
from common.add_goods import addGoods

app = Flask(__name__)
AddGoods = Blueprint('addGoods', __name__)

@AddGoods.route('/addGoods', methods=['POST', 'GET'])
def add_goods():

    if request.method == "POST":
        env = request.form.get('env', None)
        pid = request.form.get('pid', None)
        storeId = request.form.get('storeId', None)
        outerGoodsCode = request.form.get('outerGoodsCode', None)
        outerSkuCode = request.form.get('outerSkuCode', None)
        deliveryTypeIdList = request.form.get('deliveryTypeIdList', None)
        title = request.form.get('title', None)
        salePrice = request.form.get('salePrice', None)
        originalPrice = request.form.get('originalPrice', None)
        adviseSalePriceMin = request.form.get('adviseSalePriceMin', None)
        adviseSalePriceMax = request.form.get('adviseSalePriceMax', None)
        goodsWeight = request.form.get('goodsWeight', None)
        goodsVolume = request.form.get('goodsVolume', None)
        goodsImageUrl = request.form.get('goodsImageUrl', None)


        if title == "" or title == None:
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
            # 初始化新增商品类
            add_goods = addGoods(env=env, pid=pid)
            # 调用新增商品方法
            result = add_goods.add_goods(storeId=storeId, outerGoodsCode=outerGoodsCode, outerSkuCode=outerSkuCode,
                                         deliveryTypeIdList=deliveryTypeIdList,
                                         title=title, salePrice=salePrice, originalPrice=originalPrice,
                                         adviseSalePriceMin=adviseSalePriceMin,
                                         adviseSalePriceMax=adviseSalePriceMax, goodsWeight=goodsWeight,
                                         goodsVolume=goodsVolume, goodsImageUrl=goodsImageUrl)
            code = None
            if result[0]['code']['errcode'] == "0":
                code = 200
            msg = "请求成功"
        except Exception:
            code = -100
            msg = "请求失败"
            result = result

        res = {
            "code": code,
            "msg": msg,
            "请求场景": "新增商品",
            "data": result
        }
        return Response(json.dumps(res), mimetype='application/json')
    elif request.method == "GET":
        res = {
            "code": -1,
            "msg": '请使用POST请求方式'
        }
        return Response(json.dumps(res), mimetype='application/json')