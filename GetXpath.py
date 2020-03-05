# encoding: utf-8
"""
@version: v1.0.1
@author: terry
@software: PyCharm
@file: GetData.py
@time: 2020/1/7 20:18
"""

import sys,os,json,ast
import xlrd
class GetXpath:
    # os.path.abspath 是获取当前路径，os.path.dirname是获取当前父路径
    parentdir = os.path.dirname(os.path.abspath(__file__))
    def __init__(self,modular,xpath_data = 'button_table_menu'):
        self.modular = modular
        self.xpath_data = xpath_data

    def getXpath_list(self):
        try:
            work = xlrd.open_workbook(GetXpath(self.modular,self.xpath_data).parentdir + '/Data/xpath_hellotalk.xlsx')
        except:
            print('无没有存在参数文件！')
            exit('退出程序，请添加参数文件！')
        sheetName = work.sheet_by_name(self.modular)
        nrows = sheetName.nrows
        interface = []
        for n in range(1, nrows):
            interface.append(sheetName.row_values(n)[0])
        return interface

    def getXpath_data(self):
        self.getXpath_list()

        data_xpath_list = []
        for data_json in self.getXpath_list():
            data_xpath_list.append(json.loads(data_json))

        return data_xpath_list

    def getXpath_json(self):
        self.getXpath_list()

        data_xpath_list = []
        for data_json in self.getXpath_list():
            data_xpath_list.append(json.loads(data_json))

        for data_json in data_xpath_list:
            for key, value in data_json.items():
                if key == self.xpath_data:
                    return value


# aa = GetXpath("search","button_table_menu").getXpath_json()
# print(aa)



