import pytest
import requests

# Базовый URL для всех тестов
@pytest.fixture(scope="session")
def base_url():
    return "https://fakestoreapi.com"

# Тестовые данные для продуктов
@pytest.fixture
def product_data():
    return {
        "title": "Test Product",
        "price": 29.99,
        "description": "A product for testing",
        "image": "test.jpg",
        "category": "electronics"
    }

# Тестовые данные для пользователей
@pytest.fixture
def user_data():
    return {
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "test1234",
        "name": {"firstname": "Test", "lastname": "User"},
        "address": {"city": "Test City", "street": "Test St"}
    }

# Тестовые данные для корзин
@pytest.fixture
def cart_data():
    return {
        "userId": 2,
        "products": [{"productId": 2, "quantity": 3}]
    }

# Фикстура для получения токена аутентификации
@pytest.fixture(scope="session")
def auth_token():
    response = requests.post(
        "https://fakestoreapi.com/auth/login",
        json={"username": "mor_2314", "password": "83r5^_"}
    )
    return response.json().get("token")