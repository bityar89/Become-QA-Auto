import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_check_incorrect_username():
    # Создание объекта WebDriver для управления браузером
    driver = webdriver.Chrome(service=Service(r"C:\Users\Ярик\Desktop\AutomationGIT\Become-QA-Auto\chromedriver-win64\chromedriver.exe"))
    
    # Открытие страницы авторизации GitHub
    driver.get("https://github.com/login")
    
    # Находим поле для ввода неправильного логина или почты
    login_elem = driver.find_element(By.ID, "login_field")
    
    # Ввод некорректного логина
    login_elem.send_keys("incorrect_username@mistaked_domain.com")
    
    #Находим поле для ввода пароля
    pass_elem = driver.find_element(By.ID, "password")
    
    # Ввод некорректного пароля
    pass_elem.send_keys("incorrect_password")
    
    # Находим кнопку "Sign in"
    sign_in_elem = driver.find_element(By.NAME, "commit")
    
    # Кликнуть на кнопку "Sign in"
    sign_in_elem.click()
    time.sleep(3)
    
    # Проверка, что название страницы соответствует ожидаемому
    assert "Sign in to GitHub • GitHub" in driver.title
    
    # Закрытие браузера
    driver.close()