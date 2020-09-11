import unittest
# 此py文件用来描写导航条点击跳转的case
from testcase.MyTest_SetAndTear import MyTest_SetAndTear
import time
from test_data import ReadWeather_datafile


class MyTest_Weather_HomePageAttribute(MyTest_SetAndTear):
    """首页加载成功后的必要元素判断"""
    # 获取首页必要元素
    HomePage_Atr = ReadWeather_datafile.ReadFile().ReadWeather_HomePage_Atr('WeatherHomePageAtr.csv')

    def view_homepage(self):
        self.driver.get(self.baseurl)

    def CheckDataSuccess(self, PageAtr):
        try:
            self.assertIn(PageAtr, self.HomePage_Atr, msg='模块加载失败，元素为%s' % PageAtr)
        except Exception as msg:
            now = time.strftime("%Y-%m-%d %H_%M_%S")
            file_error_screenshot = 'D:\\Weathertest\\test_error_screen\\' + now + 'AtrError_png.png'
            self.driver.get_screenshot_as_file(file_error_screenshot)
            print(msg)

    def test_homepage_PageTitle(self):
        """页面title加载"""
        self.view_homepage()
        PointTitle = self.driver.title
        self.CheckDataSuccess(PointTitle)

    def test_homepage_Atr_24hWeather(self):
        """首页24h天气模块加载"""
        self.view_homepage()
        PointTitle = self.driver.find_element_by_xpath("//div[@class='hours24-data-th']/span").text
        self.CheckDataSuccess(PointTitle)

    def test_homepage_Atr_HistoryWea(self):
        """历史访问或热门天气模块"""
        self.view_homepage()
        PointTitle = self.driver.find_element_by_xpath("//span[@id='search-city-tips']").text
        self.CheckDataSuccess(PointTitle)


if __name__ == '__main__':
    unittest.main()
