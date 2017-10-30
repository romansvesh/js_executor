# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver

from helper.helper import Helper
from page import main_page, search_result_page

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('lib\chromedriver.exe')
        self.driver.get("https://www.google.ru")
        self.driver.maximize_window()

    def test_login(self):
        help_ = Helper(self.driver)
        main = main_page.MainPage(self.driver)
        print(main.get_element_offset_width())

        self.assertFalse(help_.get_scrollbar_existance())

        main.enter_search_text("Selenium")
        main.disable_focus_from_search_field()
        main.submit_search_and_wait_load()

        self.assertTrue(help_.get_scrollbar_existance())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
