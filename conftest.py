from playwright.sync_api import sync_playwright
#from tests.test_add_to_cart import test_add_to_cart
from pages.add_to_cart import Add_to_cart
from pages.login_page import LoginPage
from dotenv import load_dotenv
import pytest
import os



@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)

    page.goto("https://www.saucedemo.com")
    login_page.login(
        os.getenv("USERNAME"),
        os.getenv("PASSWORD")
    )
    return page


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute("data-test")
        browser = p.chromium.launch(headless= True, slow_mo=1000)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


# @pytest.fixture
# def cart(page):
#     return Add_to_cart(page)

@pytest.fixture
def cart(logged_in_page):
    return Add_to_cart(logged_in_page)

def pytest_html_report_title(report):
    report.title = "Saucedemo E2E Automated Test Report"