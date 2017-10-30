# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from helper.helper import Helper
from page.search_result_page import SearchResultPage


class MainPage:
    def __init__(self, driver):
        self._driver = driver

    SEARCH_FIELD = (By.XPATH, '//*[@title= "Поиск"]/parent::div')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[type=text]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@jsaction="sf.chk"]')

    def get_element_offset_width(self):
        help_ = Helper(self._driver)
        help_.wait_for_element(5, MainPage.SEARCH_FIELD)
        arg = self._driver.find_element(*self.SEARCH_FIELD)
        return self._driver.execute_script('return arguments[0].offsetWidth',
                                           arg)

    def enter_search_text(self, text):
        help_ = Helper(self._driver)
        help_.wait_for_element(5, self.SEARCH_FIELD)
        element = self._driver.find_element(*self.SEARCH_INPUT)
        element.send_keys(text)

    def disable_focus_from_search_field(self):
        help_ = Helper(self._driver)
        help_.wait_for_element(5, self.SEARCH_INPUT)
        element = self._driver.find_element(*self.SEARCH_INPUT)
        self._driver.execute_script('arguments[0].blur();', element)

    def submit_search_and_wait_load(self):
        search_result_page = SearchResultPage()
        help_ = Helper(self._driver)
        help_.wait_for_element(5, self.SUBMIT_BUTTON)
        self._driver.find_element(*self.SUBMIT_BUTTON).click()
        help_.wait_for_element(5, search_result_page.OPTIONS_MENU)
