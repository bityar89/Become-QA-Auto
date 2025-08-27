import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    # Создание объекта WebDriver для управления браузером
    driver = webdriver.Chrome(service=Service(r"C:\Users\Ярик\Desktop\AutomationGIT\Become-QA-Auto\chromedriver-win64\chromedriver.exe"))
    
    # Открытие страницы авторизации GitHub
    driver.get("https://github.com/login")
    
    # Находим поле для ввода логина
    login_elem = driver.find_element(By.ID, "login_field")
    
    # Ввод некорректного логина
    username_field.send_keys("incorrect_username")
    
    # Находим кнопку "Next"
    next_button = driver.find_element(By.XPATH, "//input[@value='Next']")
    
    # Закрытие браузера
    driver.close()