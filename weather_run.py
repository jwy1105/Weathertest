import unittest
from time import ctime
import HTMLTestRunner
from testcase.home_page_testcase import home_page_case_search
from testcase.home_page_testcase import home_page_case_navigation
#构造测试集合(采用手工添加TestSuite的方法，优势：顺序由添加顺序控制)
# suite = unittest.TestSuite()
#
# suite.addTest(home_page_case_navigation.MyTest_Weather_HomePageNavigation("test_homepage_element_HomePage"))
# suite.addTest(home_page_case_navigation.MyTest_Weather_HomePageNavigation("test_homepage_element_NationalWeather"))
# suite.addTest(home_page_case_search.MyTest_Weather_HomePageSearch("test_homepage_SearchCity"))
#构造测试集合(采用discover()方法动态添加，运行顺序根据包、类、方法的命名ASCII码依次排序)
test_dir = (r'D:\Weathertest\testcase')
discover = unittest.defaultTestLoader.discover(test_dir,pattern='home*.py')

if __name__ == '__main__':
    try:
        print(ctime())
        runner = unittest.TextTestRunner()
        runner.run(discover)
        print(ctime())
    except Exception as msg:
        print(msg)