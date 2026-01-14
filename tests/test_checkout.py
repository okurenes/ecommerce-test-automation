import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import TestData

class TestCheckout:
    """Checkout süreci test class'ı"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Her test öncesi ürün ekle ve checkout'a git"""
        login_page = LoginPage(driver)
        login_page.open(base_url)
        login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        
        products_page = ProductsPage(driver)
        products_page.add_first_product_to_cart()
        products_page.go_to_cart()
        
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()
        
        self.checkout_page = CheckoutPage(driver)
    
    def test_successful_checkout(self, driver):
        """Başarılı checkout süreci end-to-end testi"""
        # Checkout bilgilerini doldur
        self.checkout_page.fill_checkout_info(
            TestData.CHECKOUT_FIRSTNAME,
            TestData.CHECKOUT_LASTNAME,
            TestData.CHECKOUT_ZIPCODE
        )
        
        # Continue ve Finish
        self.checkout_page.click_continue()
        self.checkout_page.click_finish()
        
        # Siparişin tamamlandığını doğrula
        assert self.checkout_page.is_order_complete(), "Sipariş tamamlanamadı"
        assert "Thank you" in self.checkout_page.get_complete_message()
    
    def test_checkout_with_empty_firstname(self, driver):
        """Boş firstname ile checkout testi"""
        self.checkout_page.fill_checkout_info(
            "",
            TestData.CHECKOUT_LASTNAME,
            TestData.CHECKOUT_ZIPCODE
        )
        
        self.checkout_page.click_continue()
        
        # Hata kontrolü yapılabilir (site destekliyorsa)
