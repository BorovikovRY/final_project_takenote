import pytest
import allure
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    # Запускаем Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Можно изменить на headless=True для запуска без UI
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    # Создаём новую страницу
    page = browser.new_page()
    yield page
    page.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Проверяем, что тест завершился с ошибкой
    if rep.when == "call" and rep.failed:
        # Получаем объект page из фикстуры
        page = item.funcargs.get("page")
        if page:
            # Делаем скриншот и прикрепляем его к отчёту Allure
            allure.attach(
                page.screenshot(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )