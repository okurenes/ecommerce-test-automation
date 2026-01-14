from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    """Ürünler sayfası için Page Object"""
    
    # Locators
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_products_page_displayed(self):
        """Ürünler sayfası açıldı mı kontrol eder"""
        return self.is_element_visible(self.PRODUCTS_TITLE)
    
    def get_products_count(self):
        """Sayfadaki ürün sayısını döner"""
        return len(self.find_elements(self.INVENTORY_ITEMS))
    
    def add_first_product_to_cart(self):
        """İlk ürünü sepete ekler"""
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        buttons[0].click()
    
    def get_cart_badge_count(self):
        """Sepet badge'indeki sayıyı döner"""
        try:
            return int(self.get_text(self.SHOPPING_CART_BADGE))
        except:
            return 0
    
    def go_to_cart(self):
        """Sepet sayfasına gider"""
        self.click(self.SHOPPING_CART_LINK)
