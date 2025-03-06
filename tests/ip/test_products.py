import requests

BASE_URL = "https://fakestoreapi.com"

def test_get_all_products():
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Проверка наличия данных <button class="citation-flag" data-index="1">

def test_create_product():
    payload = {"title": "Test Product", "price": 10.99, "description": "Test", "image": "test.jpg", "category": "electronics"}
    response = requests.post(f"{BASE_URL}/products", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Product"  # Проверка создания <button class="citation-flag" data-index="8">