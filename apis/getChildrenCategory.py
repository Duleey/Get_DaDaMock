#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 15:51
# @Author  : Weiqiang.long
# @Site    : 
# @File    : getChildrenCategory.py
# @Software: PyCharm
# @Description: 查询商品类目

import json
from flask import Flask, Response, request
from flask import Blueprint
from common.get_children_category import getChildrenCategory

app = Flask(__name__)
GetChildrenCategory = Blueprint('getChildrenCategory', __name__)

@GetChildrenCategory.route('/getChildrenCategory', methods=['POST', 'GET'])
def get_children_category():

    if request.method == "POST":
        env = request.form.get('env', None)
        pid = request.form.get('pid', None)
        categoryId = request.form.get('categoryId', None)


        if categoryId == "" or categoryId == None:
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
            # 初始化查询二级类目类
            get_children_category = getChildrenCategory(env=env, pid=pid)
            # 调用查询二级类目方法
            result = get_children_category.get_children_category(categoryId=categoryId)
            code = None
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
            "请求场景": "查询商品类目",
            "data": result
        }
        return Response(json.dumps(res), mimetype='application/json')
    elif request.method == "GET":
        res = {
            "code": -1,
            "msg": '请使用POST请求方式'
        }
        return Response(json.dumps(res), mimetype='application/json')