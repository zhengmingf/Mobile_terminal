# encoding: utf-8
"""
@version: ??
@author: terry
@time: 2020/1/11 15:17
"""

import unittest,HTMLTestReportCN
import os

suite = unittest.TestSuite()#创建测试套件
all_cases = unittest.defaultTestLoader.discover('', 'TestCaseUI.py')
#找到某个目录下所有的以test开头的Python文件里面的测试用例
for case in all_cases:
    suite.addTests(case)#把所有的测试用例添加进来

filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\Report\衣图官网UI测试环境测试报告.html'      #生成报告的路径
fp = open(filePath,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(
    stream=fp,
    title=u'衣图官网',
    #description='详细测试用例结果',    #不传默认为空
    tester=u"Terry"     #测试人员名字，不传默认为QA
    )
#运行测试用例
runner.run(suite)
