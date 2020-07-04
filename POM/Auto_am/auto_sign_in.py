from selenium.webdriver.common.by import By
from BASE.auto_am_base_page import Base_Page_Auto


class Autosignin(Base_Page_Auto):
    username = {'by': By.XPATH, 'value': "//input[@placeholder='Email address']"}
    password = {'by': By.XPATH, 'value': "//input[@id='password']"}
    login_btn = {'by': By.XPATH, 'value': "//button[@name='login']"}



    def input_username(self):
        self._type(self.username, 'elibsika@gmail.com')

    def input_password(self):
        self._type(self.password, 'albert1989')

    def login(self):
        self._click(self.login_btn)
