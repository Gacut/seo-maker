
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from processors.selenium import SeleniumDriver
from utils.insert_text import insert_text



class Scraper:
    def __init__(self, product_url):
        self.selenium = SeleniumDriver()
        self.product_data = {}
        self.product_url = product_url

    def _scrape_product(self, product_url: str) -> dict:
        try:
            self._load_product_page(product_url)
            self.product_data["name"] = self._extract_product_name()
            self.product_data["specifications"] = self._extract_specifications()
            self.product_data["key_features"] = self._extract_key_features()
            self.product_data["key_features"] = self.product_data["key_features"].replace("Zobacz wszystkie cechy",'')
            self.product_data["key_features"] = self.product_data["key_features"].replace("Pokaż więcej wyników",'')
            self.product_data["specifications"] = self.product_data["specifications"].replace("Dane techniczne",'')
            return self.product_data
        finally:
            self.selenium.quit()
            
    def _load_product_page(self, url: str):
        self.selenium.get(url)
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-name='productPage']"))
        )
        
    def _extract_specifications(self):
        return self.selenium.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-name='specsGroup']"))
        ).text.strip()
    
    def _extract_product_name(self):
        return self.selenium.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-name='productName']"))
        ).text.strip()
        
    def _extract_key_features(self):
         return self.selenium.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-name='productAttributes']"))
        ).text.strip()
         
    def generate_input(self):
        
        try:
            scraped_data = self.selenium.scrape_product(self.product_url)
            
        except Exception as e:
            print(f"Error while scraping {self.product_url}: {str(e)}")
        finally:
            self.selenium.quit() 
            
        input_template = f"""
        <nazwa produktu>
        {scraped_data["name"]}
        </nazwa produktu>
        <specyfikacja techniczna>
        {scraped_data["specifications"]}
        </specyfikacja techniczna>
        <cechy kluczowe>
        {scraped_data["key_features"]}
        </cechy kluczowe>
        """
        return input_template
    
   
        