from processors.selenium import SeleniumDriver 

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def main():
  
    scraper = SeleniumDriver()
    

    test_url = "https://www.komputronik.pl/product/952642/tablet-lenovo-tab-10-1-tb311xu-4-64gb-lte-zaej0034pl-szary.html"
    product_data = {}
    try:
   
        product_data = scraper.scrape_product(test_url)
        
    except Exception as e:
        print(f"Błąd podczas scrapowania: {str(e)}")
    finally:
        scraper.quit() 
        
    product_data["key_features"] = product_data["key_features"].replace("Zobacz wszystkie cechy",'')
    product_data["key_features"] = product_data["key_features"].replace("Pokaż więcej wyników",'')
    product_data["specifications"] = product_data["specifications"].replace("Dane techniczne",'')
    
    input_template = f"""
    <nazwa produktu>
    {product_data["name"]}
    </nazwa produktu>
    <specyfikacja techniczna>
    {product_data["specifications"]}
    </specyfikacja techniczna>
    <cechy kluczowe>
    {product_data["key_features"]}
    </cechy kluczowe>
    """
    print(input_template)
    
# TERA TO UPAKOWAC W FUNKCJE ODPOWIEDNIA -> PRZYPISAC DO BUTTONA -> ZROBIĆ ŻEBY SIE INSERTOWALO W LEWE OKIENKO
    
  
if __name__ == "__main__":
    main()