import requests
url = 'https://api-push.vivo.com.cn/message/auth'
headers = {"content":"Content-Type:application/json","charset":"UTF-8"}
data = {

      "appId":18776,

        "appKey":"1c3ddb63-2777-42ea-9bf5-2b1c13cba700",

      "timestamp":1586947768000,

        "sign":"699FBD34D50A2DC2E668545C60107B6F".lower()

}

re = requests.post(url=url,headers=headers,json=data)
print(re.status_code)
print(re.text)

url = 'https://api-push.vivo.com.cn/message/send'
headers = {"content":"Content-Type:application/json","charset":"UTF-8","authToken":"840c7a9c-b8d0-4c69-b113-f36a6f636332"}
data = {

        "regId":"15826821410491877679648",

    "notifyType":1,

    "title":"标题1",

    "content":"内容1",

    "timeToLive":86400,

    "skipType":2,

        "skipContent":"http://www.vivo.com",

      "networkType":"1",

    "clientCustomMap":{

            "key1":"vlaue1",

            "key2":"vlaue2"

    },

    "extra":{

            "callback":"http://www.vivo.com",

            "callback.param":"vivo"

    },

        "requestId":"25509283-3767-4b9e-83fe-b6e55ac6b123"

}
re = requests.post(url=url,headers=headers,json=data)
print(re.status_code)
print(re.text)