#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 11:27
# @Author  : Weiqiang.long
# @Site    : 
# @File    : manage.py
# @Software: PyCharm
import json

from flask import Flask, request, Response
from flask_cors import CORS
from apis.get_dada_mock import getDaDaMock
from apis.addGoods import AddGoods
from apis.mockOrderThrow import mockOrderThrow
from apis.updateGoodsPrice import updatePrice
from apis.updateGoodsStock import updateStock
from apis.updateGoodsShelfStatus import updateShelfStatus
from apis.getGoodsDetail import getGoodsDetail

app = Flask(__name__)
# 注册蓝图，并指定其对应的前缀（url_prefix）
app.register_blueprint(getDaDaMock, url_prefix="/api")
app.register_blueprint(AddGoods, url_prefix="/api")
app.register_blueprint(updatePrice, url_prefix="/api")
app.register_blueprint(updateStock, url_prefix="/api")
app.register_blueprint(updateShelfStatus, url_prefix="/api")
app.register_blueprint(getGoodsDetail, url_prefix="/api")
app.register_blueprint(mockOrderThrow, url_prefix="/api")

@app.route('/apis', methods=['GET'])
def get_apis():
    if request.method == "GET":
        res = {
    "code": 1,
    "msg": "请求成功",
    "请求场景": "接口列表",
    "prefix": "/api",
    "data": [
        {
            "mock订单状态": {
                "path": "/getDaDaMock",
                "params": {
                    "env": "环境",
                    "type": "模拟类型",
                    "paramterInput": "订单编号"
                }
            },
            "新增商品": {
                "path": "/addGoods",
                "params": {
                    "env": "环境",
                    "pid": "商家id",
                    "storeId": "门店id",
                    "deliveryTypeIdList":"配送方式id",
                    "outerGoodsCode": "spu编码",
                    "title": "商品标题",
                    "salePrice": "售价",
                    "originalPrice": "市场价",
                    "adviseSalePriceMin": "门店售价范围开始值",
                    "adviseSalePriceMax": "门店售价范围结束值",
                    "goodsImageUrl": "商品图片"
                }
            },
            "获取商品详情": {
                "path": "/getGoodsDetail",
                "params": {
                    "env": "环境",
                    "goodsId": "商品id",
                    "storeId": "门店id"
                }
            },
            "修改商品价格": {
                "path": "/updateGoodsPrice",
                "params": {
                    "env": "环境",
                    "storeId": "门店id",
                    "goodsId": "商品id",
                    "originalPrice": "市场价",
                    "salePrice": "商家统一价"
                }
            },
            "修改商品上下架状态": {
                "path": "/updateGoodsShelfStatus",
                "params": {
                    "env": "环境",
                    "goodsIdList": "商品id（多个商品id时，请用，号隔开）",
                    "isPutAway": "商品上、下架（0：上架 1:下架）",
                    "storeId": "门店id"
                }
            },
            "修改商品库存": {
                "path": "/updateGoodsStock",
                "params": {
                    "env": "环境",
                    "storeId": "门店id",
                    "goodsId": "商品id",
                    "editStockNum": "需要修改的库存"
                }
            },
            "操作订单抛单": {
                "path": "/mockOrderThrow",
                "params": {
                    "env": "环境",
                    "pid": "商家id",
                    "orderNo": "订单id"
                }
            }
        }
    ]
}
        return Response(json.dumps(res), mimetype='application/json')




if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(host='0.0.0.0', port=8089, debug=True)