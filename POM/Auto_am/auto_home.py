from selenium.webdriver.common.by import By
from BASE.auto_am_base_page import Base_Page_Auto


class Autohome(Base_Page_Auto):
    language_icon = {'by': By.CLASS_NAME, 'value': 'material-icons'}
    make = {'by': By.ID, 'value': 'select2-filter-make-container'}
    english = {'by': By.XPATH, 'value': '/html[1]/body[1]/header[1]/div[2]/div[2]/ul[1]/li[1]/div[1]'}
    make_input = {'by': By.CLASS_NAME, 'value': 'select2-search__field'}
    search_res = {'by': By.CLASS_NAME, 'value': 'select2-results__option'}
    model = {'by': By.ID, 'value': 'select2-v-model-container'}
    model_names = {'by': By.CLASS_NAME, 'value': 'select2-results__option'}
    search_btn = {'by': By.ID, 'value': 'search-btn'}

    def click_on_make(self):
        self._click(self.make)

    def open_language_bar(self):
        list1 = self._find_elements(self.language_icon)
        for i in list1:
            if i.text == 'language':
                return i.click()

    def click_on_english(self):
        self._click(self.english)

    def find_make_text(self):
        return self._find_text(self.make)

    def input_car_name(self):
        self._type(self.make_input, 'N')

    def make_suggestion_list_text(self):
        list1 = self._find_elements(self.search_res)
        return list1[1].text

    def click_from_suggested(self):
        list1 = self._find_elements(self.search_res)
        list1[1].click()

    def find_attribute_of_make_field(self):
        return self._get_attribute(self.make, 'title')

    def model_text(self):
        return self._find_text(self.model)

    def model_click(self):
        self._click(self.model)

    def click_on_car_model(self):
        list1 = self._find_elements(self.model_names)
        for i in list1:
            if i.text == 'X-Trail':
                return i.click()

    def search_btn_click(self):
        self._click(self.search_btn)
