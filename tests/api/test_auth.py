import pytest
import requests

# Проверяет Успешная аутентификация
def test_successful_login(auth_token):
    assert auth_token is not None  # Проверка получения токена

# Проверяет Неудачная аутентификация
def test_failed_login(base_url):
    response = requests.post(
        f"{base_url}/auth/login",
        json={"username": "wrong_user", "password": "wrong_pass"}
    )
    assert response.status_code == 401  # Проверка ошибки авторизации