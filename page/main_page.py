# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self._driver = driver

    SEARCH_FIELD = (By.XPATH, '//*[@title= "Поиск"]/parent::div')

    def get_search_field(self):
        return self._driver.find_element(*self.SEARCH_FIELD)
