# -*- coding:utf-8 -*-
#from selenium import webdriver
import time,os
from UI.Element import Element
import unittest

class AddAdvertising(unittest.TestCase):


    driver = Element()



    def index(self):
        '''衣图官网-首页'''
        self.driver.element_by_xpath("//nav/ul[@id='menu']/ul[@id='menu']/li[2]/a")

    def yitu(self):
        '''衣图官网-衣图'''
        self.driver.element_by_xpath("//nav/ul[@id='menu']/ul[@id='menu']/li[3]/a")

    # def ai_qushi(self):
    #     '''衣图官网-Ai趋势'''
    #     driver = AddAdvertising().el
    #     driver.element_by_xpath("//nav/ul[@id='menu']/ul[@id='menu']/li[4]/a")




if __name__ == '__main__':
    AddAdvertising().index()
    AddAdvertising().yitu()







