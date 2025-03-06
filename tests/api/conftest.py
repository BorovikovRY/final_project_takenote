import pytest
import requests

# Базовый URL для всех тестов <button class="citation-flag" data-index="3"><button class="citation-flag" data-index="8">
@pytest.fixture(scope="session")
def base_url():
    return "https://fakestoreapi.com"

# Тестовые данные для продуктов <button class="citation-flag" data-index="5">
@pytest.fixture
def product_data():
    return {
        "title": "Test Product",
        "price": 29.99,
        "description": "A product for testing",
        "image": "test.jpg",
        "category": "electronics"
    }

# Тестовые данные для пользователей <button class="citation-flag" data-index="5">
@pytest.fixture
def user_data():
    return {
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "test1234",
        "name": {"firstname": "Test", "lastname": "User"},
        "address": {"city": "Test City", "street": "Test St"}
    }

# Тестовые данные для корзин <button class="citation-flag" data-index="5">
@pytest.fixture
def cart_data():
    return {
        "userId": 2,
        "products": [{"productId": 2, "quantity": 3}]
    }

# Фикстура для получения токена аутентификации <button class="citation-flag" data-index="8">
@pytest.fixture(scope="session")
def auth_token():
    response = requests.post(
        "https://fakestoreapi.com/auth/login",
        json={"username": "mor_2314", "password": "83r5^_"}
    )
    return response.json().get("token")