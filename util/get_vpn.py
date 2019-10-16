#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 18:00
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_vpn.py
# @Software: PyCharm

import os
import platform
from util.Logger import logger as log


def start_vpn():
    if platform.system() == 'Windows':
        log.info("当前系统为Windows，正在连接VPN")
        # print('-------------------------------------------------------')
        # print("正在启动VPN:连接KA网络")
        log.info("正在启动VPN:连接KA网络")
        # print(os.system('rasdial "ka-dev" "KAprivate" "KAprivate@$^135"'))
        log.info(os.system('rasdial "ka-dev" "KAprivate" "KAprivate@$^135"'))
        # print("VPN连接成功:KA网络")
        log.info("VPN连接成功:KA网络")
    else:
        log.info("当前系统为Liunx，不连接VPN")


def stop_vpn():
    if platform.system() == 'Windows':
        log.info("当前系统为Windows，正在连接VPN")
        # print('-------------------------------------------------------')
        # print("正在关闭VPN:关闭KA网络")
        log.info("正在关闭VPN:关闭KA网络")
        # print(os.system('rasdial ka-dev /disconnect'))
        log.info(os.system('rasdial ka-dev /disconnect'))
        # print("VPN关闭成功:KA网络")
        log.info("VPN关闭成功:KA网络")
    else:
        log.info("当前系统为Liunx，不连接VPN")