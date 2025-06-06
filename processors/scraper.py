
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
    def __init__(self, product_url, text_processor):
        self.selenium = SeleniumDriver()
        self.product_url = product_url
        self.text_processor = text_processor
         
    def generate_input(self):
        try:
            scraped_data = self._scrape_product(self.product_url)
            self.text_processor.product_code    = scraped_data["product_code"]
            self.text_processor.image_urls      = scraped_data["image_urls"]
            self.text_processor.filename_source = 'code'
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
            print(f"Błąd podczas scrapowania: {e}")
            return ""    
        
    def _scrape_product(self, product_url: str) -> dict:
        product_data = {}
        try:
            self._load_product_page(product_url)
            product_data["name"] = self._extract_product_name()
            product_data["image_urls"]   = self._extract_image_urls()
            product_data["product_code"] = self._extract_product_code()
            raw_specs = self._extract_specifications()
            product_data["specifications"] = self._clean_specifications(raw_specs)
            product_data["key_features"] = self._extract_key_features()
            return product_data
        finally:
            self.selenium.quit()
            
            
    def _load_product_page(self, url: str):
        self.selenium.get(url)
        self.selenium.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-name='productPage']"))
        )
    
    
    def _extract_image_urls(self):
        gallery = self.selenium.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-name='productGallery']"))
        )
        images = gallery.find_elements(By.TAG_NAME, "img")
        return [
            img.get_attribute("src")
            for img in images
            if 'product-picture' in img.get_attribute("src")
        ]
        
    def _extract_product_code(self):
        images = self._extract_image_urls()
        image_url = images[0]
        filename = image_url.split('/')[-1]
        product_code = filename.split('-')[0]
        
        return product_code
    

    def _extract_specifications(self):
        specs_groups = self.selenium.wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[data-name='specsGroup']"))
        )
        group_texts = []
        for group in specs_groups:
            group_text = group.text.strip()
            lines = group_text.splitlines()
            if lines and lines[0].strip() == "Producent":
                continue 
            group_texts.append(group_text)
            
            
        return "\n\n".join(group_texts)
            
    def _clean_specifications(self, raw_specs:str) -> str:
        lines = raw_specs.split('\n')
        cleaned_specs = []
        skip_next = False
        
        for line in lines:
            if skip_next:
                skip_next = False
                continue

            if line.strip() == "Gwarancja":
                skip_next = True
                continue

            if line.strip() == "Dane techniczne":
                continue
            
            cleaned_specs.append(line)

        return "\n".join(cleaned_specs).strip()

    def _extract_product_name(self):
        return self.selenium.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-name='productName']"))
        ).text.strip()
        
    def _extract_key_features(self) -> str:
        container = self.selenium.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-name='productAttributes']"))
        )
        headers = []
        
        p_elements = container.find_elements(By.XPATH, ".//p[not(ancestor::label)]")
        for p in p_elements:
            text = p.text.strip()
            if text:
                headers.append(text.rstrip(":"))
        
        div_elements = container.find_elements(By.CSS_SELECTOR, "div.mt-4")
        for div in div_elements:
            if not div.find_elements(By.TAG_NAME, "p"):
                span_elements = div.find_elements(By.TAG_NAME, "span")
                for span in span_elements:
                    text = span.text.strip()
                    if text.endswith(":"):
                        headers.append(text.rstrip(":"))
                        break  
        
        unwanted_headers = ["Kolor", "Kolor obudowy"]
        filtered_headers = [header for header in headers if header not in unwanted_headers]
        
        return "\n".join(filtered_headers).strip()

      
        
   
        