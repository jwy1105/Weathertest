import unittest
import time
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header

import os
from testcase.home_page_testcase import home_page_case_search
from testcase.home_page_testcase import home_page_case_navigation

# 构造测试集合(采用手工添加TestSuite的方法，优势：顺序由添加顺序控制)
# suite = unittest.TestSuite()
#
# suite.addTest(home_page_case_navigation.MyTest_Weather_HomePageNavigation("test_homepage_element_HomePage"))
# suite.addTest(home_page_case_navigation.MyTest_Weather_HomePageNavigation("test_homepage_element_NationalWeather"))
# suite.addTest(home_page_case_search.MyTest_Weather_HomePageSearch("test_homepage_SearchCity"))

# #构造测试集合(采用discover()方法动态添加，运行顺序根据包、类、方法的命名ASCII码依次排序)
# test_dir = (r'D:\Weathertest\testcase')
# discover = unittest.defaultTestLoader.discover(test_dir,pattern='home*.py')
#
# if __name__ == '__main__':
#     try:
#         print(ctime())
#         runner = unittest.TextTestRunner()
#         runner.run(discover)
#         print(ctime())
#     except Exception as msg:
#         print(msg)

# #构造测试集合(采用discover()方法动态添加，运行顺序根据包、类、方法的命名ASCII码依次排序,并且使用HTMLTestRun)


def sendmail(new_file):
    """获取最新文件new_file并且发送至邮箱"""
    # 获取最新文件new_file
    f = open(new_file, 'rb')
    mail_body = f.read()
    f.close()

    # 进行邮箱的连接，发送邮件并退出
    sender = '632101461@qq.com'
    receivers = ['m13975238911@163.com', 'jinwy@2345.com']
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['From'] = Header('jwy', 'utf-8')
    msg['To'] = Header('jwy2', 'utf-8')
    msg['Subject'] = Header('TestCaseReport', 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")  # 连接QQ邮箱
    smtp.login("632101461@qq.com", "wwirapvhwfuwbccb")
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()
    print('TestCaseReport发送成功')


def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))
    new_file = os.path.join(test_report, lists[-1])
    print(new_file)
    return new_file


if __name__ == '__main__':
    test_dir = 'D:\\Weathertest\\testcase'
    test_report = 'D:\\Weathertest\\test_report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='home*.py')

    # 定义报告的存放路径
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = 'D:\\Weathertest\\test_report\\' + now + 'result.html'
    fp = open(filename, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='天气测试报告',
                            description='用例执行情况：')
    runner.run(discover)
    fp.close()

    NewReport = new_report(test_report)
    sendmail(NewReport) #发送测试报告
