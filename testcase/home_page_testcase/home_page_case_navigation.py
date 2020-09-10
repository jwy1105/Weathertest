import unittest
# 此py文件用来描写导航条点击跳转的case
from testcase.MyTest_SetAndTear import MyTest_SetAndTear
import time


class MyTest_Weather_HomePageNavigation(MyTest_SetAndTear):
    """天气首页导航条模块"""

    def SwitchWindows(self):
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                continue

    def CheckSwitchWindows(self):
        WindowsHandle = self.driver.current_window_handle
        try:
            self.assertNotEqual(self.page_handle, WindowsHandle, msg='目标窗口打开失败，句柄为：%s' % WindowsHandle)
        except Exception as msg:
            now = time.strftime("%Y-%m-%d %H_%M_%S")
            file_error_screenshot = 'D:\\Weathertest\\test_error_screen\\' + now + 'WindowsSwitchError_png.png'
            self.driver.get_screenshot_as_file(file_error_screenshot)
            print(msg)

    def test_homepage_element_HomePage(self):
        """首页导航条访问---首页"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[1]/a").click()
        # 调用切换窗口方法,切换为新开窗口
        self.SwitchWindows()
        # 调用断言判断切换窗口成功
        self.CheckSwitchWindows()
        # 回到首页窗口
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_NationalWeather(self):
        """首页导航条访问---全国天气"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[2]/a").click()
        # 调用切换窗口方法,切换为新开窗口
        self.SwitchWindows()
        # 调用断言判断切换窗口成功
        self.CheckSwitchWindows()
        # 回到首页窗口
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WeatherQuality(self):
        """首页导航条访问---空气质量"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[3]/a").click()
        # 调用切换窗口方法,切换为新开窗口
        self.SwitchWindows()
        # 调用断言判断切换窗口成功
        self.CheckSwitchWindows()
        # 回到首页窗口
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WeatherVedio(self):
        """首页导航条访问---天气视频"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[4]/a").click()
        # 调用切换窗口方法,切换为新开窗口
        self.SwitchWindows()
        # 调用断言判断切换窗口成功
        self.CheckSwitchWindows()
        # 回到首页窗口
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WeatherHistory(self):
        """首页导航条访问---历史天气"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[5]/a").click()
        # 调用切换窗口方法,切换为新开窗口
        self.SwitchWindows()
        # 调用断言判断切换窗口成功
        self.CheckSwitchWindows()
        # 回到首页窗口
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WorldWeather(self):
        """首页导航条访问---国际天气"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[6]/a").click()
        # 调用切换窗口方法,切换为新开窗口
        self.SwitchWindows()
        # 调用断言判断切换窗口成功
        self.CheckSwitchWindows()
        # 回到首页窗口
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_ProfessionWeather(self):
        """首页导航条访问---专业天气"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[7]/a").click()
        # 调用切换窗口方法,切换为新开窗口
        self.SwitchWindows()
        # 调用断言判断切换窗口成功
        self.CheckSwitchWindows()
        # 回到首页窗口
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WeatherLife(self):
        """首页导航条访问---天气资讯"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[8]/a").click()
        # 调用切换窗口方法,切换为新开窗口
        self.SwitchWindows()
        # 调用断言判断切换窗口成功
        self.CheckSwitchWindows()
        # 回到首页窗口
        self.driver.switch_to.window(self.page_handle)


if __name__ == '__main__':
    unittest.main()
