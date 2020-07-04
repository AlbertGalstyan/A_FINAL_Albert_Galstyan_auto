from selenium.webdriver.common.by import By
from BASE.auto_am_base_page import Base_Page_Auto


class Autoauthorized(Base_Page_Auto):
    profile_image = {'by': By.XPATH, 'value': "//div[@class='profile-img']"}
    cell = {'by': By.XPATH, 'value': "//a[@class='waves-effect waves-light btn blue sellbtn']"}



    def profile_pic_diplayed(self):
        return self._is_displayed(self.profile_image, 0)

    def click_on_cell(self):
        self._click(self.cell)
