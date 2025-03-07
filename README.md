# Тестирование TakeNote и FakeStoreAPI

## Описание проекта
Проект содержит:
- **UI-тесты** для приложения [TakeNote](https://takenote.dev/app) с использованием Playwright и паттерна Page Object Model (POM)
- **API-тесты** для [FakeStoreAPI](https://fakestoreapi.com/) на библиотеке Requests
- Генерацию отчетов Allure

## Предварительные требования <button class="citation-flag" data-index="8"><button class="citation-flag" data-index="10">
- Python 3.8+
- Git
- Браузеры Chromium/Firefox/Webkit (для UI-тестов)

## Установка зависимостей и выполнение тестов <button class="citation-flag" data-index="9">
```bash

# Установка зависимостей
pip install -r requirements.txt
playwright install  # Загрузка браузеров для UI-тестов

# Полный запуск всех UI-тестов 
pytest tests/ui --alluredir=allure-results
# Полный запуск всех API-тестов
pytest tests/api --alluredir=allure-results

# Установка Allure (один раз)
npm install -g allure-commandline  

# Генерация отчета
allure serve allure-results