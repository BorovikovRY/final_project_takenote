# 📌 Автоматизация тестирования TakeNote с Playwright

## 🚀 Описание
Этот проект содержит автоматизированные UI-тесты для веб-приложения [TakeNote](https://takenote.dev/app), написанные с использованием **Python + Playwright + Pytest**.

## 🛠 Установка

1. Установите **Python 3.8+** (если не установлен).
2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ВАШ_РЕПОЗИТОРИЙ.git
   cd ВАШ_РЕПОЗИТОРИЙ
3. Создайте виртуальное окружение:
python -m venv venv
4. Запуск тестов
pytest tests/
5. Запуск с отчетом Allure:
pytest tests/ --alluredir=allure-results
6. Открыть отчёт 
allure serve allure-results

