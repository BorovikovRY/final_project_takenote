import pytest
import requests

# Проверяет Получение всех корзин
def test_get_all_carts(base_url):
    response = requests.get(f"{base_url}/carts")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Проверка наличия данных

# Проверяет Создание новой корзины
def test_create_cart(base_url, cart_data):
    response = requests.post(f"{base_url}/carts", json=cart_data)
    assert response.status_code == 200
    assert response.json()["userId"] == cart_data["userId"]  # Проверка создания

# Проверяет Обновление корзины
def test_update_cart(base_url, cart_data):
    cart_id = 1
    response = requests.put(f"{base_url}/carts/{cart_id}", json=cart_data)
    assert response.status_code == 200
    assert response.json()["products"][0]["quantity"] == cart_data["products"][0]["quantity"]  # Проверка обновления

# Проверяет Удаление корзины
def test_delete_cart(base_url):
    cart_id = 1
    response = requests.delete(f"{base_url}/carts/{cart_id}")
    assert response.status_code == 200  # Проверка удаления