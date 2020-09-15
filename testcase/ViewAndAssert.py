from test_data import ReadWeather_datafile
from testcase.MyTest_SetAndTear import MyTest_SetAndTear
import time
from selenium.webdriver.common.by import By


class ViewAndAssert(MyTest_SetAndTear):
    """完成页面的访问以及断言的构造"""

    def view_homepage(self):
        self.driver.get(self.baseurl)

    def CheckDataSuccess(self, PageAtr, PointAtr):
        try:
            self.assertIn(PageAtr, PointAtr, msg='模块加载失败，元素为%s' % PageAtr)
        except Exception as msg:
            now = time.strftime("%Y-%m-%d %H_%M_%S")
            file_error_screenshot = 'D:\\Weathertest\\test_error_screen\\' + now + 'AtrError_png.png'
            self.driver.get_screenshot_as_file(file_error_screenshot)
            print(msg)

    def test_ViewTextAssert(self, PointTitles, *loc):
        """访问首页，获取对应元素的Text，对比断言本件"""
        self.view_homepage()
        AtrTitle = self.driver.find_element(*loc).text
        self.CheckDataSuccess(AtrTitle, PointTitles)


if __name__ == '__main__':
    try:
        HomePage_Atr = ReadWeather_datafile.ReadFile().ReadWeather_HomePage_Atr('WeatherHomePageAtr.csv')
        print(HomePage_Atr)
        Adr = "//div[@class='box-mod-right']/div[6]/div[2]/div[1]/a"
        loc_xpath = (By.XPATH, Adr)
        VAA = ViewAndAssert()
        VAA.test_ViewTextAssert(HomePage_Atr, *loc_xpath)
    except Exception as msg:
        print(msg)
