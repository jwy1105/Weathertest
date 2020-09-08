import unittest
# 此py文件用来描写导航条点击跳转的case
from testcase.MyTest_SetAndTear import MyTest_setandtear


class MyTest_Weather_HomePageNavigation(MyTest_setandtear):
    """天气首页导航条模块"""

    def test_homepage_element_HomePage(self):
        """首页导航条访问---首页"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[1]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                continue
        windowstitle = self.driver.find_element_by_xpath("//div[@class='wea-detail-index']/a").text
        print(windowstitle)
        # home_page_title ='天气预报查询一周,天气预报15天查询,24小时,10天,30天_2345天气预报'
        self.assertIsNotNone(windowstitle, msg='首页页面窗口打开失败：获取天气数据异常')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_NationalWeather(self):
        """首页导航条访问---全国天气"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[2]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                continue
        Nationaltitle = self.driver.find_element_by_xpath("//ul[@class='juhe-left']/li[2]").text
        print(Nationaltitle)
        # NationalWeather_page_title ='全国天气预报_全国城市天气预报查询地图-2345天气预报'
        self.assertIsNotNone(Nationaltitle, msg='全国天气窗口打开失败')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WeatherQuality(self):
        """首页导航条访问---空气质量"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[3]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        # WeatherQuality_page_title ='【浦东PM2.5实时查询】_浦东空气质量污染PM2.5指数查询_2345天气预报'
        WeatherQualityhandle = self.driver.current_window_handle
        self.assertNotEqual(self.page_handle, WeatherQualityhandle, msg='空气质量窗口打开失败')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WeatherVedio(self):
        """首页导航条访问---天气视频"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[4]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        # WeatherVedio_page_title = '天气预报视频_全国天气预报视频_CCTV天气预报视频_2345天气预报'
        WeatherVediohandle = self.driver.current_window_handle
        self.assertNotEqual(self.page_handle, WeatherVediohandle, msg='天气视频页面切换失败')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WeatherHistory(self):
        """首页导航条访问---历史天气"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[5]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        # WeatherHistory_page_title = '浦东历史天气查询_历史天气预报查询_2345天气预报'
        WeatherHistoryhandle = self.driver.current_window_handle
        self.assertNotEqual(self.page_handle, WeatherHistoryhandle, msg='切换历史天气页面失败')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WorldWeather(self):
        """首页导航条访问---国际天气"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[6]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        # WorldWeather_page_title = '国际天气预报_全球城市天气预报查询-2345天气预报'
        WorldWeatherhandle = self.driver.current_window_handle
        self.assertNotEqual(self.page_handle, WorldWeatherhandle, msg='切换国际天气页面失败')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_ProfessionWeather(self):
        """首页导航条访问---专业天气"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[7]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        # ProfessionWeather_page_title = '全国降水量预报图-2345天气预报'
        ProfessionWeatherWhandle = self.driver.current_window_handle
        self.assertNotEqual(self.page_handle, ProfessionWeatherWhandle, msg='切换专业天气页面失败')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WeatherLife(self):
        """首页导航条访问---天气资讯"""
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[8]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        # WeatherLife_page_title = '天气资讯-2345天气预报'
        WeatherLifeWhandle = self.driver.current_window_handle
        self.assertNotEqual(self.page_handle, WeatherLifeWhandle, msg='切换天气生活页面失败')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)


if __name__ == '__main__':
    unittest.main()
