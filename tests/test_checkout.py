from playwright.sync_api import Page, expect
from conftest import cart
from pages.checkout import Checkout_page

def test_checkout(cart, page : Page):

    checkout_from_shop = Checkout_page(cart)

    checkout_from_shop.view_cart()
    checkout_from_shop.check_out()

    page.wait_for_url("**/checkout-step-one.html")

    assert page.url == ("https://www.saucedemo.com/checkout-step-one.html")