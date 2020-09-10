from selenium import webdriver
import time
import unittest


class MyTest_SetAndTear(unittest.TestCase):
    def setUp(self):
        # 使用unittest框架来分层进行驱动的定义
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.baseurl = "https://tianqi.2345.com"
        time.sleep(0.5)
        # 获取首页句柄，便于用例场景中切换页面
        self.page_handle = self.driver.current_window_handle

    def tearDown(self):
        time.sleep(0.5)
        self.driver.quit()
