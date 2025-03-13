from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SeleniumDriver:
    def __init__(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        options = Options()
        options.add_argument("--headless") 
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument(f"user-agent={user_agent}")  

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)  
        
        self.product_data = {}

    def scrape_product(self, product_url: str) -> dict:
        try:
            self._load_product_page(product_url)
            self.product_data["name"] = self._extract_product_name()
            self.product_data["specifications"] = self._extract_specifications()
            self.product_data["key_features"] = self._extract_key_features()
            return self.product_data
        finally:
            self.quit()
            
    def _load_product_page(self, url: str):
        self.get(url)
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-name='productPage']"))
        )
        
    def _extract_specifications(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-name='specsGroup']"))
        ).text.strip()
    
    def _extract_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-name='productName']"))
        ).text.strip()
        
    def _extract_key_features(self):
         return self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-name='productAttributes']"))
        ).text.strip()
        
    def get(self, url: str):
        return self.driver.get(url)
    
    def quit(self):
        self.driver.quit()