#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 10:21
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_dada_mock.py
# @Software: PyCharm

import json
from common.get_mock_url import *
import requests
from util.readTxt import *
from flask import Flask, Response, request
from util.get_vpn import start_vpn,stop_vpn
from flask import Blueprint
from util.Logger import logger as log

app = Flask(__name__)
getDaDaMock = Blueprint('getDaDaMock', __name__)

@getDaDaMock.route('/getDaDaMock', methods=['POST', 'GET'])
def get_dada_mock():

    result = None
    opera = OperationIni()

    if request.method == "POST":
        mock_type = request.form.get('type')
        paramterInput = request.form.get('paramterInput')
        env = request.form.get('env', None)

        # 开始调用
        print('-------------------------------------------------------')
        log.info("开始调用mock接口,入参为:mock_type:{0},paramterInput:{1},env:{2}".format(mock_type, paramterInput, env))
        print("开始调用mock接口,入参为:mock_type:{0},paramterInput:{1},env:{2}".format(mock_type, paramterInput, env))

        if env == None:
            env = "QA"
            print('-------------------------------------------------------')
            log.info("env参数为空,正在使用默认参数:{0}".format(env))
            print("env参数为空,正在使用默认参数:{0}".format(env))

        # 字符串转大写
        env = env.upper()
        url = opera.read_ini(env)
        mock_url = 'http://' + url + ':8080/service'
        msg = None
        headers = {'Content-Type':'application/x-www-form-urlencoded'}


        """
        type定义:
        1:模拟接单
        2:订单过期
        3:取消接单
        4:模拟取货
        5:订单派送完成
        6:模拟拒收
        """
        type1 = {'serviceName': 'orderMockExportService', 'methodName': 'dadaMockOrderAccept','paramterInput': paramterInput}
        type2 = {'serviceName': 'orderMockExportService', 'methodName': 'dadaMockOrderExpire','paramterInput': paramterInput}
        type3 = {'serviceName': 'orderMockExportService', 'methodName': 'dadaMockOrderCancel','paramterInput': paramterInput}
        type4 = {'serviceName': 'orderMockExportService', 'methodName': 'dadaMockOrderFetch','paramterInput': paramterInput}
        type5 = {'serviceName': 'orderMockExportService', 'methodName': 'dadaMockOrderFinish','paramterInput': paramterInput}
        type6 = {'serviceName': 'orderMockExportService', 'methodName': 'dadaMockOrderAbnormalBack','paramterInput': paramterInput}

        body_data = None
        request_type = None

        if mock_type == '1':
            body_data = type1
            request_type = '模拟接单'
        if mock_type == '2':
            body_data = type2
            request_type = '订单过期'
        if mock_type == '3':
            body_data = type3
            request_type = '取消接单'
        if mock_type == '4':
            body_data = type4
            request_type = '模拟取货'
        if mock_type == '5':
            body_data = type5
            request_type = '订单派送完成'
        if mock_type == '6':
            body_data = type6
            request_type = '模拟拒收'

        print('-------------------------------------------------------')
        print("请求url为:{0}".format(mock_url))
        print('-------------------------------------------------------')
        print("请求data为:{0}".format(body_data))
        print('-------------------------------------------------------')
        print("请求头为:{0}".format(headers))

        code = None

        # 连接VPN
        start_vpn()

        try:
            log.info("开始:调用订单mock服务接口，请求地址为：{0}，入参为：{1}，请求头为：{2}".format(mock_url, body_data, headers))
            r = requests.post(url=mock_url, data=body_data, headers=headers, timeout=3)
            code = r.status_code
            msg = '请求成功'
            result = r.json()
            log.info("结束:调用订单mock服务接口，返回数据打印:{0}".format(result))
            print('-------------------------------------------------------')
            print("返回数据打印:{0}".format(result))
        except Exception as f:
            print(f)
            status = False

            # print(status)
            if status == False or code != 200:
                print('-------------------------------------------------------')
                print('IP已失效，重新获取IP')
                log.warning('IP已失效，重新获取IP')
                print('-------------------------------------------------------')
                url = GetMockUrl(env=env).get_mock_url()
                print("获取的新IP为:{0}".format(url))
                log.warning("获取的新IP为:{0}".format(url))
                opera.write_ini(section=env, data=url)
                print('-------------------------------------------------------')
                # read_url = read_txt()
                mock_url = 'http://' + url + ':8080/service'
                print("请求url为:{0}".format(mock_url))
                log.warning("请求url为:{0}，请求data为:{1}，请求头为:{2}".format(mock_url, body_data, headers))
                print('-------------------------------------------------------')
                print("请求data为:{0}".format(body_data))
                print('-------------------------------------------------------')
                print("请求头为:{0}".format(headers))
                try:
                    log.warning("开始:调用订单mock服务接口，请求地址为：{0}，入参为：{1}，请求头为：{2}".format(mock_url, body_data, headers))
                    r = requests.post(url=mock_url, data=body_data, headers=headers)
                    result = r.json()
                    print('-------------------------------------------------------')
                    print("返回数据打印:{0}".format(result))
                    log.warning("结束:调用订单mock服务接口，返回数据打印:{0}".format(result))
                    msg = '请求成功'
                except Exception as f:
                    msg = '发生未知错误,请联系管理员,错误日志为:{0}'.format(f)
                    log.error('发生未知错误,请联系管理员,错误日志为:{0}'.format(f))

        # 关闭VPN
        stop_vpn()

        # if mock_type == '1':
        #
        #     data = {
        #         'serviceName':type1['serviceName'],
        #         'methodName':type1['methodName'],
        #         'paramterInput':paramterInput
        #     }
        #
        #     print("请求url为:{0}".format(mock_url))
        #     print('-------------------------------------------------------')
        #     print("请求data为:{0}".format(data))
        #     print('-------------------------------------------------------')
        #     print("请求头为:{0}".format(headers))
        #     # status = None
        #     code = None
        #     try:
        #         r = requests.post(url=mock_url, data=data, headers=headers, timeout=3)
        #         code = r.status_code
        #         result = r.json()
        #         print('-------------------------------------------------------')
        #         print("返回数据打印:{0}".format(result))
        #     except Exception as f:
        #         print(f)
        #         status = True
        #         print(status)
        #         if status == True or code != 200:
        #             print('-------------------------------------------------------')
        #             print('IP已失效，重新获取IP')
        #             print('-------------------------------------------------------')
        #             url = GetMockUrl().get_mock_url()
        #             print("获取的新IP为:{0}".format(url))
        #             write_txt(url)
        #             print('-------------------------------------------------------')
        #             # read_url = read_txt()
        #             mock_url = 'http://' + url + ':8080/service'
        #             print("请求url为:{0}".format(mock_url))
        #             print('-------------------------------------------------------')
        #             print("请求data为:{0}".format(data))
        #             print('-------------------------------------------------------')
        #             print("请求头为:{0}".format(headers))
        #             r = requests.post(url=mock_url, data=data, headers=headers)
        #             result = r.json()
        #             print('-------------------------------------------------------')
        #             print("返回数据打印:{0}".format(result))


        # if mock_type == '2':
        #
        #     data = {
        #         'serviceName': type2['serviceName'],
        #         'methodName': type2['methodName'],
        #         'paramterInput': paramterInput
        #     }
        #
        #     print("请求url为:{0}".format(mock_url))
        #     print('-------------------------------------------------------')
        #     print("请求data为:{0}".format(data))
        #     print('-------------------------------------------------------')
        #     print("请求头为:{0}".format(headers))
        #     status = None
        #     code = None
        #     try:
        #         r = requests.post(url=mock_url, data=data, headers=headers, timeout=3)
        #         code = r.status_code
        #         result = r.json()
        #         print('-------------------------------------------------------')
        #         print("返回数据打印:{0}".format(result))
        #     except Exception:
        #         status = False
        #     if status == False or code != 200:
        #         print('-------------------------------------------------------')
        #         print('IP已失效，重新获取IP')
        #         print('-------------------------------------------------------')
        #         url = GetMockUrl().get_mock_url()
        #         print("获取的IP为:{0}".format(url))
        #         write_txt(url)
        #         print('-------------------------------------------------------')
        #         # mock_url = 'http://' + url + ':8080/service'
        #         print("请求url为:{0}".format(mock_url))
        #         print('-------------------------------------------------------')
        #         print("请求data为:{0}".format(data))
        #         print('-------------------------------------------------------')
        #         print("请求头为:{0}".format(headers))
        #         r = requests.post(url=mock_url, data=data, headers=headers)
        #         result = r.text
        #         print('-------------------------------------------------------')
        #         print("返回数据打印:{0}".format(result))
        #
        # if mock_type == '3':
        #
        #     data = {
        #         'serviceName': type3['serviceName'],
        #         'methodName': type3['methodName'],
        #         'paramterInput': paramterInput
        #     }
        #
        #     print("请求url为:{0}".format(mock_url))
        #     print('-------------------------------------------------------')
        #     print("请求data为:{0}".format(data))
        #     print('-------------------------------------------------------')
        #     print("请求头为:{0}".format(headers))
        #     status = None
        #     code = None
        #     try:
        #         r = requests.post(url=mock_url, data=data, headers=headers, timeout=3)
        #         code = r.status_code
        #         result = r.json()
        #         print('-------------------------------------------------------')
        #         print("返回数据打印:{0}".format(result))
        #     except Exception:
        #         status = False
        #     if status == False or code != 200:
        #         print('-------------------------------------------------------')
        #         print('IP已失效，重新获取IP')
        #         print('-------------------------------------------------------')
        #         url = GetMockUrl().get_mock_url()
        #         print("获取的IP为:{0}".format(url))
        #         write_txt(url)
        #         print('-------------------------------------------------------')
        #         # mock_url = 'http://' + url + ':8080/service'
        #         print("请求url为:{0}".format(mock_url))
        #         print('-------------------------------------------------------')
        #         print("请求data为:{0}".format(data))
        #         print('-------------------------------------------------------')
        #         print("请求头为:{0}".format(headers))
        #         r = requests.post(url=mock_url, data=data, headers=headers)
        #         result = r.text
        #         print('-------------------------------------------------------')
        #         print("返回数据打印:{0}".format(result))
        #
        # if mock_type == '4':
        #
        #     data = {
        #         'serviceName': type4['serviceName'],
        #         'methodName': type4['methodName'],
        #         'paramterInput': paramterInput
        #     }
        #
        #     print("请求url为:{0}".format(mock_url))
        #     print('-------------------------------------------------------')
        #     print("请求data为:{0}".format(data))
        #     print('-------------------------------------------------------')
        #     print("请求头为:{0}".format(headers))
        #     status = None
        #     code = None
        #     try:
        #         r = requests.post(url=mock_url, data=data, headers=headers, timeout=3)
        #         code = r.status_code
        #         result = r.json()
        #         print('-------------------------------------------------------')
        #         print("返回数据打印:{0}".format(result))
        #     except Exception:
        #         status = False
        #     if status == False or code != 200:
        #         print('-------------------------------------------------------')
        #         print('IP已失效，重新获取IP')
        #         print('-------------------------------------------------------')
        #         url = GetMockUrl().get_mock_url()
        #         print("获取的IP为:{0}".format(url))
        #         write_txt(url)
        #         print('-------------------------------------------------------')
        #         # mock_url = 'http://' + url + ':8080/service'
        #         print("请求url为:{0}".format(mock_url))
        #         print('-------------------------------------------------------')
        #         print("请求data为:{0}".format(data))
        #         print('-------------------------------------------------------')
        #         print("请求头为:{0}".format(headers))
        #         r = requests.post(url=mock_url, data=data, headers=headers)
        #         result = r.text
        #         print('-------------------------------------------------------')
        #         print("返回数据打印:{0}".format(result))
        #
        # if mock_type == '5':
        #
        #     data = {
        #         'serviceName': type5['serviceName'],
        #         'methodName': type5['methodName'],
        #         'paramterInput': paramterInput
        #     }
        #
        #     print("请求url为:{0}".format(mock_url))
        #     print('-------------------------------------------------------')
        #     print("请求data为:{0}".format(data))
        #     print('-------------------------------------------------------')
        #     print("请求头为:{0}".format(headers))
        #     status = None
        #     code = None
        #     try:
        #         r = requests.post(url=mock_url, data=data, headers=headers, timeout=3)
        #         code = r.status_code
        #         result = r.json()
        #         print('-------------------------------------------------------')
        #         print("返回数据打印:{0}".format(result))
        #     except Exception:
        #         status = False
        #     if status == False or code != 200:
        #         print('-------------------------------------------------------')
        #         print('IP已失效，重新获取IP')
        #         print('-------------------------------------------------------')
        #         url = GetMockUrl().get_mock_url()
        #         print("获取的IP为:{0}".format(url))
        #         write_txt(url)
        #         print('-------------------------------------------------------')
        #         # mock_url = 'http://' + url + ':8080/service'
        #         print("请求url为:{0}".format(mock_url))
        #         print('-------------------------------------------------------')
        #         print("请求data为:{0}".format(data))
        #         print('-------------------------------------------------------')
        #         print("请求头为:{0}".format(headers))
        #         r = requests.post(url=mock_url, data=data, headers=headers)
        #         result = r.text
        #         print('-------------------------------------------------------')
        #         print("返回数据打印:{0}".format(result))
        #
        # if mock_type == '6':
        #
        #     data = {
        #         'serviceName': type6['serviceName'],
        #         'methodName': type6['methodName'],
        #         'paramterInput': paramterInput
        #     }
        #
        #     print("请求url为:{0}".format(mock_url))
        #     print('-------------------------------------------------------')
        #     print("请求data为:{0}".format(data))
        #     print('-------------------------------------------------------')
        #     print("请求头为:{0}".format(headers))
        #     status = None
        #     code = None
        #     try:
        #         r = requests.post(url=mock_url, data=data, headers=headers, timeout=3)
        #         code = r.status_code
        #         result = r.json()
        #         print('-------------------------------------------------------')
        #         print("返回数据打印:{0}".format(result))
        #     except Exception:
        #         status = False
        #     if status == False or code != 200:
        #         print('-------------------------------------------------------')
        #         print('IP已失效，重新获取IP')
        #         print('-------------------------------------------------------')
        #         url = GetMockUrl().get_mock_url()
        #         print("获取的IP为:{0}".format(url))
        #         write_txt(url)
        #         print('-------------------------------------------------------')
        #         # mock_url = 'http://' + url + ':8080/service'
        #         print("请求url为:{0}".format(mock_url))
        #         print('-------------------------------------------------------')
        #         print("请求data为:{0}".format(data))
        #         print('-------------------------------------------------------')
        #         print("请求头为:{0}".format(headers))
        #         r = requests.post(url=mock_url, data=data, headers=headers)
        #         result = r.text
        #         print('-------------------------------------------------------')
        #         print("返回数据打印:{0}".format(result))


        res = {
            "code": 1,
            "msg": msg,
            "请求类型": request_type,
            "data": result
        }

        return Response(json.dumps(res), mimetype='application/json')

    elif request.method == "GET":
        res = {
            "code": -1,
            "msg": '请使用POST请求方式'
        }
        return Response(json.dumps(res), mimetype='application/json')





# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=6000, debug=True)
