import pytest
import requests

# Проверяет  Получение всех пользователей
def test_get_all_users(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Проверка наличия данных

# Проверяет  Получение пользователя по ID
def test_get_single_user(base_url):
    user_id = 1
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id  # Проверка корректного ID


# Проверяет  Получение списка пользователей с ограничением количества (limit)
def test_get_users_with_limit(base_url):
    limit = 3
    response = requests.get(f"{base_url}/users", params={"limit": limit})
    assert response.status_code == 200  # Проверка успешного запроса
    assert len(response.json()) == limit  # Количество пользователей соответствует параметру

# Проверяет  Обновление пользователя
def test_update_user(base_url, user_data):
    user_id = 1
    response = requests.put(f"{base_url}/users/{user_id}", json=user_data)
    assert response.status_code == 200
    assert response.json()["username"] == user_data["username"]  # Проверка обновления

# ТПроверяет  Удаление пользователя
def test_delete_user(base_url):
    user_id = 1
    response = requests.delete(f"{base_url}/users/{user_id}")
    assert response.status_code == 200  # Проверка удаления