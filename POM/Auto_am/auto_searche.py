import random

from selenium.webdriver.common.by import By
from BASE.auto_am_base_page import Base_Page_Auto


class Autosearch(Base_Page_Auto):
    search_result = {'by': By.ID, 'value': 'search-result'}
    search_results = {'by': By.XPATH, 'value': "//span[contains(@class, 'card-title bold')]"}
    complist = {'by': By.XPATH, 'value': "//section[@id='sec-search']//a[3]"}
    grid = {'by': By.XPATH, 'value': "//div[@id='search-tools']//a[1]"}
    signin = {'by': By.XPATH, 'value': "//ul[contains(@class,'grey-text footer-menu-proj')]//a[contains(text(),"
                                       "'Sign In')]"}

    def matching_search_results(self):
        a = random.randrange(23, 73)
        b = self._find_elements(self.search_results)
        return b[a].text

    def search_res_view_attribute(self):
        return self._get_attribute(self.search_result, 'class')

    def click_on_complist(self):
        self._click(self.complist)

    def click_on_grid(self):
        self._click(self.grid)

    def click_on_signin(self):
        self._click(self.signin)
