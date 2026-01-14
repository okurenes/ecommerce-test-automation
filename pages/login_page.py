from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Login sayfası için Page Object"""
    
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self, url):
        """Login sayfasını açar"""
        self.driver.get(url)
    
    def login(self, username, password):
        """Login işlemini gerçekleştirir"""
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Hata mesajını döner"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """Hata mesajı görünür mü kontrol eder"""
        return self.is_element_visible(self.ERROR_MESSAGE)
