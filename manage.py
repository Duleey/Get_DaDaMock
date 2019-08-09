#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 11:27
# @Author  : Weiqiang.long
# @Site    : 
# @File    : manage.py
# @Software: PyCharm

from flask import Flask
from apis.get_dada_mock import getDaDaMock
from apis.updateGoodsPrice import updatePrice
from apis.updateGoodsStock import updateStock
from apis.updateGoodsShelfStatus import updateShelfStatus
from apis.getGoodsDetail import getGoodsDetail

app = Flask(__name__)
# 注册蓝图，并指定其对应的前缀（url_prefix）
app.register_blueprint(getDaDaMock, url_prefix="/api")
app.register_blueprint(updatePrice, url_prefix="/api")
app.register_blueprint(updateStock, url_prefix="/api")
app.register_blueprint(updateShelfStatus, url_prefix="/api")
app.register_blueprint(getGoodsDetail, url_prefix="/api")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)