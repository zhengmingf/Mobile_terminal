# -*- coding:utf-8 -*-
from selenium import webdriver

class Element():
    driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
    driver.implicitly_wait(10)
    driver.get("http://www.rss100.com/index.html")
    def element_by_xpath(self,xpath,char=None):
        if char == None:
            Element().driver.find_element_by_xpath(xpath).click()
        else:
            Element().driver.find_element_by_xpath(xpath).send_keys(char)


