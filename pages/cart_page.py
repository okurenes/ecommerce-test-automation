from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class CartPage(BasePage):
    """Sepet sayfası için Page Object"""
    
    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id^='remove']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_cart_items_count(self):
        """Sepetteki ürün sayısını döner"""
        try:
            return len(self.find_elements(self.CART_ITEMS))
        except:
            return 0
    
    def proceed_to_checkout(self):
        """Checkout sayfasına ilerler"""
        self.click(self.CHECKOUT_BUTTON)
    
    def continue_shopping(self):
        """Alışverişe devam et"""
        self.click(self.CONTINUE_SHOPPING)
    
    def remove_first_item(self):
        """İlk ürünü sepetten çıkarır"""
        buttons = self.find_elements(self.REMOVE_BUTTONS)
        if buttons:
            buttons[0].click()
            time.sleep(1)  # Ürün çıkarılması için kısa bekleme
