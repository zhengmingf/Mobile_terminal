# encoding: utf-8
"""
@version: v1.0.1
@time: 2020/2/10 19:47
"""

'''
说明：
此文档提供一些独立模块的功能

'''

import unittest,SlidingScreen,time,random,GetXpath,DecoratorF
from appium import webdriver

class TestTools(unittest.TestCase):

    def setUp(self):

        # -----------------------------包名相关信息-----------------
        desired_caps = {'platformName': 'Android',
                        'deviceName': '8RBDU19719000887',
                        'platformVersion': '9.0',
                        'appPackage': 'com.hellotalk',
                        'appActivity': 'com.hellotalkx.modules.sign.ui.LaunchActivity',
                        'autoGrantPermissions': True,  # 解决权限问题
                        # 'unicodeKeyboard':True,# 一定要有该参数，否则测试过程中无法输入中文
                        # 'resetKeyboard':True,#自动化结束后恢复原始数据模样
                        # 'noReset': True,#保证了App测试前不会清除应用数据，缺省是会清除数据的。
                        'newCommandTimeout': 6000  # appium server 认为和客户端之间无响应最大时间 超过将就会停止服务
                        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        print('start HellaTalk App')

    def getXpath_data_list(self,modular):
        '''获得当前sheet下所有的xpath'''
        return GetXpath.GetXpath(modular).getXpath_data()

    def getXpath_data(self,data_list,xpath_data):
        '''找到需要的xpath'''
        for data_json in data_list:
            for key, value in data_json.items():
                if key == xpath_data:
                    return value

    def is_element_exist(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    def login(self,mail_name):
        '''登录，参数为登录账号，密码默认是6个1'''
        xpath_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText"
        xpath_pwd = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText"
        try:
            self.driver.find_element_by_id("com.hellotalk:id/sign_in").click()
        except:
            pass
        self.driver.find_element_by_xpath(xpath_name).send_keys(mail_name) #'zstest001@qq.com'
        self.driver.find_element_by_xpath(xpath_pwd).send_keys('111111')
        time.sleep(3)
        self.driver.find_element_by_id("com.hellotalk:id/btn_login").click()
        try:
            time.sleep(1)
            self.driver.find_element_by_id("com.hellotalk:id/dialog_cancel").click()
        except:
            pass

    def environmental_science(self):
        '''正式环境切换到测试环境，正式环境默认使用到账号是zstest001@qq.com'''
        self.login('zstest001@qq.com')
        # 我
        get_xpath_list = self.getXpath_data_list("me")
        xpath_tab_me = self.getXpath_data(get_xpath_list, "xpath_tab_me")
        try:
            self.driver.find_element_by_xpath(xpath_tab_me).click()
        except:
            time.sleep(5)
            self.driver.find_element_by_xpath(xpath_tab_me).click()

        try:
            self.driver.find_element_by_id("android:id/button1").click()
        except:
            pass
        SlidingScreen.swipe_up(self.driver)
        self.driver.find_element_by_id("com.hellotalk:id/profile_nav_settings").click()
        xpath_setting_dev = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.ListView/android.widget.LinearLayout[9]/android.widget.LinearLayout/android.widget.TextView"
        self.driver.find_element_by_xpath(xpath_setting_dev).click()
        xpath_dev_server = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView[1]"
        self.driver.find_element_by_xpath(xpath_dev_server).click()
        xpath_dev_server_cs = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]"
        self.driver.find_element_by_xpath(xpath_dev_server_cs).click()


    def choice_environmental(self,envir='test'):
        '''切换正式环境和测试环境'''
        if envir == 'test':
            self.environmental_science()
            self.login('cstest001@qq.com')
        else:
            self.login('zstest001@qq.com')
    #----------------测试用例部分-------------------------#

    def test_commont_Release(self):
        '''动态-发布动态'''
        get_xpath_list = self.getXpath_data_list("common")  # 获得xpath
        #self.login('zstest001@qq.com')
        self.environmental_science()
        self.login('cstest001@qq.com')
        common_button = self.getXpath_data(get_xpath_list, "common_button")
        self.driver.find_element_by_xpath(common_button).click()
        try:
            self.driver.find_element_by_id("com.hellotalk:id/title").click()
            time.sleep(1)
            self.driver.back()
        except:
            pass
        #发布动态
        common_send_get_ready = self.getXpath_data(get_xpath_list, "common_send_get_ready")
        for i in range(200):
            try:
                self.driver.find_element_by_xpath(common_send_get_ready).click()
            except:
                time.sleep(10)
                self.driver.find_element_by_xpath(common_send_get_ready).click()

            self.driver.find_element_by_id("com.hellotalk:id/et_content").click()
            self.driver.find_element_by_id("com.hellotalk:id/et_content").send_keys("test ")
            self.driver.find_element_by_id("com.hellotalk:id/action_stream_publish").click()
            time.sleep(5)

    # def test_commont_Del(self):
    #     '''删除动态'''
    #     #我的模块
    #     get_xpath_list = self.getXpath_data_list("me")  # 获得xpath
    #     #切换正式环境和测试环境
    #     try:
    #         self.choice_environmental()#不填参数进入测试环境，填写任意参数进入正式环境
    #     except:
    #         pass
    #     xpath_tab_me = self.getXpath_data(get_xpath_list, "xpath_tab_me")
    #     self.driver.find_element_by_xpath(xpath_tab_me).click()
    #     try:
    #         self.driver.find_element_by_id("android:id/button1").click()
    #     except:
    #         pass
    #     for i in range(10):
    #         self.driver.find_element_by_id("com.hellotalk:id/moment_block_title").click()
    #         time.sleep(1)
    #         xpath_feed_one = self.getXpath_data(get_xpath_list, "xpath_feed_one")
    #         self.driver.find_element_by_xpath(xpath_feed_one).click()
    #         xpath_feed_six = self.getXpath_data(get_xpath_list, "xpath_feed_six")
    #         self.driver.find_element_by_xpath(xpath_feed_six).click()
    #         self.driver.find_element_by_id("android:id/button1").click()
    #         time.sleep(1)
    #         self.driver.back()

        # 删除动态
        # for i in range(51):
        #     el1 = self.driver.find_element_by_xpath(
        #         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageView[4]")
        #     el1.click()
        #     el2 = self.driver.find_element_by_xpath(
        #         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]")
        #     el2.click()
        #     el3 = self.driver.find_element_by_id("android:id/button1")
        #     el3.click()
        #     time.sleep(3)



if __name__ == '__main__':
    unittest.main()

