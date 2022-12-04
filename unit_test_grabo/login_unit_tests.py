from imported_library.used_librabies import unittest, By
import HtmlTestRunner
from variables.config_data import base_data
from pages.initialize_driver import initialized_driver
from pages.login import login_page


class LoginPage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = initialized_driver.get_driver()

    def test_login_valid_data(self):
        login_page.open_login_form()
        login_page.enter_email_data("valid@abv.bg")
        login_page.enter_password_data("Validpassword2022")
        login_page.click_login_button()
        # check if element appear
        self.assertTrue(
            login_page.verify_opened_successfully_and_component_present(base_data["component_on_home_page"]))

    def test_login_missing_password(self):
        login_page.open_login_form()
        login_page.enter_email_data("valid@abv.bg")
        login_page.click_login_button()
        self.assertFalse(
            login_page.verify_opened_successfully_and_component_present(base_data["component_on_home_page"]))

    def test_login_missing_email(self):
        login_page.open_login_form()
        login_page.enter_password_data("Validpassword2022")
        login_page.click_login_button()
        self.assertFalse(
            login_page.verify_opened_successfully_and_component_present(base_data["component_on_home_page"]))

    def test_login_invalid_email(self):
        login_page.open_login_form()
        login_page.enter_email_data("dvnjsdbvdc@abg.bg")
        login_page.enter_password_data("Validpassword2022")
        login_page.click_login_button()
        self.assertFalse(
            login_page.verify_opened_successfully_and_component_present(base_data["component_on_home_page"]))

    def test_login_invalid_password(self):
        login_page.open_login_form()
        login_page.enter_email_data("valid@abv.bg")
        login_page.enter_password_data("Poniponi2222")
        login_page.click_login_button()
        self.assertFalse(
            login_page.verify_opened_successfully_and_component_present(base_data["component_on_home_page"]))

    def test_login_forgotten_pass_valid_email(self):
        login_page.open_login_form()
        login_page.forgotten_pass("valid@abv.bg")
        result_popup = self.driver.find_element(By.XPATH, base_data["forgotten_pass_popup_valid_email"])
        self.assertEqual("Изпратени са инструкции на e-mail " 
                         "antonia333@abv.bg как да активираш "
                         "акаунта си и да зададеш нова парола.", result_popup.text)

    def test_login_forgotten_pass_invalid_email(self):
        login_page.open_login_form()
        login_page.forgotten_pass("lalalalalal@avv.bg")
        result_popup = self.driver.find_element(By.XPATH, base_data["forgotten_pass_popup_invalid_email"])
        self.assertEqual("Не съществува акаунт с този e-mail адрес.", result_popup.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Me/PycharmProjects/unnittestProject/reports'))

