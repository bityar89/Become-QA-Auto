from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = "https://github.com/login"
    
    def __init__(self):
        super().__init__()
        
    def go_to(self):
        self.driver.get(SignInPage.URL)
        
    def try_login(self, username, password):
        # Находим поле для ввода логина
        login_elem = self.driver.find_element(By.ID, "login_field")
        
        # Ввод логина
        login_elem.send_keys(username)
        
        # Находим поле для ввода пароля
        pass_elem = self.driver.find_element(By.ID, "password")
        
        # Ввод пароля
        pass_elem.send_keys(password)
        
        # Находим кнопку "Sign in"
        sign_in_elem = self.driver.find_element(By.NAME, "commit")
        
        # Кликнуть на кнопку "Sign in"
        sign_in_elem.click()
        
    def check_title(self, expected_title):
        return self.driver.title == expected_title