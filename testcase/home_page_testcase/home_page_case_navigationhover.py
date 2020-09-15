import unittest
import time
from selenium.webdriver import ActionChains
from testcase.MyTest_SetAndTear import MyTest_SetAndTear


class MyTest_Weather_HomePage_NavigationHover(MyTest_SetAndTear):
    """导航条上hover后可点击的页面按钮用例集"""

    def view_homepage(self):
        self.driver.get(self.baseurl)

    def mover_click_hover(self, loc_navigation, loc_hover):
        NavigationButton = self.driver.find_element_by_xpath(loc_navigation)
        PointSubmit = self.driver.find_element_by_xpath(loc_hover)
        actions = ActionChains(self.driver)
        actions.move_to_element(NavigationButton)
        actions.click(PointSubmit)
        actions.perform()

    def SwitchWindows(self):
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                continue

    def CheckSwitchWindows(self):
        WindowsHandles = self.driver.current_window_handle
        try:
            self.assertNotEqual(self.page_handle, WindowsHandles, msg='目标窗口打开失败，句柄为：%s' % WindowsHandles)
        except Exception as msg:
            now = time.strftime("%Y-%m-%d %H_%M_%S")
            file_error_screenshot = 'D:\\Weathertest\\test_error_screen\\' + now + 'WindowsSwitchError_png.png'
            self.driver.get_screenshot_as_file(file_error_screenshot)
            print(msg)

    def test_NationalWeather_hover15th(self):
        """打开首页导航条中的全国天气---15日天气"""
        self.view_homepage()
        loc_navigation = "//div[@class='nav-wrap']/ul/li[2]/a"
        loc_hover = "//div[@class='nav-wrap']/ul/li[2]/div/dl/dd[1]/a"
        self.mover_click_hover(loc_navigation, loc_hover)
        self.SwitchWindows()
        self.CheckSwitchWindows()

    def test_NationalWeather_hoverToday(self):
        """打开首页导航条中的全国天气---今天天气"""
        self.view_homepage()
        loc_navigation = "//div[@class='nav-wrap']/ul/li[2]/a"
        loc_hover = "//div[@class='nav-wrap']/ul/li[2]/div/dl/dd[2]/a"
        self.mover_click_hover(loc_navigation, loc_hover)
        self.SwitchWindows()
        self.CheckSwitchWindows()

    def test_NationalWeather_hoverThisWeek(self):
        """打开首页导航条中的全国天气---一周天气"""
        self.view_homepage()
        loc_navigation = "//div[@class='nav-wrap']/ul/li[2]/a"
        loc_hover = "//div[@class='nav-wrap']/ul/li[2]/div/dl/dd[3]/a"
        self.mover_click_hover(loc_navigation, loc_hover)
        self.SwitchWindows()
        self.CheckSwitchWindows()

    def test_NationalWeather_hover40th(self):
        """打开首页导航条中的全国天气---40天天气"""
        self.view_homepage()
        loc_navigation = "//div[@class='nav-wrap']/ul/li[2]/a"
        loc_hover = "//div[@class='nav-wrap']/ul/li[2]/div/dl/dd[4]/a"
        self.mover_click_hover(loc_navigation, loc_hover)
        self.SwitchWindows()
        self.CheckSwitchWindows()


if __name__ == '__main__':
    unittest.main()
