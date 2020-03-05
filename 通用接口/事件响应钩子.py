# encoding: utf-8
"""
@version: ??
@author: terry
@time: 2020/1/10 14:57
"""
'''
用途：把断言放到请求一个函数中执行

'''

import unittest,os,requests,time
from datetime import datetime
from GetData import GetData
from RequestAssertion import RequestAssertion
from time import ctime


class TestCaseSet(unittest.TestCase):
    url = GetData()
    respones = RequestAssertion()

    # 接口耗时
    def consuming(self, respones):
        time.sleep(1)
        return "耗时：Interface time:{}".format(respones.elapsed.total_seconds())

    def get_assertionT(self,respones, *args, **kwargs):
        self.assertEqual(respones.status_code, 200)
        try:
            self.assertIn(respones.json().get('message'), ['操作成功', 'ok', '成功', '登录成功'])
        except:
            self.assertIn(respones.json().get('msg'), ['操作成功', 'ok', '请求成功', '登录成功'])
        print(self.consuming(respones), '脚本执行时间： %s' % ctime())

    def test_login(self):
        data = {
            "username": "13333333330",
            "password": "6846860684f05029abccc09a53cd66f1"
        }
        requests.post(url='https://testpc.rstrend.com/api/login',data=data,hooks=dict(response=self.get_assertionT),verify=False)
        requests.get(url='https://testpc.rstrend.com/api/member/getInfo',hooks=dict(response=self.get_assertionT),verify=False)#verify=False 可以运行的时候开fidder。
        # requests.get(url='https://testpc.rstrend.com/api/base/getBaseData',hooks=dict(response=self.get_assertionT))
        # requests.get(url='https://testpc.rstrend.com/api/base/getChannelList?gender=1',hooks=dict(response=self.get_assertionT))
        # requests.get(url='https://testpc.rstrend.com/api/base/getAdvertisement?code=EXQUISITE_PUSH_LEFT_ROTAION&gender=1',hooks=dict(response=self.get_assertionT))
        # requests.get(url='https://testpc.rstrend.com/api/base/getAdvertisement?code=EXQUISITE_PUSH_RIGHT_FOUR_ROTAION&gender=1',hooks=dict(response=self.get_assertionT))
        # requests.post(url='https://testpc.rstrend.com/api/homepage/index', data={"sex":1}, hooks=dict(response=self.get_assertionT))



if __name__ == '__main__':
    unittest.main()