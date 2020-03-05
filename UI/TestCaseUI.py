# encoding: utf-8
"""
@version: ??
@author: terry
@time: 2020/1/11 15:18
"""

import time
from UI.Element import Element
import unittest

class AddAdvertising(unittest.TestCase):

    driver = Element()
    def test_01_index(self):
        '''衣图官网-首页'''
        self.driver.element_by_xpath("//nav/ul[@id='menu']/ul[@id='menu']/li[2]/a")

    def test_02_yitu(self):
        '''衣图官网-衣图'''
        self.driver.element_by_xpath("//nav/ul[@id='menu']/ul[@id='menu']/li[3]/a")
        time.sleep(3)

    def test_03_ai_trend(self):
        '''衣图官网-Ai趋势'''
        self.driver.element_by_xpath("//nav/ul/li[4]/a")
        time.sleep(3)

    def test_04_ai_mass_data(self):
        '''衣图官网-Ai大数据'''
        self.driver.element_by_xpath("//nav/ul/li[5]/a")
        time.sleep(3)

    def test_05_ai_designer(self):
        '''衣图官网-Ai设计师'''
        self.driver.element_by_xpath("//nav/ul/li[6]/a")
        time.sleep(3)

    def test_06_ai_Laboratory(self):
        '''衣图官网-Ai实验室'''
        self.driver.element_by_xpath("//nav/ul/li[7]/a")
        time.sleep(3)

    def test_07_about_us(self):
        '''衣图官网-Ai大数据'''
        self.driver.element_by_xpath("//nav/ul/li[1]/a")
        time.sleep(3)




if __name__ == '__main__':
    unittest.main()