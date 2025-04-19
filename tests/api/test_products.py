import pytest
import requests

# Проверяет Получение всех продуктов
def test_get_all_products(base_url):
    response = requests.get(f"{base_url}/products")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Проверка наличия данных

# Проверяет Получение продукта по ID
def test_get_single_product(base_url):
    product_id = 1
    response = requests.get(f"{base_url}/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["id"] == product_id  # Проверка корректного ID

# Проверяет Создание нового продукта
def test_create_product(base_url, product_data):
    response = requests.post(f"{base_url}/products", json=product_data)
    assert response.status_code == 200
    assert response.json()["title"] == product_data["title"]  # Проверка создания

# Проверяет  Обновление продукта
def test_update_product(base_url, product_data):
    product_id = 1
    response = requests.put(f"{base_url}/products/{product_id}", json=product_data)
    assert response.status_code == 200
    assert response.json()["price"] == product_data["price"]  # Проверка обновления

# Проверяет  Удаление продукта
def test_delete_product(base_url):
    product_id = 1
    response = requests.delete(f"{base_url}/products/{product_id}")
    assert response.status_code == 200  # Проверка удаления