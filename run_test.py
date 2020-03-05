# encoding: utf-8
"""
@version: ??
@author: luke
@contact: 你的邮箱
@site: 
@software: PyCharm
@file: run_test.py
@time: 2020/1/8 20:25
"""

import unittest,HTMLTestReportCN

suite = unittest.TestSuite()#创建测试套件
all_cases = unittest.defaultTestLoader.discover('/Users/mac/PycharmProjects/HelloTalk_UI',pattern='TestCaseSet.py')
#找到某个目录下所有的以test开头的Python文件里面的测试用例
for case in all_cases:
    suite.addTests(case)#把所有的测试用例添加进来

filePath = 'Report/HelloTalk_Android_UI测试报告.html'  #生成报告的路径
fp = open(filePath,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(
    stream=fp,
    title=u'HelloTalk_Android_UI测试结果',
    #description='详细测试用例结果',    #不传默认为空
    tester=u"luke"     #测试人员名字，不传默认为QA
    )
#运行测试用例
runner.run(suite)


