# -*- coding: utf-8 -*-

from selenium import webdriver
import time

# 注意这里使用了我本机的谷歌浏览器驱动

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# driver.quit()