# encoding: utf-8
"""
@version: v1.0.1
@time: 2020/3/9 19:47
"""
import unittest,os,requests
from datetime import datetime
from GetData import GetData
from RequestAssertion import RequestAssertion
from time import ctime

class TestCaseSet(unittest.TestCase):
    url = GetData()
    respones = RequestAssertion()

    # 第一种断言方式
    def assertionT_other(self, method, url, interfaceName, data=None, headers=None):
        # main_url = TestCaseSet().main_url
        respones = TestCaseSet().respones.request(method, url, data, headers)
        self.assertEqual(respones.status_code, 200)
        self.assertIn(respones.json().get('msg'), ['请求成功'])
        print(TestCaseSet.respones.consuming(respones, interfaceName))


    # 第二种断言方式
    def assertionT(self, method, url, interfaceName, data=None, files=None, json=None, headers=None):
        # main_url = TestCaseSet().main_url
        respones = TestCaseSet().respones.request(method, url, data, files, json, headers)
        self.assertEqual(respones.status_code, 200)
        try:
            self.assertIn(respones.json().get('message'), ['操作成功', 'ok', '成功', '登录成功'])
        except:
            self.assertIn(respones.json().get('msg'), ['操作成功', 'ok', '请求成功', '登录成功'])
        print(TestCaseSet.respones.consuming(respones, interfaceName), '脚本执行时间： %s' % ctime())

    def nowTime(self):
        name = datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace("-", "").replace(":", "").replace(" ","")
        return name  # 获取现在时间

    def upload_pic(self,url='http://play-img3.ssg6.com/file/upload'):
        # 上传图片
        file = open(os.getcwd() + r"\UI\aototestP.jpeg", 'rb')
        files = {'file': ('44ee742ffe4065bae292e34b632c7bdd.jpg', file, 'image/jpeg')}
        pic = TestCaseSet().respones.request('files', url,
                                             files=files).json().get("data")
        file.close()
        return pic


    # def test_index(self):
    #     #     url = TestCaseSet().url.getData("no_login_woman")
    #     #     for u in url:
    #     #         self.assertionT('get', u, u+'趋势汇_未登录_女装')
    #     #
    #     #
    #     # def test_panning_case(self):
    #     #     url = TestCaseSet().url.getData("no_login_panning_case")
    #     #     for u in url:
    #     #         self.assertionT('get', u, u+'趋势汇_企划案')

    def test_login(self):
        # data = {
        #     "username": "13333333330",
        #     "password": "6846860684f05029abccc09a53cd66f1"
        # }
        # self.assertionT('post_x', 'https://testpc.rstrend.com/api/login',
        #                 'https://testpc.rstrend.com/api/login,趋势汇_登录', data)
        url = "http://www.baidu.com"

        re = requests.get("http://www.baidu.com")
        print(re.json())




if __name__ == '__main__':
    unittest.main()