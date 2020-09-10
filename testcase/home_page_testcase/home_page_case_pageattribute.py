import re
import unittest
# 此py文件用来描写导航条点击跳转的case
from testcase.MyTest_SetAndTear import MyTest_SetAndTear
import time
import lxml
from lxml import html


class MyTest_Weather_HomePageAttribute(MyTest_SetAndTear):
    """首页加载成功后的必要元素判断"""

    def view_homepage(self):
        self.driver.get(self.baseurl)

    def test_homepage_Atr(self):
        self.view_homepage()
        # # 获取当前页面的html
        # html = self.driver.execute_script("return document.documentElement.outerHTML")
        # print(html)

        # 获取页面源代码
        html_source = self.driver.page_source
        MyHtml = lxml.html.fromstring(html_source)
        # 获取标签下所有文本
        items = MyHtml.xpath("//div[@id='y_prodsingle']//text()")
        # 正则 匹配以下内容 \s+ 首空格 \s+$ 尾空格 \n 换行
        pattern = re.compile("^\s+|\s+$|\n")

        clause_text = ""
        for item in items:
            # 将匹配到的内容用空替换，即去除匹配的内容，只留下文本
            line = re.sub(pattern, "", item)
            if len(line) > 0:
                clause_text += line + "\n"
        #
        #
        print(clause_text)


if __name__ == '__main__':
    unittest.main()
