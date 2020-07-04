from selenium.webdriver.common.by import By
from BASE.auto_am_base_page import Base_Page_Auto


class Autocell(Base_Page_Auto):
    category = {'by': By.ID, 'value': "select2-ad-category-container"}
    category_list = {'by': By.CLASS_NAME, 'value': "select2-results__option"}
    price = {'by': By.XPATH, 'value': "//input[@placeholder='0']"}
    my_account = {'by': By.XPATH, 'value': "//span[@class='truncate']"}
    signout = {'by': By.XPATH, 'value': "//a[@class='bold'][contains(text(),'Sign Out')]"}
    profile_image = {'by': By.XPATH, 'value': "//div[@class='profile-img']"}


    def profile_picture_not_displayed(self):
        if self._is_displayed(self.profile_image, 1):
            return False
        else:
            return True

    def categroty_attribute(self):
        return self._get_attribute(self.category, 'title')

    def click_category(self):
        self._click(self.category)

    def select_bus_from_list(self):
        list1 = self._find_elements(self.category_list)
        for i in list1:
            if i.text == 'Bus':
                return i.click()

    def set_price(self):
        self._type(self.price, '5000')

    def click_my_account(self):
        self._click(self.my_account)

    def sign_out_click(self):
        self._click(self.signout)
