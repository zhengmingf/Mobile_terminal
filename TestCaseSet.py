# encoding: utf-8
"""
@version: v1.0.1
@time: 2020/2/10 19:47
"""

'''
说明：
功能模块以函数到形式放在测试用例的前面部分，测试用例用到到地方，自行调用
1 函数部分
setUp：初始化设备，包括设备信息，如果需要更改设备、平台等，需要在此处修改，此部分启动App，每次启动重新安装app，后面可以根据业务进行设置，不是所有等操作都需要重新安装app
getXpath_data_list和getXpath_data：获得元素都xpath，统一放在Data文件夹中进行管理
login：登录，参数为登录账号，密码默认是6个1
environmental_science：正式环境切换到测试环境，正式环境默认使用到账号是zstest001@qq.com
register：注册
char_note：聊天中发送文字、表情、图片、相机-拍照、相机-录像、群组通话、涂鸦、介绍好友、贺卡、上课
create_group_chat：创建群聊（对账号对要求是必须有三个互相关注对好友）
join_group_char：直接进入群聊界面
function_text_test：文字功能键，文字功能键-翻译\改错\朗读\音译\回复\复制\收藏
quit_group_chat：退出群聊（自动化产生大量群，用于清理数据用）
group_chat_set：群聊设置所有功能，最后是退出群聊。
char_search_tab：聊天模块对搜索功能
voice_function：语音功能（此部分存在问题，没有被单独调用，先留着）
choice_environmental: 切换环境，不填参数进入测试环境，填写任意参数进入正式环境
2 测试用例部分
test_register_formal：正式环境注册
test_register_test：测试环境注册（从功能讲，应该只要一个注册就可以，这个作用方便以后创建大量用户）
test_login_formal：正式环境登录
test_login_test：测试环境登录（从功能讲，也是应该只要一个登录就可以，主要是有些功能不方便在正式环境操作）
test_char：测试环境关注，关注页面所有人，如果已经关注了，点击取消，再次关注
test_char_test：群聊-创建群聊、聊天中发布各种类型的消息、群聊设置
test_commont：动态-发布各种类型的动态

'''

