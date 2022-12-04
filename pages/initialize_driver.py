from imported_library.used_librabies import webdriver, By, urljoin, Options, EdgeChromiumDriverManager, ChromeDriverManager, EdgeService, Service
from variables.config_data import base_data


class InitialDriver:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = InitialDriver()
        return cls.instance

    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        if str(base_data["browser"]).lower() == "edge":
            self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        elif str(base_data["browser"]).lower() == "chrome":
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        else:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(10)

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(base_data["url"])

    def go_to_page(self, page):
        self.driver.get(urljoin(base_data["url"], page.lower()))

    def verify_component_exists(self, component):
        if component in self.driver.find_element(By.CSS_SELECTOR, "html").text:
            return True
        else:
            return False

    def quit_driver(self):
        self.driver.quit()


initialized_driver = InitialDriver()
