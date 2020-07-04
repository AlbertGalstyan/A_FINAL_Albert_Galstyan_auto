from POM.Auto_am.auto_authorized_home import Autoauthorized
from POM.Auto_am.auto_cell import Autocell
from POM.Auto_am.auto_home import Autohome
from POM.Auto_am.auto_searche import Autosearch
import time
from POM.Auto_am.auto_sign_in import Autosignin

                                        #THIS TEST CONTAINS
                                        #5 POM
                                        #BASE PAGE
                                        #CONFTEST FILE (ABILITY TO RUN TEST ON CHROME,FF, ON VIA DOCKER.)
                                        #DOCKER-COMPOSE FILE
                                        #CONFIG.JSON FILE 
class TestAuto():
    """" visit URL(assertion), Chnage Language(assertion),
    input 2 fields for search(assertion),
     check for suggestions, search."""
    def test_auto(self, driver):
        homepage = Autohome(driver)
        homepage.open_language_bar()
        homepage.click_on_english()
        assert driver.title == 'Car sale in Armenia - Auto.am'
        time.sleep(0.5)
        assert homepage.find_make_text() == 'select'
        homepage.click_on_make()
        homepage.input_car_name()
        assert homepage.make_suggestion_list_text() == 'Nissan'
        homepage.click_from_suggested()
        assert homepage.find_attribute_of_make_field() == 'Nissan'
        time.sleep(1)
        assert homepage.model_text() == 'Select'
        homepage.model_click()
        homepage.click_on_car_model()
        homepage.search_btn_click()
        """compare search results with search words(assertion), change view options(assertion), signin"""
        searchpage = Autosearch(driver)
        assert driver.title == 'Search - Auto.am'
        assert "Nissan X-Trail" in searchpage.matching_search_results()
        assert searchpage.search_res_view_attribute() == 'list'
        searchpage.click_on_complist()
        time.sleep(0.5)
        assert searchpage.search_res_view_attribute() == 'complist'
        searchpage.click_on_grid()
        time.sleep(0.5)
        assert searchpage.search_res_view_attribute() == 'grid'
        searchpage.click_on_signin()
        """checking page is open, input user and pass, signin"""
        signinpage = Autosignin(driver)
        time.sleep(0.5)
        assert driver.title == 'Sign In - Auto.am'
        signinpage.input_username()
        signinpage.input_password()
        time.sleep(0.5)
        signinpage.login()
        time.sleep(0.5)
        """asserting we are authorized, click on cell car button"""
        authorized = Autoauthorized(driver)
        assert authorized.profile_pic_diplayed()
        authorized.click_on_cell()
        """chech we are on cell page, choose several fields(assertion),
         click on save(asserting that there are requried fields that are not filled)"""
        autocell = Autocell(driver)
        time.sleep(0.5)
        assert driver.title == 'Sell - Auto.am'
        assert autocell.categroty_attribute() == 'Passenger'
        autocell.click_category()
        autocell.select_bus_from_list()
        assert autocell.categroty_attribute() == 'Bus'
        autocell.set_price()
        autocell.save_btn_click()
        assert autocell.error_message_count() == 'This is a required field'
        """logout(assertion)"""
        autocell.click_my_account()
        autocell.sign_out_click()
        assert autocell.profile_picture_not_displayed() == True
