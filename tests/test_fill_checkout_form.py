from playwright.sync_api import Page, expect
from conftest import cart
from pages.fill_checkout_form import Fill_checkout
from pages.view_cart import View_cart


def test_fill_checkout_form(logged_in_page, cart, page: Page):

    view_my_cart = View_cart(logged_in_page)
    view_my_cart.view_cart()     
    view_my_cart.my_checkout_button()
    check_out_form = Fill_checkout(page)
    check_out_form.fill_firstname()
    check_out_form.fill_lastname()
    check_out_form.fill_postalcode()
    check_out_form.click_button()

    assert page.url == ("https://www.saucedemo.com/checkout-step-two.html")