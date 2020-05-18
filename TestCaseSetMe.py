# encoding: utf-8
"""
@version: v1.0.1
@time: 2020/2/10 19:47
"""

'''
说明：
1 函数部分
setUp：初始化设备，包括设备信息，如果需要更改设备、平台等，需要在此处修改，此部分启动App，每次启动重新安装app，后面可以根据业务进行设置，不是所有等操作都需要重新安装app
getXpath_data_list和getXpath_data：获得元素都xpath，统一放在Data文件夹中进行管理
login：登录，参数为登录账号，密码默认是6个1
environmental_science：正式环境切换到测试环境，正式环境默认使用到账号是zstest001@qq.com
choice_environmental: 切换环境，不填参数进入测试环境，填写任意参数进入正式环境
2 测试用例部分
test_me_01：我---编辑个人信息
test_me_02：我--个人档案
test_me_03：我--个人档案--记事本
test_me_04：我--个人档案--设置、推荐
'''
import unittest,SlidingScreen,time,GetXpath,DecoratorF
from appium import webdriver

class TestCaseSet(unittest.TestCase):

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
        # 不填参数进入测试环境，填写任意参数进入正式环境
        # 切换正式环境和测试环境
        try:
            if envir == 'test':
                self.environmental_science()
                self.login('cstest001@qq.com')
            else:
                self.login('zstest001@qq.com')
        except:
            pass
    def get_xpath_me(self):
        get_xpath_list = self.getXpath_data_list("me")  # 获得xpath
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
        return get_xpath_list

    #----------------测试用例部分-------------------------#
    @DecoratorF.operation_times(5)
    def test_me_01(self):
        '''我---编辑个人信息'''
        self.choice_environmental()  # 不填参数进入测试环境，填写任意参数进入正式环境
        get_xpath_list = self.get_xpath_me()
        #编辑个人信息
        self.driver.find_element_by_id("com.hellotalk:id/introduce_view").click()
        #编辑昵称
        self.driver.find_element_by_id("com.hellotalk:id/name_layout").click()
        self.driver.find_element_by_id("com.hellotalk:id/name").click()
        self.driver.find_element_by_id("com.hellotalk:id/name").clear()
        self.driver.find_element_by_id("com.hellotalk:id/name").send_keys("cstest001"+str(time.time())[:-6:-1])
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        print("编辑昵称测试通过")
        #学习语言+位置
        self.driver.find_element_by_id("com.hellotalk:id/language_location_layout").click()
        self.driver.find_element_by_id("com.hellotalk:id/setting_1_more_lang").click()
        self.driver.find_element_by_id("com.hellotalk:id/imageview_dismiss_dialog").click()
        time.sleep(1)
        self.driver.back()
        self. driver.find_element_by_id("com.hellotalk:id/location_layout").click()
        xpath_position_one = self.getXpath_data(get_xpath_list, "xpath_position_one")
        self.driver.find_element_by_xpath(xpath_position_one).click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_id("com.hellotalk:id/location_layout").click()
        xpath_position_two = self.getXpath_data(get_xpath_list, "xpath_position_two")
        self.driver.find_element_by_xpath(xpath_position_two).click()
        self.driver.find_element_by_id("com.hellotalk:id/hidecity").click()
        self.driver.find_element_by_id("com.hellotalk:id/hidecountry").click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_id("com.hellotalk:id/slip_location_off").click()
        self.driver.find_element_by_id("com.hellotalk:id/showage").click()
        self.driver.find_element_by_id("com.hellotalk:id/showonline").click()

        self.driver.find_element_by_id("com.hellotalk:id/slip_dnd_voip").click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_id("com.hellotalk:id/useridsearch").click()
        self.driver.find_element_by_id("com.hellotalk:id/emailsearch").click()
        self.driver.find_element_by_id("com.hellotalk:id/who_can_find_me_layout").click()
        self.driver.find_element_by_id("com.hellotalk:id/on_precise").click()
        self.driver.find_element_by_id("com.hellotalk:id/same_gender_only").click()
        self.driver.find_element_by_id("com.hellotalk:id/on").click()
        self.driver.find_element_by_id("com.hellotalk:id/on_precise").click()
        self.driver.find_element_by_id("com.hellotalk:id/same_gender_only").click()
        self.driver.find_element_by_id("com.hellotalk:id/on").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.hellotalk:id/on").click()
        self.driver.find_element_by_id("com.hellotalk:id/one_month").click()
        self.driver.find_element_by_id("com.hellotalk:id/three_month").click()
        self.driver.find_element_by_id("com.hellotalk:id/one_week").click()
        self.driver.find_element_by_id("com.hellotalk:id/on").click()
        # 隐私模块，进度条拖动的效果暂时没有找到解决进
        time.sleep(1)
        self.driver.back()
        self.driver.find_element_by_id("com.hellotalk:id/hidecity").click()
        self.driver.find_element_by_id("com.hellotalk:id/hidecountry").click()
        self.driver.find_element_by_id("com.hellotalk:id/slip_location_off").click()
        self.driver.find_element_by_id("com.hellotalk:id/showage").click()
        self.driver.find_element_by_id("com.hellotalk:id/showonline").click()
        self.driver.find_element_by_id("com.hellotalk:id/slip_dnd_voip").click()
        self.driver.find_element_by_id("com.hellotalk:id/useridsearch").click()
        self.driver.find_element_by_id("com.hellotalk:id/emailsearch").click()
        SlidingScreen.swipe_up(self.driver)
        self.driver.find_element_by_id("com.hellotalk:id/hide_hisher_moments_layout").click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element_by_id("com.hellotalk:id/hide_my_moments_layout").click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element_by_id("com.hellotalk:id/black_user_list").click()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()

        print("编辑个人信息-学习语言+位置测试通过")
        #我的二维码
        self.driver.find_element_by_id("com.hellotalk:id/my_qrcode").click()
        self.driver.find_element_by_accessibility_id("更多").click()
        xpath_qr_code_one = self.getXpath_data(get_xpath_list, "xpath_qr_code_one")
        self.driver.find_element_by_xpath(xpath_qr_code_one).click()
        self.driver.find_element_by_accessibility_id("更多").click()
        xpath_qr_code_two = self.getXpath_data(get_xpath_list, "xpath_qr_code_two")
        self.driver.find_element_by_xpath(xpath_qr_code_two).click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element_by_accessibility_id("更多").click()
        xpath_qr_code_three = self.getXpath_data(get_xpath_list, "xpath_qr_code_three")
        self.driver.find_element_by_xpath(xpath_qr_code_three).click()
        self.driver.find_element_by_id("com.hellotalk:id/share_cancel").click()
        time.sleep(1)
        self.driver.back()
        print("编辑个人信息-我的二维码测试通过")

        #文字简介
        self.driver.find_element_by_id("com.hellotalk:id/text_introduction_layout").click()
        self.driver.find_element_by_id("com.hellotalk:id/content").click()
        self.driver.find_element_by_id("com.hellotalk:id/content").clear()
        self.driver.find_element_by_id("com.hellotalk:id/content").send_keys("自我介绍"+str(time.time())[:-5:-1])
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        print("编辑个人信息-文字简介测试通过")

        #语音自我介绍
        self.driver.find_element_by_id("com.hellotalk:id/audio_introduction_menu").click()
        time.sleep(10)
        try:
            self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
        except:
            time.sleep(10)
            self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
        time.sleep(5)
        try:
            self.driver.find_element_by_id("com.hellotalk:id/audio_introduction_menu").click()
        except:
            time.sleep(10)
            self.driver.find_element_by_id("com.hellotalk:id/audio_introduction_menu").click()
        self.driver.find_element_by_id("com.hellotalk:id/record_cancel_btn").click()
        self.driver.find_element_by_id("android:id/button1").click()
        print("编辑个人信息-语音自我介绍测试通过")
        #标签-兴趣
        xpath_Interest_one = self.getXpath_data(get_xpath_list, "xpath_Interest_one")
        self.driver.find_element_by_xpath(xpath_Interest_one).click()
        xpath_Interest_two = self.getXpath_data(get_xpath_list, "xpath_Interest_two")
        self.driver.find_element_by_xpath(xpath_Interest_two).click()
        self.driver.find_element_by_id("com.hellotalk:id/content").send_keys("测试兴趣")
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        xpath_Interest_three = self.getXpath_data(get_xpath_list, "xpath_Interest_three")
        self.driver.find_element_by_xpath(xpath_Interest_three).click()
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        xpath_Interest_four = self.getXpath_data(get_xpath_list, "xpath_Interest_four")
        self.driver.find_element_by_xpath(xpath_Interest_four).click()
        xpath_Interest_five = self.getXpath_data(get_xpath_list, "xpath_Interest_five")
        self.driver.find_element_by_xpath(xpath_Interest_five).click()
        xpath_Interest_six = self.getXpath_data(get_xpath_list, "xpath_Interest_six")
        self.driver.find_element_by_xpath(xpath_Interest_six).click()
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        time.sleep(1)
        print("编辑个人信息-标签-兴趣测试通过")
        #旅行国家
        xpath_travel_one = self.getXpath_data(get_xpath_list, "xpath_travel_one")
        self.driver.find_element_by_xpath(xpath_travel_one).click()
        xpath_travel_two = self.getXpath_data(get_xpath_list, "xpath_travel_two")
        self.driver.find_element_by_xpath(xpath_travel_two).click()
        self.driver.find_element_by_id("com.hellotalk:id/content").click()
        self.driver.find_element_by_id("com.hellotalk:id/content").send_keys("旅行国家")
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        xpath_travel_three = self.getXpath_data(get_xpath_list, "xpath_travel_three")
        self.driver.find_element_by_xpath(xpath_travel_three).click()
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        xpath_travel_four = self.getXpath_data(get_xpath_list, "xpath_travel_four")
        self.driver.find_element_by_xpath(xpath_travel_four).click()
        xpath_travel_five = self.getXpath_data(get_xpath_list, "xpath_travel_five")
        self.driver.find_element_by_xpath(xpath_travel_five).click()
        self.driver.find_element_by_id("com.hellotalk:id/check_icon").click()
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        print("编辑个人信息-标签-旅行国家测试通过")
        #HelloTalk ID
        self.driver.find_element_by_id("com.hellotalk:id/hellotalk_id_layout").click()
        time.sleep(1)
        self.driver.back()
        print("编辑个人信息-HelloTalk ID测试通过")
        time.sleep(1)
        self.driver.back()
        print("个人档案-编辑个人信息测试通过")

    # @DecoratorF.operation_times(3)
    # def test_me_02(self):
    #     '''我--个人档案'''
    #     self.choice_environmental()  # 不填参数进入测试环境，填写任意参数进入正式环境
    #     get_xpath_list = self.get_xpath_me()
    #
    #     #个人档案
    #     #个人档案-正在关注
    #     self.driver.find_element_by_id("com.hellotalk:id/following_label").click()
    #     xpath_follow_one = self.getXpath_data(get_xpath_list, "xpath_follow_one")
    #     self.driver.find_element_by_xpath(xpath_follow_one).click()
    #     time.sleep(1)
    #     self.driver.back()
    #     self.driver.find_element_by_id("com.hellotalk:id/img_arrow").click()
    #     xpath_follow_two = self.getXpath_data(get_xpath_list, "xpath_follow_two")
    #     self.driver.find_element_by_xpath(xpath_follow_two).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/img_arrow").click()
    #     xpath_follow_three = self.getXpath_data(get_xpath_list, "xpath_follow_three")
    #     self.driver.find_element_by_xpath(xpath_follow_three).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/img_arrow").click()
    #     xpath_follow_four = self.getXpath_data(get_xpath_list, "xpath_follow_four")
    #     self.driver.find_element_by_xpath(xpath_follow_four).click()
    #     time.sleep(1)
    #     self.driver.back()
    #     print("个人档案-正在关注测试通过")
    #     #个人档案-粉丝
    #     self.driver.find_element_by_id("com.hellotalk:id/follower_layout").click()
    #     xpath_fans_one = self.getXpath_data(get_xpath_list, "xpath_fans_one")
    #     self.driver.find_element_by_xpath(xpath_fans_one).click()
    #     time.sleep(1)
    #     self.driver.back()
    #     xpath_fans_two = self.getXpath_data(get_xpath_list, "xpath_fans_two")
    #     self.driver.find_element_by_xpath(xpath_fans_two).click()
    #     try:
    #         self.driver.find_element_by_id("android:id/button1").click()
    #     except:pass
    #     xpath_fans_two = self.getXpath_data(get_xpath_list, "xpath_fans_two")
    #     self.driver.find_element_by_xpath(xpath_fans_two).click()
    #     time.sleep(1)
    #     self.driver.back()
    #     print("个人档案-粉丝测试通过")
    #     #翻译、音译、语句收藏、语音转文字次数、句子朗读次数、帮伙伴修改句子次数
    #     self.driver.find_element_by_id("com.hellotalk:id/profile_translate_points").click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/profile_transliteration_points").click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/profile_favorite_points").click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/profile_vtt_points").click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/profile_speak_points").click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/profile_correction_points").click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     print("个人档案-翻译次数、音译、语句收藏、语音转文字次数、句子朗读次数、帮伙伴修改句子次数测试通过")
    #     #自我介绍
    #     self.driver.find_element_by_id("com.hellotalk:id/voice_length").click()
    #     time.sleep(6)
    #     self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
    #     time.sleep(30)
    #     self.driver.find_element_by_id("com.hellotalk:id/voice_player_layout").click()
    #     time.sleep(6)
    #     self.driver.find_element_by_id("com.hellotalk:id/tv_signature").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/content").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/content").clear()
    #     self.driver.find_element_by_id("com.hellotalk:id/content").send_keys("自我介绍"+str(time.time())[:-5:-1])
    #     self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/introduce_view").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/audio_introduction_menu").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/record_cancel_btn").click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     time.sleep(1)
    #     self.driver.back()
    #     print("个人档案-自我介绍测试通过")
    #     # #vip会员页面
    #     # self.driver.find_element_by_id("com.hellotalk:id/profile_store_layout").click()
    #     # xpath_vip_one = self.getXpath_data(get_xpath_list, "xpath_vip_one")
    #     # self.driver.find_element_by_xpath(xpath_vip_one).click()
    #     # self.driver.find_element_by_id("com.hellotalk:id/close_btn").click()
    #     # xpath_vip_two = self.getXpath_data(get_xpath_list, "xpath_vip_two")
    #     # self.driver.find_element_by_xpath(xpath_vip_two).click()
    #     # self.driver.find_element_by_id("com.hellotalk:id/close_btn").click()
    #     # xpath_vip_three = self.getXpath_data(get_xpath_list, "xpath_vip_three")
    #     # self.driver.find_element_by_xpath(xpath_vip_three).click()
    #     # self.driver.find_element_by_id("com.hellotalk:id/close_btn").click()
    #     # xpath_vip_four = self.getXpath_data(get_xpath_list, "xpath_vip_four")
    #     # self.driver.find_element_by_xpath(xpath_vip_four).click()
    #     # self.driver.find_element_by_id("com.hellotalk:id/close_btn").click()
    #     # xpath_vip_five = self.getXpath_data(get_xpath_list, "xpath_vip_five")
    #     # self.driver.find_element_by_xpath(xpath_vip_five).click()
    #     # self.driver.find_element_by_id("com.hellotalk:id/close_btn").click()
    #     # time.sleep(1)
    #     # self.driver.back()
    #     # print("个人档案-vip会员测试通过")
    #     #动态
    #     self.driver.find_element_by_id("com.hellotalk:id/moment_block_title").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/action_stream_publish").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/et_content").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/et_content").send_keys("test")
    #     self.driver.find_element_by_id("com.hellotalk:id/et_content").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/action_stream_publish").click()
    #     time.sleep(5)
    #     xpath_feed_one = self.getXpath_data(get_xpath_list, "xpath_feed_one")
    #     try:
    #         self.driver.find_element_by_xpath(xpath_feed_one).click()
    #     except:
    #         time.sleep(20)
    #         self.driver.find_element_by_xpath(xpath_feed_one).click()
    #     xpath_feed_two = self.getXpath_data(get_xpath_list, "xpath_feed_two")
    #     self.driver.find_element_by_xpath(xpath_feed_two).click()
    #     xpath_feed_three = self.getXpath_data(get_xpath_list, "xpath_feed_three")
    #     self.driver.find_element_by_xpath(xpath_feed_three).click()
    #     xpath_feed_four = self.getXpath_data(get_xpath_list, "xpath_feed_four")
    #     self.driver.find_element_by_xpath(xpath_feed_four).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/share_cancel").click()
    #     xpath_feed_five = self.getXpath_data(get_xpath_list, "xpath_feed_five")
    #     self.driver.find_element_by_xpath(xpath_feed_five).click()
    #     xpath_feed_six = self.getXpath_data(get_xpath_list, "xpath_feed_six")
    #     self.driver.find_element_by_xpath(xpath_feed_six).click()
    #     self.driver.find_element_by_id("android:id/button2").click()
    #     xpath_feed_seven = self.getXpath_data(get_xpath_list, "xpath_feed_seven")
    #     self.driver.find_element_by_xpath(xpath_feed_seven).click()
    #     xpath_feed_eight = self.getXpath_data(get_xpath_list, "xpath_feed_eight")
    #     self.driver.find_element_by_xpath(xpath_feed_eight).click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     print("个人档案-动态测试通过")
    #     #收藏
    #     self.driver.find_element_by_id("com.hellotalk:id/profile_favorites_layout").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/action_settings").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/edit_text").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/edit_text").send_keys("test")
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/action_settings").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/text_type").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/search_edit_clear").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/moment_type").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/search_edit_clear").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/abc_type").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/search_edit_clear").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/voice_type").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/search_edit_clear").click()
    #     time.sleep(1)
    #     self.driver.back()
    #     time.sleep(1)
    #     self.driver.back()
    #     print("个人档案-收藏测试通过")
    #
    # @DecoratorF.operation_times(3)
    # def test_me_03(self):
    #     '''我--个人档案--记事本'''
    #     self.choice_environmental()  # 不填参数进入测试环境，填写任意参数进入正式环境
    #     get_xpath_list = self.get_xpath_me()
    #     #记事本
    #     time.sleep(1)
    #     SlidingScreen.swipe_up(self.driver)
    #     self.driver.find_element_by_id("com.hellotalk:id/profile_notepad_layout").click()
    #     #记事本-搜索
    #     self.driver.find_element_by_accessibility_id("搜索").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/edit_text").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/edit_text").send_keys("test")
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     self.driver.find_element_by_accessibility_id("搜索").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/search_chatfiles_icon").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
    #     xpath_note_one = self.getXpath_data(get_xpath_list, "xpath_note_one")
    #     self.driver.find_element_by_xpath(xpath_note_one).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/album_btn_send").click()
    #     xpath_note_two = self.getXpath_data(get_xpath_list, "xpath_note_two")
    #     self.driver.find_element_by_xpath(xpath_note_two).click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #
    #     self.driver.find_element_by_accessibility_id("搜索").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/search_chatfiles_icon").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
    #     xpath_note_one = self.getXpath_data(get_xpath_list, "xpath_note_one")
    #     self.driver.find_element_by_xpath(xpath_note_one).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/album_btn_download").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/album_btn_delete").click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/search_date_icon").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/voice_type").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/abc_type").click()
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/translation_type").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/transliteration_type").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/search_edit_clear").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     #记事本 - 聊天設置
    #     self.driver.find_element_by_accessibility_id("聊天設置").click()
    #     xpath_note_three = self.getXpath_data(get_xpath_list, "xpath_note_three")
    #     self.driver.find_element_by_xpath(xpath_note_three).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/view_history").click()
    #     xpath_note_four = self.getXpath_data(get_xpath_list, "xpath_note_four")
    #     self.driver.find_element_by_xpath(xpath_note_four).click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     xpath_note_five = self.getXpath_data(get_xpath_list, "xpath_note_five")
    #     self.driver.find_element_by_xpath(xpath_note_five).click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     xpath_note_six = self.getXpath_data(get_xpath_list, "xpath_note_six")
    #     self.driver.find_element_by_xpath(xpath_note_six).click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/language_options").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/rec_to_layout").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/sent_to_layout").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #
    #     #聊天中发送消息
    #     get_xpath_list = self.getXpath_data_list("char")
    #     '''聊天中发送文字、表情、图片、相机-拍照、相机-录像、群组通话、涂鸦、介绍好友、贺卡、上课，语音（通话存在bug，暂时去掉）'''
    #     self.driver.find_element_by_id("com.hellotalk:id/msg_input_text").send_keys('自动化测试')
    #     self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
    #     print("群聊--聊天发送文字测试通过")
    #
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_emoji").click()
    #     btn_emoji = self.getXpath_data(get_xpath_list, "btn_emoji")
    #     for i in range(1, 15):
    #         self.driver.find_element_by_xpath(
    #             btn_emoji + str(i) + "]/android.widget.FrameLayout/android.widget.TextView").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
    #     print("群聊--聊天发送表情测试通过")
    #     # 发送图片等
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
    #     btn_add_one = self.getXpath_data(get_xpath_list, "btn_add_one")
    #     self.driver.find_element_by_xpath(btn_add_one).click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     for i in range(1, 7):
    #         btn_add_one_next = self.getXpath_data(get_xpath_list, "btn_add_one_next")
    #         self.driver.find_element_by_xpath(
    #             btn_add_one_next + str(i) + ']/android.widget.FrameLayout/android.widget.ImageView').click()
    #         try:
    #             self.driver.find_element_by_id("android:id/button1").click()
    #             break
    #         except:
    #             pass
    #
    #     self.driver.find_element_by_id("com.hellotalk:id/send").click()
    #     print("聊天发送-图片测试通过")
    #     # 发送-相机
    #     btn_add_two = self.getXpath_data(get_xpath_list, "btn_add_two")
    #     try:
    #         self.driver.find_element_by_xpath(btn_add_two).click()
    #     except:
    #         self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
    #         self.driver.find_element_by_xpath(btn_add_two).click()
    #     btn_add_two_next_one = self.getXpath_data(get_xpath_list, "btn_add_two_next_one")
    #     self.driver.find_element_by_xpath(btn_add_two_next_one).click()
    #     try:
    #         self.driver.find_element_by_id("android:id/button1").click()
    #     except:
    #         pass
    #
    #     self.driver.press_keycode(27)
    #     self.driver.find_element_by_id("com.huawei.camera:id/done_button").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
    #     print("聊天中发送-相机-拍照测试通过")
    #     btn_add_two = self.getXpath_data(get_xpath_list, "btn_add_two")
    #     self.driver.find_element_by_xpath(btn_add_two).click()
    #     btn_add_two_next_two = self.getXpath_data(get_xpath_list, "btn_add_two_next_two")
    #     self.driver.find_element_by_xpath(btn_add_two_next_two).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/take_camera").click()
    #     time.sleep(8)
    #     self.driver.find_element_by_id("com.hellotalk:id/take_camera").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/sure").click()
    #     print("聊天中发送-相机-录像测试通过")
    #
    #     btn_add_three = self.getXpath_data(get_xpath_list, "btn_add_three")
    #     self.driver.find_element_by_xpath(btn_add_three).click()
    #
    #     SlidingScreen.swipe_right(self.driver)
    #     SlidingScreen.swipe_left(self.driver)
    #
    #     self.driver.find_element_by_id("com.hellotalk:id/pensize").click()
    #
    #     self.driver.find_element_by_id("com.hellotalk:id/eraser").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/pencolorcircle").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/undo").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/redo").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/del").click()
    #     btn_add_four_next_two = self.getXpath_data(get_xpath_list, "btn_add_four_next_two")
    #     self.driver.find_element_by_xpath(btn_add_four_next_two).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/del").click()
    #
    #     btn_add_four_next_one = self.getXpath_data(get_xpath_list, "btn_add_four_next_one")
    #     self.driver.find_element_by_xpath(btn_add_four_next_one).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/pensize").click()
    #     SlidingScreen.swipe_right(self.driver)
    #     SlidingScreen.swipe_left(self.driver)
    #     self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
    #     try:
    #         btn_add_three = self.getXpath_data(get_xpath_list, "btn_add_three")
    #         self.driver.find_element_by_xpath(btn_add_three).click()
    #     except:
    #         self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
    #         btn_add_three = self.getXpath_data(get_xpath_list, "btn_add_three")
    #         self.driver.find_element_by_xpath(btn_add_three).click()
    #
    #     btn_add_four_next_table_two = self.getXpath_data(get_xpath_list, "btn_add_four_next_table_two")
    #     self.driver.find_element_by_xpath(btn_add_four_next_table_two).click()
    #
    #     btn_add_four_next_table_one = self.getXpath_data(get_xpath_list, "btn_add_four_next_table_one")
    #     self.driver.find_element_by_xpath(btn_add_four_next_table_one).click()
    #
    #     btn_add_four_next_table_two = self.getXpath_data(get_xpath_list, "btn_add_four_next_table_two")
    #     self.driver.find_element_by_xpath(btn_add_four_next_table_two).click()
    #
    #     self.driver.find_element_by_id("com.hellotalk:id/pensizetx").click()
    #
    #     SlidingScreen.swipe_right(self.driver)
    #     SlidingScreen.swipe_left(self.driver)
    #     time.sleep(3)
    #
    #     self.driver.find_element_by_id("com.hellotalk:id/pencolorcircletx").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/deltext").click()
    #
    #     SlidingScreen.swipe_right(self.driver)
    #     SlidingScreen.swipe_left(self.driver)
    #     time.sleep(3)
    #
    #     self.driver.find_element_by_id("com.hellotalk:id/entertext").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/deltx").click()
    #     btn_add_four_next_two = self.getXpath_data(get_xpath_list, "btn_add_four_next_two")
    #     self.driver.find_element_by_xpath(btn_add_four_next_two).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/deltx").click()
    #     btn_add_four_next_one = self.getXpath_data(get_xpath_list, "btn_add_four_next_one")
    #     self.driver.find_element_by_xpath(btn_add_four_next_one).click()
    #
    #     SlidingScreen.swipe_right(self.driver)
    #     SlidingScreen.swipe_left(self.driver)
    #     time.sleep(3)
    #
    #     self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
    #     print("聊天中发送-涂鸦测试通过")
    #
    #     btn_add_four = self.getXpath_data(get_xpath_list, "btn_add_four")
    #     self.driver.find_element_by_xpath(btn_add_four).click()
    #     self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='互相關注']").click()
    #
    #     btn_add_five_next = self.getXpath_data(get_xpath_list, "btn_add_five_next")
    #     self.driver.find_element_by_xpath(btn_add_five_next).click()
    #     self.driver.find_element_by_id("android:id/button2").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
    #     btn_add_four = self.getXpath_data(get_xpath_list, "btn_add_four")
    #     self.driver.find_element_by_xpath(btn_add_four).click()
    #     self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='互相關注']").click()
    #     btn_add_five_next = self.getXpath_data(get_xpath_list, "btn_add_five_next")
    #     self.driver.find_element_by_xpath(btn_add_five_next).click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     print("聊天中发送-介绍好友测试通过")
    #     btn_add_five = self.getXpath_data(get_xpath_list, "btn_add_five")
    #     try:
    #         self.driver.find_element_by_xpath(btn_add_five).click()
    #     except:
    #         self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
    #         self.driver.find_element_by_xpath(btn_add_five).click()
    #     time.sleep(8)
    #     self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
    #     print("聊天中发送-发送位置测试通过")
    #     self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
    #     time.sleep(6)
    #     self.driver.find_element_by_id("com.hellotalk:id/record_listen_btn").click()
    #     time.sleep(6)
    #     self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
    #     time.sleep(6)
    #     self.driver.find_element_by_id("com.hellotalk:id/record_listen_btn").click()
    #     time.sleep(6)
    #     self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
    #     time.sleep(6)
    #     self.driver.find_element_by_id("com.hellotalk:id/record_cancel_btn").click()
    #     print("聊天中发送-发送语音测试通过")
    #     #翻译
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_translate").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/source_text_input").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/source_text_input").send_keys("you are the best")
    #     self.driver.press_keycode(66)
    #     time.sleep(3)
    #     try:
    #         self.driver.find_element_by_id("com.hellotalk:id/btn_speak_source").click()
    #         time.sleep(1)
    #         self.driver.back()
    #         self.driver.find_element_by_id("com.hellotalk:id/btn_star_source").click()
    #         self.driver.find_element_by_id("com.hellotalk:id/btn_copy_source").click()
    #         self.driver.find_element_by_id("com.hellotalk:id/btn_send_source").click()
    #     except:
    #         self.driver.find_element_by_id("com.hellotalk:id/action_favorites").click()
    #
    #
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     print('聊天中发送-翻译功能测试通过')
    #
    #
    #     self.driver.find_element_by_id("com.hellotalk:id/profile_nav_translate").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/source_text_input").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/source_text_input").send_keys("you are the best")
    #     self.driver.press_keycode(66)
    #     time.sleep(8)
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_transliteration").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_speak_result").click()
    #     time.sleep(1)
    #     self.driver.back()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_star_result").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_copy_result").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     print('个人档案-翻译助手测试通过')
    #
    # @DecoratorF.operation_times(3)
    # def test_me_04(self):
    #     '''我--个人档案--设置、推荐'''
    #     self.choice_environmental()  # 不填参数进入测试环境，填写任意参数进入正式环境
    #     get_xpath_list = self.get_xpath_me()
    #     #设置
    #     #设置-账户
    #     time.sleep(1)
    #     SlidingScreen.swipe_up(self.driver)
    #     self.driver.find_element_by_id("com.hellotalk:id/profile_nav_settings").click()
    #     time.sleep(1)
    #     xpath_setting_one = self.getXpath_data(get_xpath_list, "xpath_setting_one")
    #     self.driver.find_element_by_xpath(xpath_setting_one).click()
    #     xpath_setting_two = self.getXpath_data(get_xpath_list, "xpath_setting_two")
    #     self.driver.find_element_by_xpath(xpath_setting_two).click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     xpath_setting_three = self.getXpath_data(get_xpath_list, "xpath_setting_three")
    #     self.driver.find_element_by_xpath(xpath_setting_three).click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     xpath_setting_four = self.getXpath_data(get_xpath_list, "xpath_setting_four")
    #     self.driver.find_element_by_xpath(xpath_setting_four).click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     # 设置-新消息通知
    #     xpath_setting_five = self.getXpath_data(get_xpath_list, "xpath_setting_five")
    #     self.driver.find_element_by_xpath(xpath_setting_five).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/moments_comments_cb").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/follow_cb").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/moments_comments_cb").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/follow_cb").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/new_message_alerts").click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/new_message_alerts").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/disturb_layout").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/on").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.hellotalk:id/on").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.hellotalk:id/on").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.hellotalk:id/on").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/message_preview").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.hellotalk:id/message_preview").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/notification_sys_settings").click()
    #     xpath_setting_six = self.getXpath_data(get_xpath_list, "xpath_setting_six")
    #     self.driver.find_element_by_xpath(xpath_setting_six).click()
    #     self.driver.find_element_by_id("android:id/switch_widget").click()
    #     xpath_setting_more_one = self.getXpath_data(get_xpath_list, "xpath_setting_more_one")
    #     self.driver.find_element_by_xpath(xpath_setting_more_one).click()
    #     xpath_setting_more_two = self.getXpath_data(get_xpath_list, "xpath_setting_more_two")
    #     self.driver.find_element_by_xpath(xpath_setting_more_two).click()
    #     xpath_setting_more_three = self.getXpath_data(get_xpath_list, "xpath_setting_more_three")
    #     self.driver.find_element_by_xpath(xpath_setting_more_three).click()
    #     xpath_setting_more_four = self.getXpath_data(get_xpath_list, "xpath_setting_more_four")
    #     self.driver.find_element_by_xpath(xpath_setting_more_four).click()
    #     xpath_setting_more_five = self.getXpath_data(get_xpath_list, "xpath_setting_more_five")
    #     self.driver.find_element_by_xpath(xpath_setting_more_five).click()
    #     self.driver.find_element_by_xpath(xpath_setting_more_one).click()
    #     self.driver.find_element_by_xpath(xpath_setting_more_two).click()
    #     self.driver.find_element_by_xpath(xpath_setting_more_three).click()
    #     self.driver.find_element_by_xpath(xpath_setting_more_four).click()
    #     self.driver.find_element_by_xpath(xpath_setting_more_five).click()
    #
    #     xpath_setting_more_six = self.getXpath_data(get_xpath_list, "xpath_setting_more_six")
    #     xpath_setting_more_seven = self.getXpath_data(get_xpath_list, "xpath_setting_more_seven")
    #
    #     for i in range(3,0,-1):
    #         self.driver.find_element_by_xpath(xpath_setting_more_six).click()
    #         self.driver.find_element_by_xpath(xpath_setting_more_seven + str(i)+"]/android.widget.LinearLayout/android.widget.RadioButton").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上导航").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     print('个人档案-设置测试通过')
    #     #推荐
    #     self.driver.find_element_by_id("com.hellotalk:id/recommend").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/item_icon").click()
    #     time.sleep(3)
    #     xpath_recommend = self.getXpath_data(get_xpath_list, "xpath_recommend")
    #     self.driver.find_element_by_xpath(xpath_recommend).click()
    #     time.sleep(1)
    #     self.driver.find_element_by_accessibility_id("向上瀏覽").click()
    #     print('个人档案-推荐测试通过')

if __name__ == '__main__':
    unittest.main()
