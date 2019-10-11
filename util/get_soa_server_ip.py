#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 14:39
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_soa_server_ip.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from util.readTxt import OperationIni
from util import findPath
from util.Logger import logger as log

"""
爬取SOA后台对应服务的ip
"""
class GetSoaServerIp:

    def __init__(self, env, serviceName):
        self.log = log

        opera = OperationIni()

        chrome_driver = findPath.data_dir(fileName='chromedriver.exe', pathName='driver')
        base_url = opera.read_ini(section='CONFIG', key='base_url')
        url = base_url + opera.read_ini(section=env, key='url')


        self.userName = opera.read_ini(section='CONFIG', key='userName')
        self.passWord = opera.read_ini(section='CONFIG', key='passWord')
        self.ServiceName = opera.read_ini(section='CONFIG', key=serviceName)

        chrome_options = Options()
        # 设置chrome浏览器无界面模式
        chrome_options.add_argument('--headless')

        self.log.info("开始调用webdriver，当前模式为Chrome无界面模式")
        self.d = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
        self.d.maximize_window()
        self.log.info('成功打开谷歌浏览器')
        self.d.get(url)
        self.d.implicitly_wait(30)
        print('成功打开网址:{0}'.format(url))
        self.log.info('成功打开网址:{0}'.format(url))



    def get_soa_url(self):
        self.d.find_element_by_xpath("//input[@placeholder='请输入用户名']").send_keys(self.userName)
        self.d.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys(self.passWord)
        self.d.find_element_by_xpath("//button[@class='ivu-btn ivu-btn-primary ivu-btn-long']").click()
        self.d.implicitly_wait(30)
        print('-------------------------------------------------------')
        print('登录成功')
        self.log.info('登录成功')
        self.d.find_element_by_id('searchContent').send_keys(self.ServiceName)
        print('-------------------------------------------------------')
        print('正在查询对应服务')
        self.log.info("正在查询服务：{0}".format(self.ServiceName))
        self.d.find_element_by_id('searchContent').send_keys(Keys.ENTER)
        u = self.d.find_element_by_xpath("//*[@id='table_o']/tbody/tr[2]/td[2]/a").text
        # 截取冒号之前的ip段，并转换成str类型
        str_url = (" ".join(u.split(':')[:1]))
        self.log.info("查询到当前服务ip为：{0}".format(str_url))
        # print(str_url, type(str_url))
        self.d.quit()
        return str_url



# g = GetSoaServerIp(env='QA', serviceName='mock_order_throw_servicename')
# g.get_soa_url()