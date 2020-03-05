# encoding: utf-8
"""
@version: v1.0.1
@author: terry
@software: PyCharm
@file: GetData.py
@time: 2020/1/7 20:18
"""

import sys,os
import xlrd
class GetData:
    # os.path.abspath 是获取当前路径，os.path.dirname是获取当前父路径
    parentdir = os.path.dirname(os.path.abspath(__file__))

    def getData(self, modular):
        try:
            work = xlrd.open_workbook(GetData().parentdir + '\Data\DataUrl.xlsx')
        except:
            print('无没有存在参数文件！')
            exit('退出程序，请添加参数文件！')
        sheetName = work.sheet_by_name(modular)
        nrows = sheetName.nrows
        interface = []
        for n in range(1, nrows):
            interface.append(sheetName.row_values(n)[0])

        # interface = sheetName.row_values(1)
        # url= interface[n]
        return interface
# aa = GetData().getData("odds_setup")
# #print(aa)
# for i in aa:
#     print(type(i))
