import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.driver_factory import DriverFactory

@pytest.fixture(scope="function")
def driver():
    """Her test için yeni bir browser instance oluşturur"""
    driver = DriverFactory.create_driver("chrome")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    """Test edilecek site URL'i"""
    return "https://www.saucedemo.com"
