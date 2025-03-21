
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
        self.product_url = product_url
        
    def _scrape_product(self, product_url: str) -> dict:
        product_data = {}
        try:
            self._load_product_page(product_url)
            product_data["name"] = self._extract_product_name()
            
            raw_specs = self._extract_specifications()
            lines = raw_specs.split('\n')
            cleaned_specs = []
            skip_next = False
            
            for i, line in enumerate(lines):
                if skip_next:
                    skip_next = False
                    continue
            
                if line.strip() == "Gwarancja":
                    skip_next = True
                    continue
                
                if line.strip() == "Dane techniczne":
                    continue
                
                cleaned_specs.append(line)
            
            product_data["specifications"] = '\n'.join(cleaned_specs).strip()
            
            
            
            raw_features = self._extract_key_features()
            cleaned_features = []
            
            for line in raw_features.split('\n'):
                line = line.strip()
                if line.strip() == "Pokaż więcej wyników":
                    continue
                elif ':' in line:
                    header_part = line.split(':', 1)[0].strip()
                    cleaned_features.append(f"{header_part}")
                elif line and not line.isdigit():  
                    cleaned_features.append(f"{line}:")
            
            product_data["key_features"] = '\n'.join(cleaned_features).strip()
            
            return product_data
        finally:
            self.selenium.quit()
            
            
    def _load_product_page(self, url: str):
        self.selenium.get(url)
        self.selenium.wait.until(
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
            scraped_data = self._scrape_product(self.product_url)
            return f"""
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
        except Exception as e:
            print(f"Błąd podczas scrapowania: {str(e)}")
            return ""