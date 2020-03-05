# encoding: utf-8
"""
@version: v1.0.1
@time: 2020/1/7 19:47
"""
import unittest,SlidingScreen,time,random,GetXpath

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


    def login(self,mail_name):
        '''登录'''
        xpath_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText"
        xpath_pwd = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText"
        try:
            self.driver.find_element_by_id("com.hellotalk:id/sign_in").click()
        except:
            pass
        self.driver.find_element_by_xpath(xpath_name).send_keys(mail_name) #'zstest001@qq.com'
        self.driver.find_element_by_xpath(xpath_pwd).send_keys('111111')
        self.driver.find_element_by_id("com.hellotalk:id/btn_login").click()
        try:
            self.driver.find_element_by_id("com.hellotalk:id/dialog_cancel").click()
        except:
            pass

    def environmental_science(self):
        '''正式环境切换到测试环境'''
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

    def register(self,user_name):
        '''注册'''
        try:
            self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
        except:
            pass
        self.driver.find_element_by_id("com.hellotalk:id/sign_up").click()
        xpath_reginster_mail_button = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout'
        self.driver.find_element_by_xpath(xpath_reginster_mail_button).click()
        xpath_reginster_mail_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText'

        self.driver.find_element_by_xpath(xpath_reginster_mail_name).send_keys(user_name)
        xpath_reginster_pwd = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText'
        self.driver.find_element_by_xpath(xpath_reginster_pwd).send_keys('111111')
        xpath_reginster_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.EditText'
        self.driver.find_element_by_xpath(xpath_reginster_name).send_keys(user_name[:11])
        xpath_reginster_birthday = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView'
        self.driver.find_element_by_xpath(xpath_reginster_birthday).click()
        self.driver.find_element_by_id('android:id/button1').click()
        id_gender = ['com.hellotalk:id/set_female_tx1','com.hellotalk:id/set_male_tx1']
        self.driver.find_element_by_id(random.choice(id_gender)).click()
        self.driver.find_element_by_id('com.hellotalk:id/img_avatar').click()
        xpath_reginster_photo = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]'
        self.driver.find_element_by_xpath(xpath_reginster_photo).click()
        xpath_reginster_photo_next = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.RelativeLayout[1]/android.widget.ImageView'
        self.driver.find_element_by_xpath(xpath_reginster_photo_next).click()
        self.driver.find_element_by_id('com.hellotalk:id/action_ok').click()
        self.driver.find_element_by_id('com.hellotalk:id/action_reg').click()

        #地区
        xpath_reginster_from = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout'
        self.driver.find_element_by_xpath(xpath_reginster_from).click()
        xpath_reginster_from_loc = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView'
        self.driver.find_element_by_xpath(xpath_reginster_from_loc).click()
        #母语
        xpath_reginster_mother_tongue = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout'
        self.driver.find_element_by_xpath(xpath_reginster_mother_tongue).click()
        xpath_reginster_mother_tongue_language = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout'
        self.driver.find_element_by_xpath(xpath_reginster_mother_tongue_language).click()
        #学习语言
        xpath_reginster_learn_pronunciation = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView'
        self.driver.find_element_by_xpath(xpath_reginster_learn_pronunciation).click()
        xpath_reginster_learn_pronunciation_learning = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView'
        self.driver.find_element_by_xpath(xpath_reginster_learn_pronunciation_learning).click()
        #语言级别
        #xpath_reginster_learn_leve = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.LinearLayout'
        #self.driver.find_element_by_xpath(xpath_reginster_learn_leve).click()
        xpath_reginster_learn_leve_next = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.TextView'
        self.driver.find_element_by_xpath(xpath_reginster_learn_leve_next).click()
        #确认
        self.driver.find_element_by_id('com.hellotalk:id/action_reg').click()
        time.sleep(8)
        for i in range(4):
            SlidingScreen.swipe_left(self.driver)
        print('注册完成')

    def char_note(self,get_xpath_list):
        self.driver.find_element_by_id("com.hellotalk:id/msg_input_text").send_keys('自动化测试')
        self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        print("群聊--聊天发送文字")

        self.driver.find_element_by_id("com.hellotalk:id/btn_emoji").click()
        btn_emoji = self.getXpath_data(get_xpath_list, "btn_emoji")
        for i in range(1, 15):
            self.driver.find_element_by_xpath(
                btn_emoji + str(i) + "]/android.widget.FrameLayout/android.widget.TextView").click()
        self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        print("群聊--聊天发送表情测试通过")
        # #语音遇到问题
        # 发送图片等
        self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        btn_add_one = self.getXpath_data(get_xpath_list, "btn_add_one")
        self.driver.find_element_by_xpath(btn_add_one).click()
        self.driver.find_element_by_id("android:id/button1").click()
        for i in range(1, 7):
            btn_add_one_next = self.getXpath_data(get_xpath_list, "btn_add_one_next")
            self.driver.find_element_by_xpath(
                btn_add_one_next + str(i) + ']/android.widget.FrameLayout/android.widget.ImageView').click()
            try:
                self.driver.find_element_by_id("android:id/button1").click()
                break
            except:
                pass

        #self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_id("com.hellotalk:id/send").click()
        print("聊天发送-图片测试通过")
        # 发送-相机
        # self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        btn_add_two = self.getXpath_data(get_xpath_list, "btn_add_two")
        self.driver.find_element_by_xpath(btn_add_two).click()
        btn_add_two_next_one = self.getXpath_data(get_xpath_list, "btn_add_two_next_one")
        self.driver.find_element_by_xpath(btn_add_two_next_one).click()
        try:
            self.driver.find_element_by_id("android:id/button1").click()
        except:
            pass

        self.driver.press_keycode(27)
        self.driver.find_element_by_id("com.huawei.camera:id/done_button").click()
        self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
        print("聊天中发送-相机-拍照完成")
        btn_add_two = self.getXpath_data(get_xpath_list, "btn_add_two")
        self.driver.find_element_by_xpath(btn_add_two).click()
        btn_add_two_next_two = self.getXpath_data(get_xpath_list, "btn_add_two_next_two")
        self.driver.find_element_by_xpath(btn_add_two_next_two).click()
        self.driver.find_element_by_id("com.hellotalk:id/take_camera").click()
        time.sleep(8)
        self.driver.find_element_by_id("com.hellotalk:id/take_camera").click()
        self.driver.find_element_by_id("com.hellotalk:id/sure").click()
        print("聊天中发送-相机-录像完成")
        btn_add_three = self.getXpath_data(get_xpath_list, "btn_add_three")
        self.driver.find_element_by_xpath(btn_add_three).click()
        self.driver.find_element_by_id("android:id/text1").click()
        time.sleep(3)
        self.driver.find_element_by_id("com.hellotalk:id/callend").click()
        print("聊天中发送-群组通话")
        btn_add_four = self.getXpath_data(get_xpath_list, "btn_add_four")
        self.driver.find_element_by_xpath(btn_add_four).click()

        SlidingScreen.swipe_right(self.driver)
        SlidingScreen.swipe_left(self.driver)

        self.driver.find_element_by_id("com.hellotalk:id/pensize").click()

        self.driver.find_element_by_id("com.hellotalk:id/eraser").click()
        self.driver.find_element_by_id("com.hellotalk:id/pencolorcircle").click()
        self.driver.find_element_by_id("com.hellotalk:id/undo").click()
        self.driver.find_element_by_id("com.hellotalk:id/redo").click()
        self.driver.find_element_by_id("com.hellotalk:id/del").click()
        btn_add_four_next_two = self.getXpath_data(get_xpath_list, "btn_add_four_next_two")
        self.driver.find_element_by_xpath(btn_add_four_next_two).click()
        self.driver.find_element_by_id("com.hellotalk:id/del").click()

        btn_add_four_next_one = self.getXpath_data(get_xpath_list, "btn_add_four_next_one")
        self.driver.find_element_by_xpath(btn_add_four_next_one).click()
        self.driver.find_element_by_id("com.hellotalk:id/pensize").click()
        SlidingScreen.swipe_right(self.driver)
        SlidingScreen.swipe_left(self.driver)
        self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        try:
            btn_add_four = self.getXpath_data(get_xpath_list, "btn_add_four")
            self.driver.find_element_by_xpath(btn_add_four).click()
        except:
            self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
            btn_add_four = self.getXpath_data(get_xpath_list, "btn_add_four")
            self.driver.find_element_by_xpath(btn_add_four).click()

        btn_add_four_next_table_two = self.getXpath_data(get_xpath_list, "btn_add_four_next_table_two")
        self.driver.find_element_by_xpath(btn_add_four_next_table_two).click()

        btn_add_four_next_table_one = self.getXpath_data(get_xpath_list, "btn_add_four_next_table_one")
        self.driver.find_element_by_xpath(btn_add_four_next_table_one).click()

        btn_add_four_next_table_two = self.getXpath_data(get_xpath_list, "btn_add_four_next_table_two")
        self.driver.find_element_by_xpath(btn_add_four_next_table_two).click()

        self.driver.find_element_by_id("com.hellotalk:id/pensizetx").click()

        SlidingScreen.swipe_right(self.driver)
        SlidingScreen.swipe_left(self.driver)
        time.sleep(3)

        self.driver.find_element_by_id("com.hellotalk:id/pencolorcircletx").click()
        self.driver.find_element_by_id("com.hellotalk:id/deltext").click()

        SlidingScreen.swipe_right(self.driver)
        SlidingScreen.swipe_left(self.driver)
        time.sleep(3)

        self.driver.find_element_by_id("com.hellotalk:id/entertext").click()
        self.driver.find_element_by_id("com.hellotalk:id/deltx").click()
        btn_add_four_next_two = self.getXpath_data(get_xpath_list, "btn_add_four_next_two")
        self.driver.find_element_by_xpath(btn_add_four_next_two).click()
        self.driver.find_element_by_id("com.hellotalk:id/deltx").click()
        btn_add_four_next_one = self.getXpath_data(get_xpath_list, "btn_add_four_next_one")
        self.driver.find_element_by_xpath(btn_add_four_next_one).click()

        SlidingScreen.swipe_right(self.driver)
        SlidingScreen.swipe_left(self.driver)
        time.sleep(3)

        self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
        print("聊天中发送-涂鸦测试通过")
        btn_add_five = self.getXpath_data(get_xpath_list, "btn_add_five")
        self.driver.find_element_by_xpath(btn_add_five).click()
        btn_add_five_next = self.getXpath_data(get_xpath_list, "btn_add_five_next")
        self.driver.find_element_by_xpath(btn_add_five_next).click()
        self.driver.find_element_by_id("android:id/button2").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        btn_add_five = self.getXpath_data(get_xpath_list, "btn_add_five")
        self.driver.find_element_by_xpath(btn_add_five).click()
        btn_add_five_next = self.getXpath_data(get_xpath_list, "btn_add_five_next")
        self.driver.find_element_by_xpath(btn_add_five_next).click()
        self.driver.find_element_by_id("android:id/button1").click()
        print("聊天中发送-介绍好友测试通过")

        self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        btn_add_six = self.getXpath_data(get_xpath_list, "btn_add_six")
        self.driver.find_element_by_xpath(btn_add_six).click()
        btn_add_six_next = self.getXpath_data(get_xpath_list, "btn_add_six_next")
        self.driver.find_element_by_xpath(btn_add_six_next).click()
        self.driver.find_element_by_id("com.hellotalk:id/card_btn").click()
        print("聊天中发送-发送贺卡测试通过")
        btn_add_seven = self.getXpath_data(get_xpath_list, "btn_add_seven")
        self.driver.find_element_by_xpath(btn_add_seven).click()
        time.sleep(8)
        self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
        print("聊天中发送-发送位置测试通过")
        btn_add_eight = self.getXpath_data(get_xpath_list, "btn_add_eight")
        self.driver.find_element_by_xpath(btn_add_eight).click()
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        self.driver.press_keycode(4)
        print("聊天中发送-发送上课测试通过")

    def create_group_chat(self,get_xpath_list):
        '''创建群聊'''
        self.driver.find_element_by_id("com.hellotalk:id/icon").click()
        create_group_chat = self.getXpath_data(get_xpath_list, "create_group_chat")
        self.driver.find_element_by_xpath(create_group_chat).click()
        self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='互相關注']").click()

        for i in range(1, 4):
            user_layout_xpath = self.getXpath_data(get_xpath_list, "user_layout_xpath")
            self.driver.find_element_by_xpath(
                user_layout_xpath + str(i + 1) + "]/android.widget.RelativeLayout").click()

            user_layout_up_xpath = self.getXpath_data(get_xpath_list, "user_layout_up_xpath")
            self.driver.find_element_by_xpath(user_layout_up_xpath + str(i) + "]/android.widget.ImageView[3]").click()

            self.driver.find_element_by_xpath(
                user_layout_xpath + str(i + 1) + "]/android.widget.RelativeLayout").click()
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        print("建立群聊--测试通过")

    def join_group_char(self,get_xpath_list):
        '''进入群聊界面'''
        self.driver.find_element_by_id("com.hellotalk:id/icon").click()
        create_group_chat = self.getXpath_data(get_xpath_list, "create_group_chat")
        self.driver.find_element_by_xpath(create_group_chat).click()
        self.driver.find_element_by_xpath(
            "//androidx.appcompat.app.ActionBar.Tab[@content-desc='群聊']/android.widget.TextView").click()
        btn_group_char = self.getXpath_data(get_xpath_list, "btn_group_char")
        self.driver.find_element_by_xpath(btn_group_char).click()

    def function_text_test(self,get_xpath_list):
        '''文字功能键'''
        # self.driver.find_element_by_id("com.hellotalk:id/icon").click()
        # create_group_chat = self.getXpath_data(get_xpath_list, "create_group_chat")
        # self.driver.find_element_by_xpath(create_group_chat).click()
        # self.driver.find_element_by_xpath(
        #     "//androidx.appcompat.app.ActionBar.Tab[@content-desc='群聊']/android.widget.TextView").click()
        # btn_group_char = self.getXpath_data(get_xpath_list, "btn_group_char")
        # self.driver.find_element_by_xpath(btn_group_char).click()

        textView_input = self.getXpath_data(get_xpath_list, "textView_input")
        self.driver.find_element_by_id("com.hellotalk:id/msg_input_text").send_keys("测试")
        self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()

        def text_function(xpath):
            time.sleep(3)
            SlidingScreen.long_press(self.driver, textView_input, 10000)
            text_function_up = self.getXpath_data(get_xpath_list, xpath)
            self.driver.find_element_by_xpath(text_function_up).click()


        text_function("text_function_up_one")  # 翻译
        text_function("text_function_up_two")  # 改错
        self.driver.find_element_by_id("com.hellotalk:id/source_text").click()
        self.driver.find_element_by_id("com.hellotalk:id/target_edit").send_keys("modify")
        self.driver.find_element_by_id("com.hellotalk:id/action_edit_wrongtext_send").click()
        self.driver.find_element_by_id("com.hellotalk:id/inclue_text").click()
        self.driver.find_element_by_id("com.hellotalk:id/action_edit_wrongtext_send").click()
        text_function("text_function_up_three")  # 朗读
        self.driver.find_element_by_id("com.hellotalk:id/speak_play_img").click()
        self.driver.find_element_by_id("com.hellotalk:id/speak_repeat_img").click()
        self.driver.press_keycode(4)
        text_function("text_function_up_four")  # 音译
        text_function("text_function_up_eight_more")  # 更多
        self.driver.find_element_by_id("com.hellotalk:id/more_del").click()
        text_function_up_eight_more_one = self.getXpath_data(get_xpath_list, "text_function_up_eight_more_one")
        self.driver.find_element_by_xpath(text_function_up_eight_more_one).click()
        textView_input = self.getXpath_data(get_xpath_list, "textView_input")
        self.driver.find_element_by_id("com.hellotalk:id/msg_input_text").send_keys("测试")
        self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()

        text_function("text_function_up_five")  # 回复
        textView_input = self.getXpath_data(get_xpath_list, "textView_input")
        self.driver.find_element_by_id("com.hellotalk:id/msg_input_text").send_keys("回复内容")
        self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        text_function("text_function_up_six")  # 复制
        text_function("text_function_up_seven")  # 收藏
        print("文字功能键-翻译\改错\朗读\音译\回复\复制\收藏测试通过")

    def quit_group_chat(self):
        '''退出群聊'''
        self.driver.find_element_by_accessibility_id("聊天設置").click()
        SlidingScreen.swipe_up(self.driver)
        self.driver.find_element_by_id("com.hellotalk:id/leave_group__delete_chat").click()
        self.driver.find_element_by_id("android:id/button1").click()

    def group_chat_set(self,get_xpath_list):
        '''群聊搜索、设置'''
        #群聊--搜索
        self.driver.find_element_by_id("com.hellotalk:id/search").click()
        self.driver.find_element_by_id("com.hellotalk:id/edit_text").send_keys("test")
        search_layout_xpath = self.getXpath_data(get_xpath_list, "search_layout_xpath")
        self.driver.find_element_by_xpath(search_layout_xpath).click()

        id_search_list = ['com.hellotalk:id/search_mention_icon','com.hellotalk:id/search_chatfiles_icon',
                          'com.hellotalk:id/search_member_icon','com.hellotalk:id/search_date_icon',
                          'com.hellotalk:id/voice_type','com.hellotalk:id/abc_type',
                          'com.hellotalk:id/translation_type',
                          'com.hellotalk:id/transliteration_type']
        self.driver.find_element_by_id('com.hellotalk:id/search').click()
        for i,id_search in enumerate(id_search_list):
            if i == 2:
                self.driver.find_element_by_id(id_search).click()
                self.driver.find_element_by_id("com.hellotalk:id/inputtext").send_keys('test')
                self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
            self.driver.find_element_by_id(id_search).click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
        print("群聊--搜索测试通过")
        #群聊--设置--减人和加人
        self.driver.find_element_by_id("com.hellotalk:id/chat_setting").click()
        group_char_setting_sub = self.getXpath_data(get_xpath_list, "group_char_setting_sub")
        self.driver.find_element_by_xpath(group_char_setting_sub).click()
        group_char_setting_sub_next = self.getXpath_data(get_xpath_list, "group_char_setting_sub_next")
        self.driver.find_element_by_xpath(group_char_setting_sub_next).click()
        print("群聊--设置--减人通过")

        group_char_setting_odd = self.getXpath_data(get_xpath_list, "group_char_setting_odd")
        self.driver.find_element_by_xpath(group_char_setting_odd).click()

        self.driver.find_element_by_id("com.hellotalk:id/inputtext").send_keys("test")
        self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='互相關注']").click()

        for i in range(2,5):
            user_layout_xpath = self.getXpath_data(get_xpath_list, "user_layout_xpath")
            self.driver.find_element_by_xpath(user_layout_xpath + str(i) + "]/android.widget.RelativeLayout").click()
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        print("群聊--设置--加人通过")
        #群聊--设置--群聊名称
        self.driver.find_element_by_id("com.hellotalk:id/room_name").click()
        self.driver.find_element_by_id("com.hellotalk:id/name").send_keys("test_zdh_char")
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()

        # 群聊--设置--群二维码
        self.driver.find_element_by_id("com.hellotalk:id/group_qrcode").click()
        self.driver.find_element_by_id("com.hellotalk:id/more").click()
        group_char_group_qrcode_pic = self.getXpath_data(get_xpath_list, "group_char_group_qrcode_pic")
        self.driver.find_element_by_xpath(group_char_group_qrcode_pic).click()

        self.driver.find_element_by_id("com.hellotalk:id/more").click()
        group_char_group_qrcode_code = self.getXpath_data(get_xpath_list, "group_char_group_qrcode_code")
        self.driver.find_element_by_xpath(group_char_group_qrcode_code).click()
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()

        self.driver.find_element_by_id("com.hellotalk:id/more").click()
        group_char_group_qrcode_share = self.getXpath_data(get_xpath_list, "group_char_group_qrcode_share")
        self.driver.find_element_by_xpath(group_char_group_qrcode_share).click()
        self.driver.find_element_by_id("com.hellotalk:id/share_cancel").click()
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
        print("群聊--设置--群二维码测试通过")
        #群聊--设置--群管理
        self.driver.find_element_by_id("com.hellotalk:id/manage_options_layout").click()
        self.driver.find_element_by_id("com.hellotalk:id/switch_btn").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.hellotalk:id/switch_btn").click()

        group_char_group_manage_change = self.getXpath_data(get_xpath_list, "group_char_group_manage_change")
        self.driver.find_element_by_xpath(group_char_group_manage_change).click()
        self.driver.find_element_by_id("com.hellotalk:id/inputtext").send_keys("test")
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()

        group_char_group_manage_set = self.getXpath_data(get_xpath_list, "group_char_group_manage_set")
        self.driver.find_element_by_xpath(group_char_group_manage_set).click()
        self.driver.find_element_by_id("com.hellotalk:id/inputtext").send_keys("test")
        group_char_group_manage_set_one = self.getXpath_data(get_xpath_list, "group_char_group_manage_set_one")
        self.driver.find_element_by_xpath(group_char_group_manage_set_one).click()
        group_char_group_manage_set_two = self.getXpath_data(get_xpath_list, "group_char_group_manage_set_two")
        self.driver.find_element_by_xpath(group_char_group_manage_set_two).click()

        group_char_group_manage_set_up_two = self.getXpath_data(get_xpath_list, "group_char_group_manage_set_up_two")
        self.driver.find_element_by_xpath(group_char_group_manage_set_up_two).click()
        group_char_group_manage_set_up_one = self.getXpath_data(get_xpath_list, "group_char_group_manage_set_up_one")
        self.driver.find_element_by_xpath(group_char_group_manage_set_up_one).click()

        group_char_group_manage_set_one = self.getXpath_data(get_xpath_list, "group_char_group_manage_set_one")
        self.driver.find_element_by_xpath(group_char_group_manage_set_one).click()
        group_char_group_manage_set_two = self.getXpath_data(get_xpath_list, "group_char_group_manage_set_two")
        self.driver.find_element_by_xpath(group_char_group_manage_set_two).click()
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
        print("群聊--设置--群管理测试通过（设置了两个管理员）")
        #群聊--设置--群公告
        self.driver.find_element_by_id("com.hellotalk:id/notice_options_layout").click()
        self.driver.find_element_by_id("com.hellotalk:id/et_content").send_keys('群公告内容')
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        self.driver.find_element_by_id("android:id/button2").click()
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        self.driver.find_element_by_id("android:id/button1").click()
        print("群聊--设置--群公告测试通过")
        #群聊--设置--新消息通知、接收语音通话、聊天列表置顶
        id_message_list = ["com.hellotalk:id/new_message_alerts","com.hellotalk:id/voip_allow","com.hellotalk:id/chat_top",]
        for id_message in id_message_list:
            self.driver.find_element_by_id(id_message).click()
            time.sleep(3)
            self.driver.find_element_by_id(id_message).click()
        print("群聊--设置--新消息通知、接收语音通话、聊天列表置顶测试通过")
        #群聊--设置--我的群聊昵称、展示群成员昵称
        SlidingScreen.swipe_up(self.driver)
        SlidingScreen.swipe_up(self.driver)
        self.driver.find_element_by_id("com.hellotalk:id/my_nickname_in_group").click()
        self.driver.find_element_by_id("com.hellotalk:id/name").send_keys("群聊昵称001")
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()

        self.driver.find_element_by_id("com.hellotalk:id/display_group_member_nickname").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.hellotalk:id/display_group_member_nickname").click()
        print("群聊--设置--我的群聊昵称、展示群成员昵称测试通过")
        #群聊--设置--聊天文件、查找聊天内容、查看聊天记录
        self.driver.find_element_by_id("com.hellotalk:id/chatfile_options_layout").click()
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()

        self.driver.find_element_by_id("com.hellotalk:id/search_history_label").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
        self.driver.find_element_by_id("com.hellotalk:id/view_history").click()
        for i in range(1,4):
            view_history_layout = self.getXpath_data(get_xpath_list, "view_history_layout")
            self.driver.find_element_by_xpath(view_history_layout + str(i)+ "]/android.widget.TextView").click()
            self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
        print("群聊--设置--聊天文件、查找聊天内容、查看聊天记录测试通过")
        #群聊--设置--翻译目标语音
        self.driver.find_element_by_id("com.hellotalk:id/language_options_layout").click()
        self.driver.find_element_by_id("com.hellotalk:id/rec_to_layout").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
        self.driver.find_element_by_id("com.hellotalk:id/sent_to_layout").click()
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
        print("群聊--设置--翻译目标语音测试通过")
        #群聊--设置--删除会话、退出群并删除记录
        id_clear_list = ["com.hellotalk:id/clear_history","com.hellotalk:id/leave_group__delete_chat"]
        for id_clear in id_clear_list:
            self.driver.find_element_by_id(id_clear).click()
            self.driver.find_element_by_id("android:id/button2").click()
            self.driver.find_element_by_id(id_clear).click()
            self.driver.find_element_by_id("android:id/button1").click()
        print("群聊--设置--删除会话、退出群并删除记录测试通过")

    def char_search_tab(self,get_xpath_list):


        self.driver.find_element_by_id("com.hellotalk:id/main_etEdit").click()
        self.driver.find_element_by_id("com.hellotalk:id/main_etEdit").send_keys("test")
        self.driver.find_element_by_id("com.hellotalk:id/btn_online").click()
        self.driver.find_element_by_id("com.hellotalk:id/search_edit_clear").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_return").click()
        self.driver.find_element_by_id("com.hellotalk:id/header_text").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_back").click()
        self.driver.find_element_by_accessibility_id("搜索").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_timezone").click()
        self.driver.find_element_by_id("com.hellotalk:id/header_text").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_back").click()
        self.driver.find_element_by_accessibility_id("搜索").click()
        char_search = self.getXpath_data(get_xpath_list, "char_search")
        self.driver.find_element_by_xpath(char_search).click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_1").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_back").click()
        print("聊天模块搜索功能测试通过")
    def voice_function(self):
        '''语音功能'''
        try:
            self.driver.find_element_by_id("com.hellotalk:id/btn_voice").click()
        except:
            self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        time.sleep(6)
        self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
        self.driver.find_element_by_id("com.hellotalk:id/close_voice").click()
        self.driver.find_element_by_id("android:id/button2").click()
        self.driver.find_element_by_id("com.hellotalk:id/close_voice").click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_voice").click()
        time.sleep(6)
        self.driver.find_element_by_id("com.hellotalk:id/record_listen_btn").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.hellotalk:id/record_cancel_btn").click()
        self.driver.find_element_by_id("android:id/button2").click()
        self.driver.find_element_by_id("com.hellotalk:id/record_cancel_btn").click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_voice").click()
        time.sleep(6)
        self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()


    #----------------测试用例部分-------------------------#

    # def test_register_formal(self,):
    #     '''正式环境注册'''
    #     user_name = 'zstest' + str(time.time())[:-6:-1] + '@zdhUI.com'
    #     self.register(user_name)
    #     print('正式环境注册测试通过')
    #
    # def test_register_test(self):
    #     '''测试环境注册'''
    #     self.environmental_science()
    #     user_name = 'cstest' + str(time.time())[:-6:-1] + '@zdhUI.com'
    #     self.register(user_name)
    #     print('测试环境注册测试通过')
    #
    # def test_login_formal(self):
    #     '''正式环境登录'''
    #     self.login('zstest001@qq.com')
    #     print('正式环境登录测试通过')
    #
    # def test_login_test(self):
    #     '''测试环境登录'''
    #     self.environmental_science()
    #     self.login('cstest001@qq.com')
    #     print('测试环境登录测试通过')
    #
    # def test_char(self):
    #     '''测试环境关注，关注页面所有人，如果已经关注了，点击取消，再次关注'''
    #     self.environmental_science()
    #     self.login('cstest001@qq.com')
    #     #点击搜索table
    #     get_xpath_list = self.getXpath_data_list("search")
    #     button_table = self.getXpath_data(get_xpath_list,"button_table")
    #     self.driver.find_element_by_xpath(button_table).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/item_icon").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/search_input").send_keys("test")
    #     self.driver.find_element_by_id("com.hellotalk:id/search_input").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_id("com.hellotalk:id/search_input").send_keys('test')#只有通过这种方式才能搜索到内容
    #     relativeLayout = self.getXpath_data(get_xpath_list,"relativeLayout")
    #
    #     for i in range(1,7):
    #         #关注页面所有人
    #         print('关注人数%i' %i)
    #         elativeLayout_layout = relativeLayout + str(i)+ ']'
    #         self.driver.find_element_by_xpath(elativeLayout_layout).click()
    #         self.driver.find_element_by_id("com.hellotalk:id/profile_img_follow").click()
    #         try:
    #             self.driver.find_element_by_id("android:id/button2").click()#取消按钮
    #             self.driver.find_element_by_id("com.hellotalk:id/profile_img_follow").click()
    #             self.driver.find_element_by_id("android:id/button1").click()#确认按钮
    #             self.driver.find_element_by_id("com.hellotalk:id/profile_img_follow").click()
    #             #self.driver.keyevent(4)
    #         except:
    #             pass
    #         widgetTextView_tip = self.getXpath_data(get_xpath_list,"widgetTextView_tip")
    #         try:
    #             self.driver.find_element_by_xpath(widgetTextView_tip).click()
    #         except:pass
    #         SlidingScreen.swipe_up(self.driver)
    #         self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
    #     print("测试环境关注功能测试通过，用例中关注了7个人")

    def test_char_test(self):
        '''群聊-创建群聊、聊天中发布各种类型的消息、群聊设置'''

        get_xpath_list = self.getXpath_data_list("char")#获得xpath
        #self.environmental_science()
        #self.login('cstest001@qq.com')
        self.login('zstest001@qq.com')
        self.join_group_char(get_xpath_list)#进入群聊界面

        #self.create_group_chat(get_xpath_list)#创建群聊
        #self.char_note(get_xpath_list)#聊天中发送各种类型信息
        # 聊天中发送语音消息
        # try:
        #     self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        # except:
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        #     self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        #
        # self.driver.find_element_by_id("com.hellotalk:id/record_listen_btn").click()
        # time.sleep(6)
        # self.driver.find_element_by_id("com.hellotalk:id/record_cancel_btn").click()
        # time.sleep(6)
        # self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        # self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        # time.sleep(6)
        # self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
        #翻译功能
        try:
            self.driver.find_element_by_id("com.hellotalk:id/btn_translation").click()
        except:
            self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
            self.driver.find_element_by_id("com.hellotalk:id/btn_translate").click()


        self.driver.find_element_by_id("com.hellotalk:id/source_text_input").click()
        self.driver.find_element_by_id("com.hellotalk:id/source_text_input").send_keys("you are the best!")
        self.driver.press_keycode(66)

        self.driver.find_element_by_id("com.hellotalk:id/btn_speak_source").click()
        self.driver.find_element_by_id("com.hellotalk:id/speak_play_img").click()
        self.driver.find_element_by_id("com.hellotalk:id/speak_repeat_img").click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element_by_id("com.hellotalk:id/btn_star_source").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_copy_source").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_send_source").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_translate").click()
        self.driver.find_element_by_id("com.hellotalk:id/source_text_input").click()
        self.driver.find_element_by_id("com.hellotalk:id/source_text_input").send_keys("you are the best!")
        self.driver.press_keycode(66)

        self.driver.find_element_by_id("com.hellotalk:id/btn_transliteration").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_speak_result").click()
        time.sleep(1)
        self.driver.back()
        self. driver.find_element_by_id("com.hellotalk:id/btn_star_result").click()

        self.driver.find_element_by_id("com.hellotalk:id/btn_send_result").click()


        #调试到聊天中使用翻译功能

        #self.function_text_test(get_xpath_list)#文字功能键
    #     #self.quit_group_chat()#退出群聊
    #     #self.group_chat_set(get_xpath_list)#聊天搜索、设置。由于有会员功能，只能在测试环境测试
    #     #self.char_search_tab(get_xpath_list)#聊天列表搜索，此模块有问题，后期再改，包括加语音伙伴、扫二维码
    # def test_commont(self):
    #     '''动态-发布各种类型的动态'''
    #     get_xpath_list = self.getXpath_data_list("common")  # 获得xpath
    #     #self.login('zstest001@qq.com')
    #     self.environmental_science()
    #     self.login('cstest001@qq.com')
    #     common_button = self.getXpath_data(get_xpath_list, "common_button")
    #     self.driver.find_element_by_xpath(common_button).click()
    #     common_tab = self.getXpath_data(get_xpath_list, "common_tab")
    #     for i in range(1,5):
    #         self.driver.find_element_by_xpath(common_tab + str(i) + "]/android.widget.LinearLayout/android.widget.TextView").click()
    #         time.sleep(2)
    #     for i in range(4,6):
    #         self.driver.find_element_by_xpath(common_tab + str(i) + "]/android.widget.LinearLayout/android.widget.TextView").click()
    #         self.driver.find_element_by_xpath(
    #             common_tab + str(i) + "]/android.widget.LinearLayout/android.widget.TextView").click()
    #         time.sleep(2)
    #     print("动态页面-点击栏目（推荐、互助、关注、附近、学习、语音、同学）--测试通过")
    #     #发布动态--文字+图片+话题+位置+表情+语音
    #     common_send_get_ready = self.getXpath_data(get_xpath_list, "common_send_get_ready")
    #     self.driver.find_element_by_xpath(common_send_get_ready).click()
    #     self.driver.find_element_by_id("com.hellotalk:id/et_content").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/et_content").send_keys("you are the best!")
    #     #插入话题
    #     self.driver.find_element_by_id("com.hellotalk:id/moment_tag_view").click()
    #     common_conversation_two = self.getXpath_data(get_xpath_list, "common_conversation_two")
    #     self.driver.find_element_by_xpath(common_conversation_two).click()
    #     common_conversation_one = self.getXpath_data(get_xpath_list, "common_conversation_one")
    #     self.driver.find_element_by_xpath(common_conversation_one).click()
    #     common_conversation_one_next = self.getXpath_data(get_xpath_list, "common_conversation_one_next")
    #     self.driver.find_element_by_xpath(common_conversation_one_next).click()
    #     #加入地址信息
    #     self.driver.find_element_by_id("com.hellotalk:id/moment_location_view").click()
    #     time.sleep(2)
    #     common_send_get_ready_loc_next = self.getXpath_data(get_xpath_list, "common_send_get_ready_loc_next")
    #     self.driver.find_element_by_xpath(common_send_get_ready_loc_next).click()
    #
    #     #插入图片
    #     self.driver.find_element_by_id("com.hellotalk:id/iv_photo").click()
    #     common_send_get_ready_pic = self.getXpath_data(get_xpath_list, "common_send_get_ready_pic")
    #     #插入图片--从相册选取
    #     self.driver.find_element_by_xpath(common_send_get_ready_pic).click()
    #     for i in range(1, 11):
    #         btn_add_one_next = self.getXpath_data(get_xpath_list, "btn_add_one_next")
    #         self.driver.find_element_by_xpath(
    #             btn_add_one_next + str(i) + ']/android.widget.FrameLayout/android.widget.ImageView').click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/send").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_id("com.hellotalk:id/iv_photo").click()
    #     common_send_get_ready_pic_next = self.getXpath_data(get_xpath_list, "common_send_get_ready_pic_next")
    #     self.driver.find_element_by_xpath(common_send_get_ready_pic_next).click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     #插入表情
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_emoji").click()
    #     btn_emoji = self.getXpath_data(get_xpath_list, "btn_emoji")
    #     for i in range(1, 15):
    #         self.driver.find_element_by_xpath(
    #             btn_emoji + str(i) + "]/android.widget.FrameLayout/android.widget.TextView").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_send").click()
    #     #插入涂鸦
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_doogle").click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     #插入语音
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_voice").click()
    #     time.sleep(6)
    #     self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/close_voice").click()
    #     self.driver.find_element_by_id("android:id/button2").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/close_voice").click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_voice").click()
    #     time.sleep(6)
    #     self.driver.find_element_by_id("com.hellotalk:id/record_listen_btn").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_id("com.hellotalk:id/record_cancel_btn").click()
    #     self.driver.find_element_by_id("android:id/button2").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/record_cancel_btn").click()
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_voice").click()
    #     time.sleep(6)
    #     self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
    #     #插入翻译
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_translation").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/cancel_btn").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/source_text_input").send_keys("you are the best!")
    #     self.driver.press_keycode(4)
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_translation").click()
    #     time.sleep(2)
    #
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_speak_source").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/speak_play_img").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/speak_repeat_img").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/speak_play_img").click()
    #     self.driver.back()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_star_source").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_star_source").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_star_source").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_copy_source").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_send_source").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_translation").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_transliteration").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_speak_result").click()
    #     time.sleep(1)
    #     self.driver.back()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_star_result").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_copy_result").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_send_result").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/action_stream_publish").click()
    #     print("动态页面-发布动态（文字+图片+话题+位置+表情+语音+翻译）--测试通过")
    #     #发布动态--图片+涂鸦
    #     common_send_get_ready = self.getXpath_data(get_xpath_list, "common_send_get_ready")
    #     self.driver.find_element_by_xpath(common_send_get_ready).click()
    #     # 插入图片
    #     self.driver.find_element_by_id("com.hellotalk:id/iv_photo").click()
    #     common_send_get_ready_pic = self.getXpath_data(get_xpath_list, "common_send_get_ready_pic")
    #     #插入图片--从相册选取
    #     self.driver.find_element_by_xpath(common_send_get_ready_pic).click()
    #     btn_add_one_next = self.getXpath_data(get_xpath_list, "btn_add_one_next")
    #     for i in range(1, 3):
    #         self.driver.find_element_by_xpath(
    #             btn_add_one_next + str(i) + ']/android.widget.FrameLayout/android.widget.ImageView').click()
    #     self.driver.find_element_by_id("com.hellotalk:id/send").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_id("com.hellotalk:id/iv_photo").click()
    #     common_send_get_ready_pic_next = self.getXpath_data(get_xpath_list, "common_send_get_ready_pic_next")
    #     self.driver.find_element_by_xpath(common_send_get_ready_pic_next).click()
    #     self.driver.press_keycode(27)
    #     self.driver.find_element_by_id("com.huawei.camera:id/done_button").click()
    #     self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
    #     common_send_get_ready_pic_next_one = self.getXpath_data(get_xpath_list, "common_send_get_ready_pic_next_one")
    #     self.driver.find_element_by_xpath(common_send_get_ready_pic_next_one).click()
    #     self.driver.find_element_by_xpath(
    #         btn_add_one_next + '1]/android.widget.FrameLayout/android.widget.ImageView').click()
    #     self.driver.find_element_by_id("com.hellotalk:id/send").click()
    #
    #     #插入涂鸦
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_doogle").click()
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
    #
    #     self.driver.find_element_by_id("com.hellotalk:id/btn_doogle").click()
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
    #     self.driver.find_element_by_id("com.hellotalk:id/action_stream_publish").click()
    #     print("动态页面-发布动态（照相+涂鸦）--测试通过")
    # def test_operation_commont(self):
    #     '''动态-搜索、点赞、评论'''
    #     get_xpath_list = self.getXpath_data_list("common")  # 获得xpath
    #     #self.login('zstest001@qq.com')
    #     self.environmental_science()
    #     self.login('cstest001@qq.com')
    #     common_button = self.getXpath_data(get_xpath_list, "common_button")
    #     self.driver.find_element_by_xpath(common_button).click()




















# if __name__ == '__main__':
#     unittest.main()
