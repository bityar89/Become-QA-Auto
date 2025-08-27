import pytest

from selenium import webdriver
from selenium.webdriver.common.service import Service

@pytest.mark.ui
def test_check_incorrect_username():
    # Создание объекта WebDriver для управления браузером
    driver = webdriver.Chrome(service=Service(r"C:\Users\Ярик\Desktop\AutomationGIT\Become-QA-Auto\chromedriver-win64\chromedriver.exe"))