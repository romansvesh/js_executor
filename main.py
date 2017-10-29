# -*- coding: utf-8 -*-

import unittest

import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from helper.helper import Helper


class TestLogin(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Chrome('lib\chromedriver.exe', chrome_options=options)
        self.driver.get("http://www.google.ru")
        self.driver.maximize_window()

    def test_login(self):
        help_ = Helper(self.driver)
        print(help_.get_element_offset_width())

    def tearDown(self):
        time.sleep(30)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()