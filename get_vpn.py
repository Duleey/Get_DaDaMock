#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 18:00
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_vpn.py
# @Software: PyCharm

import os

def start_vpn():
    print('-------------------------------------------------------')
    print("正在启动VPN:连接KA网络")
    print(os.system('rasdial "ka-dev" "账号" "密码"'))
    print("VPN连接成功:KA网络")


def stop_vpn():
    print('-------------------------------------------------------')
    print("正在关闭VPN:关闭KA网络")
    print(os.system('rasdial ka-dev /disconnect'))
    print("VPN关闭成功:KA网络")