class ReadFile(object):

    def ReadWeather_HomePage_Atr(self, Filename):
        """读取数据，构建断言对象"""
        with open('G:\\TestCaseData\\%s' % Filename, 'r') as f:
            MyTestData = f.readlines()
            # 去除list中的\n
            MyTestData = ''.join(MyTestData).strip('\n')
        return MyTestData


if __name__ == '__main__':
    print(ReadFile().ReadWeather_HomePage_Atr('WeatherHomePageAtr.csv'))
