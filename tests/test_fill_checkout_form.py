from playwright.sync_api import Page, expect
from conftest import cart
from pages.fill_checkout_form import Fill_checkout


def test_fill_checkout_form(cart, page: Page):

    check_out_form = Fill_checkout(page)

    check_out_form.click_firstname()
    check_out_form.fill_firstname()
    check_out_form.click_lastname()
    check_out_form.fill_firstname()
    check_out_form.click_postalcode()
    check_out_form.fill_postalcode()
    check_out_form.click_button()

    assert page.url == ("https://www.saucedemo.com/checkout-step-two.html")