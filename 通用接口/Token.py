# -*- coding:utf-8 -*-
import requests



def token():

    main_url = 'http://gateway-api.yhtest0.com'
    #_type_equality_funcs = {}

    login_app_auth_url = main_url + "/api/user/1.0/login"
    login_app_auth_headers = {'Content-Type': 'application/x-www-form-urlencoded',"pl":"3","seqNo": "9473ba7bbecf439f872b27a6381a178e"}
    login_app_auth_data = {"account": "13333333333", "pwd": "96e79218965eb72c92a549dd5a330112"}
    login_app_auth_respones = requests.post(url=login_app_auth_url, data=login_app_auth_data,
                                            headers=login_app_auth_headers)
    app_token = login_app_auth_respones.json().get('data').get('token')
    app_uid = login_app_auth_respones.json().get('data').get('uid')

    return app_token,app_uid


