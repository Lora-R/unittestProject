from imported_library.used_librabies import By, WebDriverWait, EC, NoSuchElementException
from pages.initialize_driver import initialized_driver
from variables.config_data import base_data

list_pops_elements = ["/html/body/div[1]/div/a", "/html/body/div[109]/div[2]/div[1]/a",
                      "/html/body/div[111]/div/div", '//*[@id="yd_close"]']


class LoginPage:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
        return cls.instance

    def __init__(self):
        self.driver = initialized_driver.get_driver()

    @staticmethod
    def open_login_form():
        initialized_driver.load_website()
        initialized_driver.go_to_page("https://grabo.bg/user/signin")

    def enter_email_data(self, email):
        email_field = self.driver.find_element(By.XPATH, base_data["xpath_email"])
        email_field.send_keys(email)

    def enter_password_data(self, password):
        password_field = self.driver.find_element(By.XPATH, base_data["xpath_password"])
        password_field.send_keys(password)

    def click_login_button(self):
        login_btn = self.driver.find_element(By.XPATH, base_data["xpath_login_btn"])
        login_btn.click()

    def forgotten_pass(self, email):
        forgotten_pass_button = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, base_data["xpath_forgotten_pass_button"])))
        forgotten_pass_button.click()

        email_field = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, base_data["xpath_email"])))
        email_field.send_keys(email)

        send_button = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, base_data["forgotten_pass_send_email_button"])))
        send_button.click()

    # def check_popups(self, check_el_appears):
    #     self.driver.refresh()
    #     if not self.driver.find_element(By.XPATH, check_el_appears):
    #         still_popup = True
    #         while still_popup:
    #             for el in list_pops_elements:
    #                 popup_el_close_button = WebDriverWait(self.driver, 30). \
    #                     until(EC.presence_of_element_located((By.XPATH, el)))
    #                 popup_el_close_button.click()
    #                 if self.driver.find_element(By.XPATH, check_el_appears):
    #                     still_popup = False
    #     else:
    #         print("no popups")

    def verify_opened_successfully_and_component_present(self, component):
        try:
            if self.driver.find_element(By.XPATH, component).is_displayed():
                return True
        except NoSuchElementException as ex:
            return False

    @staticmethod
    def close_window():
        initialized_driver.quit_driver()


login_page = LoginPage()