import unittest,SlidingScreen,time,random,GetXpath,DecoratorF
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
        '''聊天中发送文字、表情、图片、相机-拍照、相机-录像、群组通话、涂鸦、介绍好友、贺卡、上课，语音（通话存在bug，暂时去掉）'''
        self.driver.find_element_by_id("com.hellotalk:id/msg_input_text").send_keys('自动化测试')
        self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        print("群聊--聊天发送文字测试通过")

        self.driver.find_element_by_id("com.hellotalk:id/btn_emoji").click()
        btn_emoji = self.getXpath_data(get_xpath_list, "btn_emoji")
        for i in range(1, 15):
            self.driver.find_element_by_xpath(
                btn_emoji + str(i) + "]/android.widget.FrameLayout/android.widget.TextView").click()
        self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        print("群聊--聊天发送表情测试通过")
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


        self.driver.find_element_by_id("com.hellotalk:id/send").click()
        print("聊天发送-图片测试通过")
        #发送-相机
        btn_add_two = self.getXpath_data(get_xpath_list, "btn_add_two")
        try:
            self.driver.find_element_by_xpath(btn_add_two).click()
        except:
            self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
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
        print("聊天中发送-相机-拍照测试通过")
        btn_add_two = self.getXpath_data(get_xpath_list, "btn_add_two")
        self.driver.find_element_by_xpath(btn_add_two).click()
        btn_add_two_next_two = self.getXpath_data(get_xpath_list, "btn_add_two_next_two")
        self.driver.find_element_by_xpath(btn_add_two_next_two).click()
        self.driver.find_element_by_id("com.hellotalk:id/take_camera").click()
        time.sleep(8)
        self.driver.find_element_by_id("com.hellotalk:id/take_camera").click()
        self.driver.find_element_by_id("com.hellotalk:id/sure").click()
        print("聊天中发送-相机-录像测试通过")
        #聊天中发送通话暂时去掉
        # btn_add_three = self.getXpath_data(get_xpath_list, "btn_add_three")
        # self.driver.find_element_by_xpath(btn_add_three).click()
        # time.sleep(1)
        # self.driver.find_element_by_id("android:id/text1").click()
        # time.sleep(3)
        # self.driver.find_element_by_id("com.hellotalk:id/callend").click()
        # print("聊天中发送-群组通话测试通过")
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
        self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='互相關注']").click()


        btn_add_five_next = self.getXpath_data(get_xpath_list, "btn_add_five_next")
        self.driver.find_element_by_xpath(btn_add_five_next).click()
        self.driver.find_element_by_id("android:id/button2").click()
        self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        btn_add_five = self.getXpath_data(get_xpath_list, "btn_add_five")
        self.driver.find_element_by_xpath(btn_add_five).click()
        self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='互相關注']").click()
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
        try:
            time.sleep(1)
            self.driver.back()
        except:
            self.driver.press_keycode(4)
        print("聊天中发送-发送上课测试通过")

        try:
            self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
            time.sleep(6)
        except:
            self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
            self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()

        self.driver.find_element_by_id("com.hellotalk:id/record_listen_btn").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
        self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        time.sleep(6)
        self.driver.find_element_by_id("com.hellotalk:id/record_listen_btn").click()
        time.sleep(3)
        self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
        self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        time.sleep(6)
        self.driver.find_element_by_id("com.hellotalk:id/record_cancel_btn").click()
        print("聊天中发送-发送语音测试通过")
        # 翻译
        self.driver.find_element_by_id("com.hellotalk:id/btn_translate").click()
        btn_group_char_one = self.getXpath_data(get_xpath_list, "btn_group_char_one")
        self.driver.find_element_by_xpath(btn_group_char_one).click()
        self.driver.find_element_by_id("com.hellotalk:id/source_text_input").click()
        self.driver.find_element_by_id("com.hellotalk:id/source_text_input").send_keys("you are the best")
        self.driver.press_keycode(66)
        time.sleep(3)
        try:
            self.driver.find_element_by_id("com.hellotalk:id/btn_speak_source").click()
            time.sleep(1)
            self.driver.back()
            self.driver.find_element_by_id("com.hellotalk:id/btn_star_source").click()
            self.driver.find_element_by_id("com.hellotalk:id/btn_copy_source").click()
            self.driver.find_element_by_id("com.hellotalk:id/btn_send_source").click()
            self. driver.find_element_by_id("com.hellotalk:id/btn_translate").click()

            btn_group_char_one = self.getXpath_data(get_xpath_list, "btn_group_char_one")
            self.driver.find_element_by_xpath(btn_group_char_one).click()

            self.driver.find_element_by_id("com.hellotalk:id/source_text_input").click()
            self.driver.find_element_by_id("com.hellotalk:id/source_text_input").send_keys("you are the best")
            self.driver.press_keycode(66)
            self.driver.find_element_by_id("com.hellotalk:id/btn_transliteration").click()
            self.driver.find_element_by_id("com.hellotalk:id/btn_speak_result").click()
            time.sleep(1)
            self.driver.back()
            self.driver.find_element_by_id("com.hellotalk:id/btn_star_result").click()
            self.driver.find_element_by_id("com.hellotalk:id/btn_copy_result").click()
            self.driver.find_element_by_id("com.hellotalk:id/btn_send_result").click()
        except:
            self.driver.find_element_by_id("com.hellotalk:id/action_favorites").click()



    def create_group_chat(self,get_xpath_list):
        '''创建群聊'''
        self.driver.find_element_by_id("com.hellotalk:id/icon").click()
        time.sleep(1)
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
        time.sleep(1)
        self.driver.find_element_by_id("com.hellotalk:id/icon").click()
        time.sleep(1)
        create_group_chat = self.getXpath_data(get_xpath_list, "create_group_chat")
        self.driver.find_element_by_xpath(create_group_chat).click()
        self.driver.find_element_by_xpath(
            "//androidx.appcompat.app.ActionBar.Tab[@content-desc='群聊']/android.widget.TextView").click()
        btn_group_char = self.getXpath_data(get_xpath_list, "btn_group_char")
        self.driver.find_element_by_xpath(btn_group_char).click()

    def function_text_test(self,get_xpath_list):
        '''文字功能键'''
        # self.driver.find_element_by_id("com.hellotalk:id/icon").click()
        #time.sleep(1)
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
            time.sleep(2)
            SlidingScreen.long_press(self.driver, textView_input, 10000)
            text_function_up = self.getXpath_data(get_xpath_list, xpath)
            self.driver.find_element_by_xpath(text_function_up).click()


        text_function("text_function_up_one")  # 翻译
        print("翻译功能")
        text_function("text_function_up_two")  # 改错
        print("改错功能")
        self.driver.find_element_by_id("com.hellotalk:id/source_text").click()
        self.driver.find_element_by_id("com.hellotalk:id/target_edit").send_keys("modify")
        self.driver.find_element_by_id("com.hellotalk:id/action_edit_wrongtext_send").click()
        self.driver.find_element_by_id("com.hellotalk:id/inclue_text").click()
        self.driver.find_element_by_id("com.hellotalk:id/action_edit_wrongtext_send").click()
        text_function("text_function_up_three")  # 朗读
        print("朗读功能")
        self.driver.find_element_by_id("com.hellotalk:id/speak_play_img").click()
        self.driver.find_element_by_id("com.hellotalk:id/speak_repeat_img").click()
        self.driver.press_keycode(4)
        text_function("text_function_up_four")  # 音译
        print("音译功能")
        text_function("text_function_up_eight_more")  # 更多
        print("更多按钮功能")
        self.driver.find_element_by_id("com.hellotalk:id/more_del").click()
        text_function_up_eight_more_one = self.getXpath_data(get_xpath_list, "text_function_up_eight_more_one")
        self.driver.find_element_by_xpath(text_function_up_eight_more_one).click()
        textView_input = self.getXpath_data(get_xpath_list, "textView_input")
        self.driver.find_element_by_id("com.hellotalk:id/msg_input_text").send_keys("测试")
        self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()

        text_function("text_function_up_five")  # 回复
        print("回复功能")
        textView_input = self.getXpath_data(get_xpath_list, "textView_input")
        self.driver.find_element_by_id("com.hellotalk:id/msg_input_text").send_keys("回复内容")
        self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        text_function("text_function_up_six")  # 复制
        print("复制功能")
        text_function("text_function_up_seven")  # 收藏
        print("收藏功能")
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
        '''聊天模块搜索'''
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

    def choice_environmental(self,envir='test'):
        '''切换正式环境和测试环境'''
        if envir == 'test':
            self.environmental_science()
            self.login('cstest001@qq.com')
        else:
            self.login('zstest001@qq.com')



    #----------------测试用例部分-------------------------#

    # def test_register_formal(self,):
    #     '''正式环境注册'''
    #     user_name = 'zstest' + str(time.time())[:-6:-1] + '@zdhUI.com'
    #     self.register(user_name)
    #     print('正式环境注册测试通过')

    # def test_register_test(self):
    #     '''测试环境注册'''
    #     self.environmental_science()
    #     user_name = 'cstest' + str(time.time())[:-6:-1] + '@zdhUI.com'
    #     self.register(user_name)
    #     print('测试环境注册测试通过')

    # def test_login_formal(self):
    #     '''正式环境登录'''
    #     self.login('zstest001@qq.com')
    #     print('正式环境登录测试通过')

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

    # def test_char_test(self):
    #     '''群聊-创建群聊、聊天中发布各种类型的消息、群聊设置'''
    #
    #     get_xpath_list = self.getXpath_data_list("char")#获得xpath
    #     #切换正式环境和测试环境
    #     self.choice_environmental()#不填参数进入测试环境，填写任意参数进入正式环境
    #     #进入群聊界面和创建群聊只能选一个
    #     #self.join_group_char(get_xpath_list)#进入群聊界面
    #     self.create_group_chat(get_xpath_list)#创建群聊
    #     #self.function_text_test(get_xpath_list)  # 文字功能键
    #     #self.char_note(get_xpath_list)#聊天中发送各种类型信息
    #
    #     #self.quit_group_chat()#退出群聊
    #     self.group_chat_set(get_xpath_list)#聊天搜索、群聊设置。由于有会员功能，只能在测试环境测试
    #     #self.char_search_tab(get_xpath_list)#聊天列表搜索，此模块有问题，后期再改，包括加语音伙伴、扫二维码

    # def test_commont_one(self):
    #     '''动态-发布动态'''
    #     get_xpath_list = self.getXpath_data_list("common")  # 获得xpath
    #     #self.login('zstest001@qq.com')
    #     self.environmental_science()
    #     self.login('cstest001@qq.com')
    #     common_button = self.getXpath_data(get_xpath_list, "common_button")
    #     self.driver.find_element_by_xpath(common_button).click()
    #     try:
    #         self.driver.find_element_by_id("com.hellotalk:id/title").click()
    #         time.sleep(1)
    #         self.driver.back()
    #     except:
    #         pass

        # #发布动态
        # common_send_get_ready = self.getXpath_data(get_xpath_list, "common_send_get_ready")
        # for i in range(50):
        #     try:
        #         self.driver.find_element_by_xpath(common_send_get_ready).click()
        #     except:
        #         time.sleep(10)
        #         self.driver.find_element_by_xpath(common_send_get_ready).click()
        #
        #     self.driver.find_element_by_id("com.hellotalk:id/et_content").click()
        #     self.driver.find_element_by_id("com.hellotalk:id/et_content").send_keys("test ")
        #     self.driver.find_element_by_id("com.hellotalk:id/action_stream_publish").click()
        #     time.sleep(5)

        # #删除动态
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

    # def test_commont(self):
    #     '''动态-发布各种类型的动态'''
    #     get_xpath_list = self.getXpath_data_list("common")  # 获得xpath
    #     #self.login('zstest001@qq.com')
    #     self.environmental_science()
    #     self.login('cstest001@qq.com')
    #     common_button = self.getXpath_data(get_xpath_list, "common_button")
    #     self.driver.find_element_by_xpath(common_button).click()
    #     # common_tab = self.getXpath_data(get_xpath_list, "common_tab")
    #     # for i in range(1,5):
    #     #     self.driver.find_element_by_xpath(common_tab + str(i) + "]/android.widget.LinearLayout/android.widget.TextView").click()
    #     #     time.sleep(2)
    #     # for i in range(4,6):
    #     #     self.driver.find_element_by_xpath(common_tab + str(i) + "]/android.widget.LinearLayout/android.widget.TextView").click()
    #     #     self.driver.find_element_by_xpath(
    #     #         common_tab + str(i) + "]/android.widget.LinearLayout/android.widget.TextView").click()
    #     #     time.sleep(2)
    #     # print("动态页面-点击栏目（推荐、互助、关注、附近、学习、语音、同学）--测试通过")
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
    #     # common_conversation_one_next = self.getXpath_data(get_xpath_list, "common_conversation_one_next")
    #     # self.driver.find_element_by_xpath(common_conversation_one_next).click()
    #     #加入地址信息
    #     time.sleep(1)
    #     # self.driver.back()
    #     # self.driver.find_element_by_id("com.hellotalk:id/moment_location_view").click()
    #     # time.sleep(2)
    #     # common_send_get_ready_loc_next = self.getXpath_data(get_xpath_list, "common_send_get_ready_loc_next")
    #     # self.driver.find_element_by_xpath(common_send_get_ready_loc_next).click()
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

    @DecoratorF.operation_times(1)
    def test_me(self):
        '''我---编辑个人信息'''
        get_xpath_list = self.getXpath_data_list("me")  # 获得xpath
        #切换正式环境和测试环境
        try:
            self.choice_environmental()#不填参数进入测试环境，填写任意参数进入正式环境
        except:
            pass
        xpath_tab_me = self.getXpath_data(get_xpath_list, "xpath_tab_me")
        self.driver.find_element_by_xpath(xpath_tab_me).click()
        try:
            self.driver.find_element_by_id("android:id/button1").click()
        except:
            pass
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
        time.sleep(7)
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

    # def test_me(self):
    #     '''我---编辑个人信息'''
    #     get_xpath_list = self.getXpath_data_list("me")  # 获得xpath
    #     # 切换正式环境和测试环境
    #     try:
    #         self.choice_environmental()  # 不填参数进入测试环境，填写任意参数进入正式环境
    #     except:
    #         pass
    #     xpath_tab_me = self.getXpath_data(get_xpath_list, "xpath_tab_me")
    #     self.driver.find_element_by_xpath(xpath_tab_me).click()
    #     try:
    #         self.driver.find_element_by_id("android:id/button1").click()
    #     except:
    #         pass
    #
    #     #个人档案
    #     #个人档案-正在关注
    #     self.driver.find_element_by_id("com.hellotalk:id/following_label").click()
    #     # self.driver.find_element_by_id("com.hellotalk:id/editText").click()
    #     # self.driver.find_element_by_id("com.hellotalk:id/editText").send_keys("test")
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
        # # #vip会员页面
        # # self.driver.find_element_by_id("com.hellotalk:id/profile_store_layout").click()
        # # xpath_vip_one = self.getXpath_data(get_xpath_list, "xpath_vip_one")
        # # self.driver.find_element_by_xpath(xpath_vip_one).click()
        # # self.driver.find_element_by_id("com.hellotalk:id/close_btn").click()
        # # xpath_vip_two = self.getXpath_data(get_xpath_list, "xpath_vip_two")
        # # self.driver.find_element_by_xpath(xpath_vip_two).click()
        # # self.driver.find_element_by_id("com.hellotalk:id/close_btn").click()
        # # xpath_vip_three = self.getXpath_data(get_xpath_list, "xpath_vip_three")
        # # self.driver.find_element_by_xpath(xpath_vip_three).click()
        # # self.driver.find_element_by_id("com.hellotalk:id/close_btn").click()
        # # xpath_vip_four = self.getXpath_data(get_xpath_list, "xpath_vip_four")
        # # self.driver.find_element_by_xpath(xpath_vip_four).click()
        # # self.driver.find_element_by_id("com.hellotalk:id/close_btn").click()
        # # xpath_vip_five = self.getXpath_data(get_xpath_list, "xpath_vip_five")
        # # self.driver.find_element_by_xpath(xpath_vip_five).click()
        # # self.driver.find_element_by_id("com.hellotalk:id/close_btn").click()
        # # time.sleep(1)
        # # self.driver.back()
        # # print("个人档案-vip会员测试通过")
        # #动态
        # self.driver.find_element_by_id("com.hellotalk:id/moment_block_title").click()
        # self.driver.find_element_by_id("com.hellotalk:id/action_stream_publish").click()
        # self.driver.find_element_by_id("com.hellotalk:id/et_content").click()
        # self.driver.find_element_by_id("com.hellotalk:id/et_content").send_keys("test")
        # self.driver.find_element_by_id("com.hellotalk:id/et_content").click()
        # self.driver.find_element_by_id("com.hellotalk:id/action_stream_publish").click()
        # time.sleep(5)
        # xpath_feed_one = self.getXpath_data(get_xpath_list, "xpath_feed_one")
        # try:
        #     self.driver.find_element_by_xpath(xpath_feed_one).click()
        # except:
        #     time.sleep(20)
        #     self.driver.find_element_by_xpath(xpath_feed_one).click()
        # xpath_feed_two = self.getXpath_data(get_xpath_list, "xpath_feed_two")
        # self.driver.find_element_by_xpath(xpath_feed_two).click()
        # xpath_feed_three = self.getXpath_data(get_xpath_list, "xpath_feed_three")
        # self.driver.find_element_by_xpath(xpath_feed_three).click()
        # xpath_feed_four = self.getXpath_data(get_xpath_list, "xpath_feed_four")
        # self.driver.find_element_by_xpath(xpath_feed_four).click()
        # self.driver.find_element_by_id("com.hellotalk:id/share_cancel").click()
        # xpath_feed_five = self.getXpath_data(get_xpath_list, "xpath_feed_five")
        # self.driver.find_element_by_xpath(xpath_feed_five).click()
        # xpath_feed_six = self.getXpath_data(get_xpath_list, "xpath_feed_six")
        # self.driver.find_element_by_xpath(xpath_feed_six).click()
        # self.driver.find_element_by_id("android:id/button2").click()
        # xpath_feed_seven = self.getXpath_data(get_xpath_list, "xpath_feed_seven")
        # self.driver.find_element_by_xpath(xpath_feed_seven).click()
        # xpath_feed_eight = self.getXpath_data(get_xpath_list, "xpath_feed_eight")
        # self.driver.find_element_by_xpath(xpath_feed_eight).click()
        # self.driver.find_element_by_id("android:id/button1").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # print("个人档案-动态测试通过")
        # #收藏
        # self.driver.find_element_by_id("com.hellotalk:id/profile_favorites_layout").click()
        # self.driver.find_element_by_id("com.hellotalk:id/action_settings").click()
        # self.driver.find_element_by_id("com.hellotalk:id/edit_text").click()
        # self.driver.find_element_by_id("com.hellotalk:id/edit_text").send_keys("test")
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # self.driver.find_element_by_id("com.hellotalk:id/action_settings").click()
        # self.driver.find_element_by_id("com.hellotalk:id/text_type").click()
        # self.driver.find_element_by_id("com.hellotalk:id/search_edit_clear").click()
        # self.driver.find_element_by_id("com.hellotalk:id/moment_type").click()
        # self.driver.find_element_by_id("com.hellotalk:id/search_edit_clear").click()
        # self.driver.find_element_by_id("com.hellotalk:id/abc_type").click()
        # self.driver.find_element_by_id("com.hellotalk:id/search_edit_clear").click()
        # self.driver.find_element_by_id("com.hellotalk:id/voice_type").click()
        # self.driver.find_element_by_id("com.hellotalk:id/search_edit_clear").click()
        # time.sleep(1)
        # self.driver.back()
        # time.sleep(1)
        # self.driver.back()
        # print("个人档案-收藏测试通过")
        # #记事本
        # time.sleep(1)
        # SlidingScreen.swipe_up(self.driver)
        # self.driver.find_element_by_id("com.hellotalk:id/profile_notepad_layout").click()
        # #记事本-搜索
        # self.driver.find_element_by_accessibility_id("搜索").click()
        # self.driver.find_element_by_id("com.hellotalk:id/edit_text").click()
        # self.driver.find_element_by_id("com.hellotalk:id/edit_text").send_keys("test")
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # self.driver.find_element_by_accessibility_id("搜索").click()
        # self.driver.find_element_by_id("com.hellotalk:id/search_chatfiles_icon").click()
        # self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        # xpath_note_one = self.getXpath_data(get_xpath_list, "xpath_note_one")
        # self.driver.find_element_by_xpath(xpath_note_one).click()
        # self.driver.find_element_by_id("com.hellotalk:id/album_btn_send").click()
        # xpath_note_two = self.getXpath_data(get_xpath_list, "xpath_note_two")
        # self.driver.find_element_by_xpath(xpath_note_two).click()
        # self.driver.find_element_by_id("android:id/button1").click()
        #
        # self.driver.find_element_by_accessibility_id("搜索").click()
        # self.driver.find_element_by_id("com.hellotalk:id/search_chatfiles_icon").click()
        # self.driver.find_element_by_id("com.hellotalk:id/action_ok").click()
        # xpath_note_one = self.getXpath_data(get_xpath_list, "xpath_note_one")
        # self.driver.find_element_by_xpath(xpath_note_one).click()
        # self.driver.find_element_by_id("com.hellotalk:id/album_btn_download").click()
        # self.driver.find_element_by_id("com.hellotalk:id/album_btn_delete").click()
        # self.driver.find_element_by_id("android:id/button1").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # self.driver.find_element_by_id("com.hellotalk:id/search_date_icon").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # self.driver.find_element_by_id("com.hellotalk:id/voice_type").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # self.driver.find_element_by_id("com.hellotalk:id/abc_type").click()
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # self.driver.find_element_by_id("com.hellotalk:id/translation_type").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # self.driver.find_element_by_id("com.hellotalk:id/transliteration_type").click()
        # self.driver.find_element_by_id("com.hellotalk:id/search_edit_clear").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # #记事本 - 聊天設置
        # self.driver.find_element_by_accessibility_id("聊天設置").click()
        # xpath_note_three = self.getXpath_data(get_xpath_list, "xpath_note_three")
        # self.driver.find_element_by_xpath(xpath_note_three).click()
        # self.driver.find_element_by_id("com.hellotalk:id/view_history").click()
        # xpath_note_four = self.getXpath_data(get_xpath_list, "xpath_note_four")
        # self.driver.find_element_by_xpath(xpath_note_four).click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # xpath_note_five = self.getXpath_data(get_xpath_list, "xpath_note_five")
        # self.driver.find_element_by_xpath(xpath_note_five).click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # xpath_note_six = self.getXpath_data(get_xpath_list, "xpath_note_six")
        # self.driver.find_element_by_xpath(xpath_note_six).click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # self.driver.find_element_by_id("com.hellotalk:id/language_options").click()
        # self.driver.find_element_by_id("com.hellotalk:id/rec_to_layout").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # self.driver.find_element_by_id("com.hellotalk:id/sent_to_layout").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        #
        # #聊天中发送消息
        #
        # get_xpath_list = self.getXpath_data_list("char")
        # '''聊天中发送文字、表情、图片、相机-拍照、相机-录像、群组通话、涂鸦、介绍好友、贺卡、上课，语音（通话存在bug，暂时去掉）'''
        # self.driver.find_element_by_id("com.hellotalk:id/msg_input_text").send_keys('自动化测试')
        # self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        # print("群聊--聊天发送文字测试通过")
        #
        # self.driver.find_element_by_id("com.hellotalk:id/btn_emoji").click()
        # btn_emoji = self.getXpath_data(get_xpath_list, "btn_emoji")
        # for i in range(1, 15):
        #     self.driver.find_element_by_xpath(
        #         btn_emoji + str(i) + "]/android.widget.FrameLayout/android.widget.TextView").click()
        # self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        # print("群聊--聊天发送表情测试通过")
        # # 发送图片等
        # self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        # btn_add_one = self.getXpath_data(get_xpath_list, "btn_add_one")
        # self.driver.find_element_by_xpath(btn_add_one).click()
        # self.driver.find_element_by_id("android:id/button1").click()
        # for i in range(1, 7):
        #     btn_add_one_next = self.getXpath_data(get_xpath_list, "btn_add_one_next")
        #     self.driver.find_element_by_xpath(
        #         btn_add_one_next + str(i) + ']/android.widget.FrameLayout/android.widget.ImageView').click()
        #     try:
        #         self.driver.find_element_by_id("android:id/button1").click()
        #         break
        #     except:
        #         pass
        #
        # self.driver.find_element_by_id("com.hellotalk:id/send").click()
        # print("聊天发送-图片测试通过")
        # # 发送-相机
        # btn_add_two = self.getXpath_data(get_xpath_list, "btn_add_two")
        # try:
        #     self.driver.find_element_by_xpath(btn_add_two).click()
        # except:
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        #     self.driver.find_element_by_xpath(btn_add_two).click()
        # btn_add_two_next_one = self.getXpath_data(get_xpath_list, "btn_add_two_next_one")
        # self.driver.find_element_by_xpath(btn_add_two_next_one).click()
        # try:
        #     self.driver.find_element_by_id("android:id/button1").click()
        # except:
        #     pass
        #
        # self.driver.press_keycode(27)
        # self.driver.find_element_by_id("com.huawei.camera:id/done_button").click()
        # self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
        # print("聊天中发送-相机-拍照测试通过")
        # btn_add_two = self.getXpath_data(get_xpath_list, "btn_add_two")
        # self.driver.find_element_by_xpath(btn_add_two).click()
        # btn_add_two_next_two = self.getXpath_data(get_xpath_list, "btn_add_two_next_two")
        # self.driver.find_element_by_xpath(btn_add_two_next_two).click()
        # self.driver.find_element_by_id("com.hellotalk:id/take_camera").click()
        # time.sleep(8)
        # self.driver.find_element_by_id("com.hellotalk:id/take_camera").click()
        # self.driver.find_element_by_id("com.hellotalk:id/sure").click()
        # print("聊天中发送-相机-录像测试通过")
        #
        # btn_add_three = self.getXpath_data(get_xpath_list, "btn_add_three")
        # self.driver.find_element_by_xpath(btn_add_three).click()
        #
        # SlidingScreen.swipe_right(self.driver)
        # SlidingScreen.swipe_left(self.driver)
        #
        # self.driver.find_element_by_id("com.hellotalk:id/pensize").click()
        #
        # self.driver.find_element_by_id("com.hellotalk:id/eraser").click()
        # self.driver.find_element_by_id("com.hellotalk:id/pencolorcircle").click()
        # self.driver.find_element_by_id("com.hellotalk:id/undo").click()
        # self.driver.find_element_by_id("com.hellotalk:id/redo").click()
        # self.driver.find_element_by_id("com.hellotalk:id/del").click()
        # btn_add_four_next_two = self.getXpath_data(get_xpath_list, "btn_add_four_next_two")
        # self.driver.find_element_by_xpath(btn_add_four_next_two).click()
        # self.driver.find_element_by_id("com.hellotalk:id/del").click()
        #
        # btn_add_four_next_one = self.getXpath_data(get_xpath_list, "btn_add_four_next_one")
        # self.driver.find_element_by_xpath(btn_add_four_next_one).click()
        # self.driver.find_element_by_id("com.hellotalk:id/pensize").click()
        # SlidingScreen.swipe_right(self.driver)
        # SlidingScreen.swipe_left(self.driver)
        # self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
        # time.sleep(2)
        # self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        # try:
        #     btn_add_three = self.getXpath_data(get_xpath_list, "btn_add_three")
        #     self.driver.find_element_by_xpath(btn_add_three).click()
        # except:
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        #     btn_add_three = self.getXpath_data(get_xpath_list, "btn_add_three")
        #     self.driver.find_element_by_xpath(btn_add_three).click()
        #
        # btn_add_four_next_table_two = self.getXpath_data(get_xpath_list, "btn_add_four_next_table_two")
        # self.driver.find_element_by_xpath(btn_add_four_next_table_two).click()
        #
        # btn_add_four_next_table_one = self.getXpath_data(get_xpath_list, "btn_add_four_next_table_one")
        # self.driver.find_element_by_xpath(btn_add_four_next_table_one).click()
        #
        # btn_add_four_next_table_two = self.getXpath_data(get_xpath_list, "btn_add_four_next_table_two")
        # self.driver.find_element_by_xpath(btn_add_four_next_table_two).click()
        #
        # self.driver.find_element_by_id("com.hellotalk:id/pensizetx").click()
        #
        # SlidingScreen.swipe_right(self.driver)
        # SlidingScreen.swipe_left(self.driver)
        # time.sleep(3)
        #
        # self.driver.find_element_by_id("com.hellotalk:id/pencolorcircletx").click()
        # self.driver.find_element_by_id("com.hellotalk:id/deltext").click()
        #
        # SlidingScreen.swipe_right(self.driver)
        # SlidingScreen.swipe_left(self.driver)
        # time.sleep(3)
        #
        # self.driver.find_element_by_id("com.hellotalk:id/entertext").click()
        # self.driver.find_element_by_id("com.hellotalk:id/deltx").click()
        # btn_add_four_next_two = self.getXpath_data(get_xpath_list, "btn_add_four_next_two")
        # self.driver.find_element_by_xpath(btn_add_four_next_two).click()
        # self.driver.find_element_by_id("com.hellotalk:id/deltx").click()
        # btn_add_four_next_one = self.getXpath_data(get_xpath_list, "btn_add_four_next_one")
        # self.driver.find_element_by_xpath(btn_add_four_next_one).click()
        #
        # SlidingScreen.swipe_right(self.driver)
        # SlidingScreen.swipe_left(self.driver)
        # time.sleep(3)
        #
        # self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
        # print("聊天中发送-涂鸦测试通过")
        #
        # btn_add_four = self.getXpath_data(get_xpath_list, "btn_add_four")
        # self.driver.find_element_by_xpath(btn_add_four).click()
        # self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='互相關注']").click()
        #
        # btn_add_five_next = self.getXpath_data(get_xpath_list, "btn_add_five_next")
        # self.driver.find_element_by_xpath(btn_add_five_next).click()
        # self.driver.find_element_by_id("android:id/button2").click()
        # self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        # btn_add_four = self.getXpath_data(get_xpath_list, "btn_add_four")
        # self.driver.find_element_by_xpath(btn_add_four).click()
        # self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='互相關注']").click()
        # btn_add_five_next = self.getXpath_data(get_xpath_list, "btn_add_five_next")
        # self.driver.find_element_by_xpath(btn_add_five_next).click()
        # self.driver.find_element_by_id("android:id/button1").click()
        # print("聊天中发送-介绍好友测试通过")
        # btn_add_five = self.getXpath_data(get_xpath_list, "btn_add_five")
        # try:
        #     self.driver.find_element_by_xpath(btn_add_five).click()
        # except:
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_add").click()
        #     self.driver.find_element_by_xpath(btn_add_five).click()
        # time.sleep(8)
        # self.driver.find_element_by_id("com.hellotalk:id/action_send").click()
        # print("聊天中发送-发送位置测试通过")
        #
        #
        # self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        #
        # self.driver.find_element_by_id("com.hellotalk:id/record_listen_btn").click()
        # time.sleep(6)
        # self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
        # self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        # time.sleep(6)
        # self.driver.find_element_by_id("com.hellotalk:id/record_listen_btn").click()
        # time.sleep(6)
        # self.driver.find_element_by_id("com.hellotalk:id/record_listen_send_btn").click()
        # self.driver.find_element_by_id("com.hellotalk:id/chat_btn_voice").click()
        # time.sleep(6)
        # self.driver.find_element_by_id("com.hellotalk:id/record_cancel_btn").click()
        # print("聊天中发送-发送语音测试通过")
        # #翻译
        # self.driver.find_element_by_id("com.hellotalk:id/btn_translate").click()
        # btn_group_char_one = self.getXpath_data(get_xpath_list, "btn_group_char_one")
        # self.driver.find_element_by_xpath(btn_group_char_one).click()
        # self.driver.find_element_by_id("com.hellotalk:id/source_text_input").click()
        # self.driver.find_element_by_id("com.hellotalk:id/source_text_input").send_keys("you are the best")
        # self.driver.press_keycode(66)
        # time.sleep(3)
        # try:
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_speak_source").click()
        #     time.sleep(1)
        #     self.driver.back()
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_star_source").click()
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_copy_source").click()
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_send_source").click()
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_translate").click()
        #
        #     btn_group_char_one = self.getXpath_data(get_xpath_list, "btn_group_char_one")
        #     self.driver.find_element_by_xpath(btn_group_char_one).click()
        #
        #     self.driver.find_element_by_id("com.hellotalk:id/source_text_input").click()
        #     self.driver.find_element_by_id("com.hellotalk:id/source_text_input").send_keys("you are the best")
        #     self.driver.press_keycode(66)
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_transliteration").click()
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_speak_result").click()
        #     time.sleep(1)
        #     self.driver.back()
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_star_result").click()
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_copy_result").click()
        #     self.driver.find_element_by_id("com.hellotalk:id/btn_send_result").click()
        # except:
        #     self.driver.find_element_by_id("com.hellotalk:id/action_favorites").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # print('聊天中发送-翻译功能测试通过')
        #
        # self.driver.find_element_by_id("com.hellotalk:id/profile_nav_translate").click()
        # self.driver.find_element_by_id("com.hellotalk:id/source_text_input").click()
        # self.driver.find_element_by_id("com.hellotalk:id/source_text_input").send_keys("you are the best")
        # self.driver.press_keycode(66)
        # time.sleep(8)
        # self.driver.find_element_by_id("com.hellotalk:id/btn_transliteration").click()
        # time.sleep(1)
        # self.driver.find_element_by_id("com.hellotalk:id/btn_speak_result").click()
        # time.sleep(1)
        # self.driver.back()
        # self.driver.find_element_by_id("com.hellotalk:id/btn_star_result").click()
        # time.sleep(1)
        # self.driver.find_element_by_id("com.hellotalk:id/btn_copy_result").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        #
        # print('个人档案-翻译助手测试通过')
        # #设置
        # #设置-账户
        # self.driver.find_element_by_id("com.hellotalk:id/profile_nav_settings").click()
        # time.sleep(1)
        # xpath_setting_one = self.getXpath_data(get_xpath_list, "xpath_setting_one")
        # self.driver.find_element_by_xpath(xpath_setting_one).click()
        # xpath_setting_two = self.getXpath_data(get_xpath_list, "xpath_setting_two")
        # self.driver.find_element_by_xpath(xpath_setting_two).click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # xpath_setting_three = self.getXpath_data(get_xpath_list, "xpath_setting_three")
        # self.driver.find_element_by_xpath(xpath_setting_three).click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # xpath_setting_four = self.getXpath_data(get_xpath_list, "xpath_setting_four")
        # self.driver.find_element_by_xpath(xpath_setting_four).click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # # 设置-新消息通知
        # xpath_setting_five = self.getXpath_data(get_xpath_list, "xpath_setting_five")
        # self.driver.find_element_by_xpath(xpath_setting_five).click()
        # self.driver.find_element_by_id("com.hellotalk:id/moments_comments_cb").click()
        # self.driver.find_element_by_id("com.hellotalk:id/follow_cb").click()
        # self.driver.find_element_by_id("com.hellotalk:id/moments_comments_cb").click()
        # self.driver.find_element_by_id("com.hellotalk:id/follow_cb").click()
        # self.driver.find_element_by_id("com.hellotalk:id/new_message_alerts").click()
        # self.driver.find_element_by_id("android:id/button1").click()
        # self.driver.find_element_by_id("com.hellotalk:id/new_message_alerts").click()
        # self.driver.find_element_by_id("com.hellotalk:id/disturb_layout").click()
        # self.driver.find_element_by_id("com.hellotalk:id/on").click()
        # time.sleep(1)
        # self.driver.find_element_by_id("com.hellotalk:id/on").click()
        # time.sleep(1)
        # self.driver.find_element_by_id("com.hellotalk:id/on").click()
        # time.sleep(1)
        # self.driver.find_element_by_id("com.hellotalk:id/on").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # self.driver.find_element_by_id("com.hellotalk:id/message_preview").click()
        # time.sleep(1)
        # self.driver.find_element_by_id("com.hellotalk:id/message_preview").click()
        # self.driver.find_element_by_id("com.hellotalk:id/notification_sys_settings").click()
        # xpath_setting_six = self.getXpath_data(get_xpath_list, "xpath_setting_six")
        # self.driver.find_element_by_xpath(xpath_setting_six).click()
        # self.driver.find_element_by_id("android:id/switch_widget").click()
        # xpath_setting_more_one = self.getXpath_data(get_xpath_list, "xpath_setting_more_one")
        # self.driver.find_element_by_xpath(xpath_setting_more_one).click()
        # xpath_setting_more_two = self.getXpath_data(get_xpath_list, "xpath_setting_more_two")
        # self.driver.find_element_by_xpath(xpath_setting_more_two).click()
        # xpath_setting_more_three = self.getXpath_data(get_xpath_list, "xpath_setting_more_three")
        # self.driver.find_element_by_xpath(xpath_setting_more_three).click()
        # xpath_setting_more_four = self.getXpath_data(get_xpath_list, "xpath_setting_more_four")
        # self.driver.find_element_by_xpath(xpath_setting_more_four).click()
        # xpath_setting_more_five = self.getXpath_data(get_xpath_list, "xpath_setting_more_five")
        # self.driver.find_element_by_xpath(xpath_setting_more_five).click()
        # self.driver.find_element_by_xpath(xpath_setting_more_one).click()
        # self.driver.find_element_by_xpath(xpath_setting_more_two).click()
        # self.driver.find_element_by_xpath(xpath_setting_more_three).click()
        # self.driver.find_element_by_xpath(xpath_setting_more_four).click()
        # self.driver.find_element_by_xpath(xpath_setting_more_five).click()
        #
        # xpath_setting_more_six = self.getXpath_data(get_xpath_list, "xpath_setting_more_six")
        # xpath_setting_more_seven = self.getXpath_data(get_xpath_list, "xpath_setting_more_seven")
        #
        # for i in range(3,0,-1):
        #     self.driver.find_element_by_xpath(xpath_setting_more_six).click()
        #     self.driver.find_element_by_xpath(xpath_setting_more_seven + str(i)+"]/android.widget.LinearLayout/android.widget.RadioButton").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上导航").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # print('个人档案-设置测试通过')
        # #推荐
        # self.driver.find_element_by_id("com.hellotalk:id/recommend").click()
        # self.driver.find_element_by_id("com.hellotalk:id/item_icon").click()
        # time.sleep(3)
        # xpath_recommend = self.getXpath_data(get_xpath_list, "xpath_recommend")
        # self.driver.find_element_by_xpath(xpath_recommend).click()
        # time.sleep(1)
        # self.driver.find_element_by_accessibility_id("向上瀏覽").click()
        # print('个人档案-推荐测试通过')



# if __name__ == '__main__':
#     unittest.main()
