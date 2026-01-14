from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    """Checkout sayfası için Page Object"""
    
    # Locators
    FIRSTNAME_INPUT = (By.ID, "first-name")
    LASTNAME_INPUT = (By.ID, "last-name")
    ZIPCODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_checkout_info(self, firstname, lastname, zipcode):
        """Checkout bilgilerini doldurur"""
        self.type(self.FIRSTNAME_INPUT, firstname)
        self.type(self.LASTNAME_INPUT, lastname)
        self.type(self.ZIPCODE_INPUT, zipcode)
    
    def click_continue(self):
        """Continue butonuna tıklar"""
        self.click(self.CONTINUE_BUTTON)
    
    def click_finish(self):
        """Finish butonuna tıklar"""
        self.click(self.FINISH_BUTTON)
    
    def is_order_complete(self):
        """Sipariş tamamlandı mı kontrol eder"""
        return self.is_element_visible(self.COMPLETE_HEADER)
    
    def get_complete_message(self):
        """Tamamlanma mesajını döner"""
        return self.get_text(self.COMPLETE_HEADER)
