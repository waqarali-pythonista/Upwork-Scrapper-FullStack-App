from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScraperService:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        #Use ChromeDriver path from .env
        #driver_path = os.getenv('SELENIUM_DRIVER_PATH')
        #driver = webdriver.Chrome(executable_path=driver_path)
        
        driver = webdriver.Chrome()

        try:
            driver.get(self.url)

            # Extract the header (h4)
            header_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div[1]/div/div/header/h4"))
            )
            header_text = header_element.text

            # Extract the description (p)
            description_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[1]/div/p"))
            )
            description_text = description_element.text

            return header_text, description_text

        finally:
            driver.quit()
