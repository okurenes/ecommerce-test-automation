import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.test_data import TestData

class TestProducts:
    """Ürünler sayfası test class'ı"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Her test öncesi login işlemi"""
        login_page = LoginPage(driver)
        login_page.open(base_url)
        login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        self.products_page = ProductsPage(driver)
    
    def test_products_displayed(self, driver):
        """Ürünlerin görüntülendiği testi"""
        products_count = self.products_page.get_products_count()
        assert products_count > 0, "Hiç ürün görüntülenmiyor"
        assert products_count == 6, f"Beklenen 6 ürün, görüntülenen {products_count}"
    
    def test_add_product_to_cart(self, driver):
        """Sepete ürün ekleme testi"""
        # Başlangıçta sepet badge'i olmamalı
        initial_count = self.products_page.get_cart_badge_count()
        assert initial_count == 0, "Sepet başlangıçta boş olmalı"
        
        # Ürün ekle
        self.products_page.add_first_product_to_cart()
        
        # Sepet badge'inin 1 olduğunu doğrula
        badge_count = self.products_page.get_cart_badge_count()
        assert badge_count == 1, f"Sepet badge beklenen 1, görünen {badge_count}"
