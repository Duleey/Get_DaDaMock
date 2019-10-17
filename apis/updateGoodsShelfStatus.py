#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 21:58
# @Author  : Weiqiang.long
# @Site    : 
# @File    : updateGoodsShelfStatus.py
# @Software: PyCharm

import json
from flask import Flask, Response, request
from flask import Blueprint
from common.update_goods_shelf_status import updateGoodsShelfStatus

app = Flask(__name__)
updateShelfStatus = Blueprint('updateGoodsShelfStatus', __name__)

@updateShelfStatus.route('/updateGoodsShelfStatus', methods=['POST', 'GET'])
def update_goods_shelf_status():

    if request.method == "POST":
        env = request.form.get('env', None)
        pid = request.form.get('pid', None)
        goodsIdList = request.form.get('goodsIdList', None)
        isPutAway = request.form.get('isPutAway', None)
        storeId = request.form.get('storeId', None)

        if goodsIdList == "" or isPutAway == "" or storeId == "":
            res = {"status":101, "message":"参数value为空"}
            return Response(json.dumps(res), mimetype='application/json')
        if goodsIdList == None or isPutAway == None or storeId == None:
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
            update_shelf_status = updateGoodsShelfStatus(env=env, pid=pid)
            # 调用修改商品价格方法
            result = update_shelf_status.update_goods_shelf_status(goodsIdList=goodsIdList, isPutAway=isPutAway, storeId=storeId)
            # print(result)
            if result['data']['result'] == True:
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
            "请求场景": "修改商品上下架状态",
            "data": result
        }
        return Response(json.dumps(res), mimetype='application/json')
    elif request.method == "GET":
        res = {
            "code": -1,
            "msg": '请使用POST请求方式'
        }
        return Response(json.dumps(res), mimetype='application/json')
