# -*- coding:utf-8 -*-
import time,os
from UI.Element import Element

class UploadFiles():


    def login(self):
        # 登录
        driver = Element()
        driver.element_by_xpath("//*[@id='app']/div/div/div/div[2]/div/form/div[1]/div/div/input", 'admin')
        driver.element_by_xpath("//*[@id='app']/div/div/div/div[2]/div/form/div[2]/div/div/input", "123456")
        driver.element_by_xpath("//*[@id='app']/div/div/div/div[2]/div/form/div[3]/div/button/span")



    def logout(self):
        time.sleep(1)
        driver = Element()
        driver.element_by_xpath("//*[@class='quickHint']/li/div")
        time.sleep(1)
        driver.element_by_xpath(
            "//*[@class='main ivu-layout ivu-layout-has-sider']/div[2]/div/div/div[4]/ul/li/div/div[2]/ul/li[2]")
        time.sleep(2)
        try:
            driver.element_by_xpath("//*[@class='v-transfer-dom'][6]/div[2]/div/div/div/div/div[3]/button[2]/span")
            driver.element_by_xpath("//*[@class='v-transfer-dom'][3]/div[2]/div/div/div/div/div[3]/button[2]/span")
        except:
            pass
        time.sleep(1)

    def video_upload(self):
        UploadFiles().login()
        driver = Element()


        #点击互动-影片管理
        driver.element_by_xpath("//*[@class='side-menu-wrapper']/ul/li[5]/div")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='side-menu-wrapper']/ul/li[5]/ul/li[5]")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='main ivu-layout ivu-layout-has-sider']/div[2]/div[2]/div/div[2]/button/span")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='v-transfer-dom']/div[2]/div/div/div[2]/form/div/div/div/input","zdhtest")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='v-transfer-dom']/div[2]/div/div/div[2]/form/div[2]/div/div/div/div/button/span")
        time.sleep(1)
        os.system(os.getcwd() + r"\UI\updataV.exe")
        time.sleep(2)
        driver.element_by_xpath("//*[@class='v-transfer-dom']/div[2]/div/div/div[3]/button/span")
        time.sleep(5)
        print("影片上传完成")
        UploadFiles().logout()

    def Anchor_head(self):
        # 互动-主播管理-编辑主播账号(新增主播头像)
        driver = Element()
        UploadFiles().login()
        driver.element_by_xpath("//*[@class='side-menu-wrapper']/ul/li[5]/div")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='side-menu-wrapper']/ul/li[5]/ul/li")
        time.sleep(1)
        driver.element_by_xpath(
            "//*[@class='main-content-wrap ivu-layout-content']/div/div[3]/div/div/div[2]/table/tbody/tr/td[12]/div/div/div/button[2]/span")
        time.sleep(1)
        driver.element_by_xpath(
            "//*[@class='v-transfer-dom'][3]/div/div/div/div[2]/form/div[4]/div/div/div/div/div/div/button/span")
        time.sleep(1)
        os.system(os.getcwd() + r"\UI\updataPic.exe")
        time.sleep(2)
        driver.element_by_xpath(
            "//*[@class='v-transfer-dom'][3]/div[2]/div/div/div[2]/form/div[4]/div/div/div/div/div[2]/button/span")
        time.sleep(5)
        driver.element_by_xpath("//*[@class='v-transfer-dom'][3]/div[2]/div/div/div[3]/div/button[2]/span")
        UploadFiles().logout()

    def anchor_film(self):
        # 创建影片主播
        driver = Element()
        UploadFiles().login()
        driver.element_by_xpath("//*[@class='side-menu-wrapper']/ul/li[5]/div")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='side-menu-wrapper']/ul/li[5]/ul/li[2]")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='main-content ivu-layout']/div[2]/div/div[2]/div/div/div[2]/button/span")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='modal v-transfer-dom']/div/div/div/div/div[2]/div/div/label")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='modal v-transfer-dom']/div/div/div/div[2]/div/button[2]/span")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='modal v-transfer-dom']/div/div/div/div/div[2]/div/div/label")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='modal v-transfer-dom']/div/div/div/div[2]/div/button[2]/span")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='modal v-transfer-dom']/div/div/div/div/div[2]/ul/li/div/div/div/span")
        time.sleep(1)
        os.system(os.getcwd() + r"\UI\updataPic.exe")
        time.sleep(8)
        driver.element_by_xpath("//*[@class='modal v-transfer-dom']/div/div/div/div/div[2]/ul/li/div")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='modal v-transfer-dom']/div/div/div/div[2]/div/button[2]/span")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='modal v-transfer-dom']/div/div/div/div/div[2]/div/div/label")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='modal v-transfer-dom']/div/div/div/div[2]/div/button[2]/span")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='modal v-transfer-dom']/div/div/div/div/div[2]/div/div/input", "zdhtest")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='modal v-transfer-dom']/div/div/div/div[2]/div/button[2]/span")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='modal v-transfer-dom']/div/div/div/div[2]/div/button[2]/span")
        UploadFiles().logout()




#
# if __name__ == '__main__':
#     VideoUpload().video_upload()