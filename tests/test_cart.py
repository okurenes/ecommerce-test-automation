import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.test_data import TestData

class TestCart:
    """Sepet fonksiyonalitesi test class'ı"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Her test öncesi login ve ürün ekleme"""
        login_page = LoginPage(driver)
        login_page.open(base_url)
        login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        
        self.products_page = ProductsPage(driver)
        self.products_page.add_first_product_to_cart()
        self.products_page.go_to_cart()
        
        self.cart_page = CartPage(driver)
    
    def test_cart_contains_added_product(self, driver):
        """Sepette eklenen ürün var mı testi"""
        cart_items = self.cart_page.get_cart_items_count()
        assert cart_items == 1, f"Sepette beklenen 1 ürün, bulunan {cart_items}"
    
    def test_remove_product_from_cart(self, driver):
        """Sepetten ürün çıkarma testi"""
        self.cart_page.remove_first_item()
        
        cart_items = self.cart_page.get_cart_items_count()
        assert cart_items == 0, "Ürün sepetten çıkarılamadı"
    
    def test_continue_shopping(self, driver):
        """Alışverişe devam et testi"""
        self.cart_page.continue_shopping()
        
        # Products sayfasına dönüldüğünü doğrula
        assert self.products_page.is_products_page_displayed()
