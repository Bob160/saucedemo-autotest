from playwright.sync_api import Page, expect
from conftest import cart
from pages.checkout import Checkout_page

def test_checkout(cart, page : Page):

    #add to fixture
    checkout_from_shop = Checkout_page(page)

    cart.view_item_in_inventory()
    cart.is_add_to_cart_visible()
    checkout_from_shop.view_cart()
    checkout_from_shop.check_out()

    #page.wait_for_url("**/checkout-step-one.html")

    #assert page.url == ("https://www.saucedemo.com/checkout-step-one.html") add to POM