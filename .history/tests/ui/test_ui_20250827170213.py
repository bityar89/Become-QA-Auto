import pytest

from selenium import webdriver
from selenium.webdriver.common.service import Service

@pytest.mark.ui
def test_check_incorrect_username():
    # Создание объекта WebDriver для управления браузером
    driver = webdriver.Chrome(service=Service(r"C:\Users\Ярик\Desktop\AutomationGIT\Become-QA-Auto\chromedriver-win64\chromedriver.exe"))
    
    # Открытие страницы авторизации GitHub
    driver.get("https://github.com/login")
    
    # Ввод некорректного имени пользователя
    username_input = driver.find_element("id", "login_field")
    username_input.send_keys("incorrect_username")
    
    # Клик на кнопку "Next"