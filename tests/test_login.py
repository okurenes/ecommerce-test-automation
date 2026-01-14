import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.test_data import TestData

class TestLogin:
    """Login fonksiyonalitesi test class'ı"""
    
    def test_successful_login(self, driver, base_url):
        """Geçerli kullanıcı bilgileriyle login testi"""
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        
        # Login sayfasını aç
        login_page.open(base_url)
        
        # Valid credentials ile login ol
        login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        
        # Products sayfasının açıldığını doğrula
        assert products_page.is_products_page_displayed(), "Login başarısız, products sayfası açılmadı"
    
    def test_invalid_username_login(self, driver, base_url):
        """Geçersiz kullanıcı adı ile login testi"""
        login_page = LoginPage(driver)
        
        login_page.open(base_url)
        login_page.login(TestData.INVALID_USERNAME, TestData.VALID_PASSWORD)
        
        # Hata mesajının göründüğünü doğrula
        assert login_page.is_error_displayed(), "Hata mesajı gösterilmedi"
        assert "Epic sadface" in login_page.get_error_message()
    
    def test_invalid_password_login(self, driver, base_url):
        """Geçersiz şifre ile login testi"""
        login_page = LoginPage(driver)
        
        login_page.open(base_url)
        login_page.login(TestData.VALID_USERNAME, TestData.INVALID_PASSWORD)
        
        assert login_page.is_error_displayed(), "Hata mesajı gösterilmedi"
    
    def test_locked_user_login(self, driver, base_url):
        """Kilitli kullanıcı ile login testi"""
        login_page = LoginPage(driver)
        
        login_page.open(base_url)
        login_page.login(TestData.LOCKED_USERNAME, TestData.VALID_PASSWORD)
        
        # Locked user mesajını doğrula
        assert login_page.is_error_displayed()
        assert "locked out" in login_page.get_error_message().lower()
    
    def test_empty_credentials_login(self, driver, base_url):
        """Boş credentials ile login testi"""
        login_page = LoginPage(driver)
        
        login_page.open(base_url)
        login_page.login("", "")
        
        assert login_page.is_error_displayed(), "Hata mesajı gösterilmedi"
