#接口自动化Class文件
import unittest
import requests
import HTMLTestReportCN
class Shangjia_houtai(unittest.TestCase):

    def setUp(self):
        login_url = "https://sso.sanduspace.com/v1/user/login"
        login_data = {'account': 16200000055, 'password': 'f5ad667b8df2239bf2f284e23d106482'}
        login_headers = {'Platform-Code': 'merchantManage'}
        login_response = requests.post(url=login_url, data=login_data, headers=login_headers)
        # print(login_response.status_code)
        # print(login_response.text)
        self.Authorization = login_response.json().get('obj').get('token')
        self.companyId = login_response.json().get('obj').get('companyId')
        self.usgId = login_response.json().get('obj').get('id')

    def test_cabrand(self):
        cabrand_url = "https://system.sanduspace.com/v1/base/franchiser/cabrand"
        cabrand_data = {'companyId': self.companyId, 'msgId': 1}
        cabrand_headers = {'Authorization': self.Authorization, 'Platform-Code': 'merchantManage'}
        cabrand_respones = requests.post(url=cabrand_url, data=cabrand_data, headers=cabrand_headers)
        self.assertEqual(cabrand_respones.status_code,200)
        self.assertEqual(cabrand_respones.json().get('message'),'获取经销商企业默认品牌与可见产品范围成功')
        # print(cabrand_respones.status_code)
        # print(cabrand_respones.text)

    def test_list(self):
        list_url = "https://system.sanduspace.com/v1/base/brand/company/list"
        list_data = {'companyId': self.companyId, 'userId': self.usgId}
        list_headers = {'Authorization': self.Authorization, 'Platform-Code': 'merchantManage'}
        list_response = requests.get(url=list_url, params=list_data, headers=list_headers)
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(list_response.json().get('message'),'ok')
        # print(list_response.status_code)
        # print(list_response.text)

    def test_user(self):
        user_url = "https://system.sanduspace.com/v1/sys/eiu/user"
        user_params = {'id': self.companyId, 'userId': self.usgId}
        user_headers = {'Authorization': self.Authorization, 'Platform-Code': 'merchantManage'}
        user_response = requests.get(url=user_url, params=user_params, headers=user_headers)
        self.assertEqual(user_response.status_code, 200)
        self.assertEqual(user_response.json().get('message'),'详情获取成功!')
        # print(user_response.status_code)
        # print(user_response.text)

    def test_area_list(self):
        area_list_url = "https://system.sanduspace.com/v1/base/area/list"
        area_list_data = {"areaCode": 0, "userId": self.usgId}
        area_list_headers = {'Content-Type': 'application/json', 'Authorization': self.Authorization,
                             'Platform-Code': 'merchantManage'}
        area_list_response = requests.post(url=area_list_url, json=area_list_data, headers=area_list_headers)
        self.assertEqual(area_list_response.status_code, 200)
        self.assertEqual(area_list_response.json().get('message'),'ok')
        self.assertEqual(area_list_response.json().get('totalCount'),34)
        # print(area_list_response.status_code)
        # print(area_list_response.text)


    def test_getCompanyType(self):
        getCompanyType_url = "https://system.sanduspace.com/v1/company/shop/getCompanyType"
        getCompanyType_params = {'companyId': self.companyId, 'userId': self.usgId}
        getCompanyType_headers = {'Content-Type': 'application/json', 'Authorization': self.Authorization,
                                  'Platform-Code': 'merchantManage'}
        getCompanyType_response = requests.post(url=getCompanyType_url, json=getCompanyType_params,headers=getCompanyType_headers)
        self.assertEqual(getCompanyType_response.status_code, 200)
        self.assertEqual(getCompanyType_response.json().get('message'),'ok')
        # print(getCompanyType_response.status_code)
        # print(getCompanyType_response.text)

    def tearDown(self):
        #print('接口测试通过')
        pass

# if __name__ == "__main__":
#     unittest.main()