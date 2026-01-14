from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """Tüm page object'lerin inherit edeceği base class"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Element bulur ve döner"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """Birden fazla element bulur"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        """Element'e tıklar"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def type(self, locator, text):
        """Element'e text yazar"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Element'in text'ini döner"""
        return self.find_element(locator).text
    
    def is_element_visible(self, locator, timeout=10):
        """Element görünür mü kontrol eder"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
