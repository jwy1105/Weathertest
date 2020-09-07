import unittest
#此py文件用来描写导航条点击跳转的case
from testcase.MyTest_SetAndTear import MyTest_setandtear

class MyTest_Weather_HomePageNavigation(MyTest_setandtear):

    def test_homepage_element_HomePage(self):
        #点击导航条上的第一个按钮
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[1]/a").click()
        #获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        windowstitle = self.driver.title
        print(windowstitle)
        home_page_title ='天气预报查询一周,天气预报15天查询,24小时,10天,30天_2345天气预报'
        self.assertEqual(windowstitle,home_page_title,msg='页面title与首页不符合')
        #切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_NationalWeather(self):
        # 点击导航条上的第二个按钮
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[2]/a").click()
        #获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        title = self.driver.title
        NationalWeather_page_title ='全国天气预报_全国城市天气预报查询地图-2345天气预报'
        self.assertEqual(title,NationalWeather_page_title,msg='页面title与全国天气页面不符合')
        #切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WeatherQuality(self):
        # 点击导航条上的第三个按钮
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[3]/a").click()
        #获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        title = self.driver.title
        WeatherQuality_page_title ='【浦东PM2.5实时查询】_浦东空气质量污染PM2.5指数查询_2345天气预报'
        self.assertEqual(title,WeatherQuality_page_title,msg='页面title与空气质量不符合')
        #切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WeatherVedio(self):
        # 点击导航条上的第三个按钮
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[4]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        title = self.driver.title
        WeatherVedio_page_title = '天气预报视频_全国天气预报视频_CCTV天气预报视频_2345天气预报'
        self.assertEqual(title, WeatherVedio_page_title, msg='页面title与天气视频不符合')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WeatherHistory(self):
        # 点击导航条上的第三个按钮
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[5]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        title = self.driver.title
        WeatherHistory_page_title = '浦东历史天气查询_历史天气预报查询_2345天气预报'
        self.assertEqual(title, WeatherHistory_page_title, msg='页面title与历史天气不符合')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WorldWeather(self):
        # 点击导航条上的第三个按钮
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[6]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        title = self.driver.title
        WorldWeather_page_title = '国际天气预报_全球城市天气预报查询-2345天气预报'
        self.assertEqual(title, WorldWeather_page_title, msg='页面title与国际天气不符合')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_ProfessionWeather(self):
        # 点击导航条上的第三个按钮
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[7]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        title = self.driver.title
        ProfessionWeather_page_title = '全国降水量预报图-2345天气预报'
        self.assertEqual(title, ProfessionWeather_page_title, msg='页面title与专业天气不符合')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)

    def test_homepage_element_WeatherLife(self):
        # 点击导航条上的第三个按钮
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath("//ul[@class='nav-list']/li[8]/a").click()
        # 获取当前所有页面的句柄，并切换至新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.page_handle:
                self.driver.switch_to.window(handle)
            else:
                pass
        title = self.driver.title
        WeatherLife_page_title = '天气资讯-2345天气预报'
        self.assertEqual(title, WeatherLife_page_title, msg='页面title与天气生活不符合')
        # 切换回首页
        self.driver.switch_to.window(self.page_handle)

if __name__ == '__main__':
    unittest.main()