import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru, en-gb, es, fr")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart chrome browser for test...")
        browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser...")
    browser.quit()