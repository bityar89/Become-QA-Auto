from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"C:\Users\Ярик\Desktop\AutomationGIT\FirstStepsInAutomation\chromedriver-win64\\"
    DRIVER_NAME = "chromedriver.exe"
    
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(BasePage.PATH + BasePage.DRIVER_NAME))
        
    def close(self):
        self.driver.close()
        