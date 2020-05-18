import unittest,SlidingScreen,time,random,GetXpath
from appium import webdriver

class TestCaseSet(unittest.TestCase):

    def setUp(self):

        # -----------------------------包名相关信息-----------------
        desired_caps = {'platformName': 'Android',
                        'deviceName': '8RBDU19719000887',
                        'platformVersion': '9.0',
                        'appPackage': 'com.hellotalk.aigrammar',
                        'appActivity': 'com.hellotalk.aigrammar.MainActivity',
                        'autoGrantPermissions': True,  # 解决权限问题
                        # 'unicodeKeyboard':True,# 一定要有该参数，否则测试过程中无法输入中文
                        # 'resetKeyboard':True,#自动化结束后恢复原始数据模样
                        # 'noReset': True,#保证了App测试前不会清除应用数据，缺省是会清除数据的。
                        'newCommandTimeout': 6000  # appium server 认为和客户端之间无响应最大时间 超过将就会停止服务
                        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        print('start HellaTalk App')


    def test_01(self):
        # el1 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")
        # el1.click()
        # el2 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText")
        # el2.click()
        # self.driver.press_keycode(29)
        #self.driver.find_element_by_name("HelloTalk登录").click()
        aa = self.driver.find_element_by_android_uiautomator('new UiSelector().text("HelloTalk登录")')
        print(aa)


