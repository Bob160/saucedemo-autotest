from playwright.sync_api import sync_playwright, Page, expect
from tests.test_login_test import test_login
from pages.login_page import LoginPage
from pages.add_to_cart import Add_to_cart
from conftest import logged_in_page


def test_add_to_cart(logged_in_page) -> None:
    
    cart = Add_to_cart(logged_in_page)

    cart.view_item_in_inventory()
    cart.is_add_to_cart_visible()
    cart.click_add_to_cart_button()
    cart.check_item_in_cart()