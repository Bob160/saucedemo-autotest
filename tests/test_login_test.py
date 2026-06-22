from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from config import Config

import os


def test_login (page : Page) -> None:

    page.goto(Config.BASE_URL)

    login_page = LoginPage(page)

    login_page.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    page.wait_for_url('**/inventory.html')

    assert page.url == ('https://www.saucedemo.com/inventory.html')

    #assert "inventory.html" in page.url