import selenium
from  selenium import  webdriver
import time
import unittest
from testcase.MyTest_SetAndTear import MyTest_setandtear

class MyTest_Weather_HomePageSearch(MyTest_setandtear):

    def test_homepage_SearchCity(self):
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//div[@class='search']/input").clear()
        self.driver.find_element_by_xpath("//div[@class='search']/input").send_keys('北京')
        time.sleep(0.5)
        self.driver.find_element_by_id('js_searchBtn').click()
        time.sleep(0.5)
        title= self.driver.find_element_by_xpath("//div[@class='info-box']/div/div/div/em").text
        self.assertEqual(title,'北京',msg='搜索框检索北京失败')
        # windowstitle = self.driver.title
        # print(windowstitle)

if __name__ == '__main__':
    unittest.main()