# -*- coding:utf-8 -*-
import requests
import time

class RequestAssertion():

    def request(self,method,url,data=None,files=None,json=None,headers=None):
        if data is None:
            data={}
        if files is None:
            files={}
        if headers is None:
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}

        respones = {}
        if method == "get":
            respones = requests.get(url=url, headers=headers)
        elif method == "post_x":
            respones = requests.post(url=url, data=data, headers=headers,verify=False)
        elif method == "post":
            respones = requests.post(url=url,json=json, headers=headers)
        elif method == "put":
            respones = requests.put(url=url, json=data, headers=headers)
        elif method == "patch":
            respones = requests.patch(url=url, json=data, headers=headers)
        elif method == "del":
            respones = requests.delete(url=url, json=data, headers=headers)
        elif method == "files":
            respones = requests.post(url=url, data=data,files=files, headers=headers)
        return respones

    # 接口耗时
    def consuming(self,respones,interfaceName):
        time.sleep(1)
        return interfaceName + ",耗时：Interface time:{}".format(respones.elapsed.total_seconds())

    # def request(self,method,url,data=None,headers=None):
    #     if data is None:
    #         data={}
    #     if headers is None:
    #         #headers={}
    #         headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    #
    #     respones = {}
    #     if method == "get":
    #         respones = requests.get(url=url, headers=headers)
    #     elif method == "post_x":
    #         respones = requests.post(url=url, data=data, headers=headers)
    #     elif method == "post":
    #         respones = requests.post(url=url,json=data, headers=headers)
    #     elif method == "put":
    #         respones = requests.put(url=url, json=data, headers=headers)
    #     elif method == "patch":
    #         respones = requests.patch(url=url, json=data, headers=headers)
    #     elif method == "del":
    #         respones = requests.delete(url=url, json=data, headers=headers)
    #     return respones
    #
    # # 接口耗时
    # def consuming(self,respones,interfaceName):
    #     time.sleep(1)
    #     return interfaceName + ",Interface time:{}".format(respones.elapsed.total_seconds())







