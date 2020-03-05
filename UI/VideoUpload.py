# -*- coding:utf-8 -*-
import time,os
from UI.Element import Element

class VideoUpload():

    el = Element()

    def video_upload(self):
        '''网站-互动-影片管理'''
        driver = VideoUpload().el
        #登录
        driver.element_by_xpath("//*[@id='app']/div/div/div/div[2]/div/form/div[1]/div/div/input",'admin')
        driver.element_by_xpath("//*[@id='app']/div/div/div/div[2]/div/form/div[2]/div/div/input","123456")
        driver.element_by_xpath("//*[@id='app']/div/div/div/div[2]/div/form/div[3]/div/button/span")
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
        os.system(os.getcwd() + r"\updataV.exe")
        time.sleep(2)
        driver.element_by_xpath("//*[@class='v-transfer-dom']/div[2]/div/div/div[3]/button/span")
        time.sleep(5)
        driver.element_by_xpath("//*[@class='quickHint']/li/div")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='main ivu-layout ivu-layout-has-sider']/div[2]/div/div/div[4]/ul/li/div/div[2]/ul/li[2]")
        time.sleep(1)
        driver.element_by_xpath("//*[@style='overflow: hidden;']/div[5]//div/div/div/div/div/div[3]/button[2]/span")
        time.sleep(1)
        print("影片上传完成")

        time.sleep(1)
        driver.element_by_xpath("//*[@class='quickHint']/li/div")
        time.sleep(1)
        driver.element_by_xpath(
            "//*[@class='main ivu-layout ivu-layout-has-sider']/div[2]/div/div/div[4]/ul/li/div/div[2]/ul/li[2]")
        time.sleep(1)
        driver.element_by_xpath("//*[@class='v-transfer-dom'][4]/div[2]/div/div/div/div/div[3]/button[2]/span")
        time.sleep(1)



if __name__ == '__main__':
    VideoUpload().video_upload()