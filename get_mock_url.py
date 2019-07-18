#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 9:44
# @Author  : Weiqiang.long
# @Site    : 
# @File    : get_mock_url.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class GetMockUrl:

    def __init__(self):
        chrome_driver = r"D:\work\TestCode\Git_DaDaMock\driver\chromedriver.exe"
        url = 'xxx'
        self.userName = 'xxx'
        self.passWord = 'xxx'
        self.mockServiceName = 'xxx'

        chrome_options = Options()
        # 设置chrome浏览器无界面模式
        chrome_options.add_argument('--headless')

        self.d = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
        self.d.maximize_window()
        self.d.get(url)
        self.d.implicitly_wait(30)



    def get_mock_url(self):
        self.d.find_element_by_xpath("//input[@placeholder='请输入用户名']").send_keys(self.userName)
        self.d.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys(self.passWord)
        self.d.find_element_by_xpath("//button[@class='ivu-btn ivu-btn-primary ivu-btn-long']").click()
        self.d.implicitly_wait(30)
        self.d.find_element_by_id('searchContent').send_keys(self.mockServiceName)
        self.d.find_element_by_id('searchContent').send_keys(Keys.ENTER)
        u = self.d.find_element_by_xpath("//*[@id='table_o']/tbody/tr[2]/td[2]/a").text
        # 截取冒号之前的ip段，并转换成str类型
        str_url = (" ".join(u.split(':')[:1]))
        # print(str_url, type(str_url))
        self.d.quit()
        return str_url



# g = GetMockUrl()
# g.get_mock_url()