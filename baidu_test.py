# -*- coding: utf-8 -*-  
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner

class baidu(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(baidu("test_baidu_search"))
    fp = open(r'./result.html','wb')
    runner = HTMLTestRunner(stream=fp,
                        title='百度搜索测试报告',
                        description ='用例执行情况：')
    print("11111111111111111111111111111111111111111")
    runner.run(testunit)
    fp.close()


