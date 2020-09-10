import selenium
from selenium import webdriver
import time
import unittest
from testcase.MyTest_SetAndTear import MyTest_SetAndTear


class MyTest_Weather_HomePageSearch(MyTest_SetAndTear):
    """天气搜索框模块"""

    def Search(self, adr):
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//div[@class='search']/input").clear()
        self.driver.find_element_by_xpath("//div[@class='search']/input").send_keys(adr)
        time.sleep(0.5)
        self.driver.find_element_by_id('js_searchBtn').click()
        time.sleep(0.5)

    def CheckAdrAssertEqual(self, PointText):
        CountyTitle = self.driver.find_element_by_xpath("//div[@class='info-box']/div/div/div/em").text
        try:
            self.assertEqual(CountyTitle, PointText, msg='搜索框搜索%s失败' % PointText)
        except Exception as msg:
            now = time.strftime("%Y-%m-%d %H_%M_%S")
            file_error_screenshot = 'D:\\Weathertest\\test_error_screen\\' + now + PointText + 'error_png.png'
            self.driver.get_screenshot_as_file(file_error_screenshot)
            print(msg)

    #
    # def test_homepage_SearchCity(self):
    #     """首页搜索框---搜索北京市，首页切换至北京"""
    #     self.Search('北京')
    #     self.CheckAdrAssertEqual('北京')
    #     # windowstitle = self.driver.title
    #     # print(windowstitle)
    #
    # def test_homepage_SearchCounty(self):
    #     """首页搜索框---搜索浦东区，首页切换至浦东区"""
    #     self.Search('浦东')
    #     self.CheckAdrAssertEqual('浦东')
    #
    # def test_homepage_SearchTownship(self):
    #     """首页搜索---搜索张江镇，首页切换至张江镇"""
    #     self.Search('张江镇')
    #     self.CheckAdrAssertEqual('张江镇')

    def test_homepage_SearchHistoryView(self):
        """首页搜索框---点击历史访问"""
        self.driver.get(self.baseurl)
        HistoryAdr = self.driver.find_element_by_xpath("//div[@class='search-city-wrap']/div/a[1]").text
        self.driver.find_element_by_xpath("//div[@class='search-city-wrap']/div/a[1]").click()
        self.CheckAdrAssertEqual(HistoryAdr)


if __name__ == '__main__':
    unittest.main()
