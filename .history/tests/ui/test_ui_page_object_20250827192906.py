from modules.ui.page_objects.sign_in_page import SignInPage
import pytest

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # Создание объекта страницы авторизации
    sign_in_page = SignInPage()
    
    # Открытие страницы авторизации GitHub
    sign_in_page.go_to()
    
    # Выполняем попытку входа в систему GitHub
    sign_in_page.try_login("incorrect_username@mistaked_domain.com", "incorrect_password")
    
    # Проверка, что название страницы соответствует ожидаемому
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    
    # Закрытие браузера
    sign_in_page.close()