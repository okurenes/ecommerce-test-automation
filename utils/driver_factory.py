from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:
    """WebDriver oluşturma factory class"""
    
    @staticmethod
    def create_driver(browser="chrome", headless=False):
        """
        Belirtilen browser tipinde driver oluşturur
        
        Args:
            browser: Browser tipi (chrome, firefox)
            headless: Headless modda çalışsın mı
        
        Returns:
            WebDriver instance
        """
        if browser.lower() == "chrome":
            options = Options()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            return driver
        
        else:
            raise ValueError(f"Desteklenmeyen browser: {browser}")
