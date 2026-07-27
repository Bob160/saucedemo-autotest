from playwright.sync_api import Page, expect
#from conftest import logged_in_page, cart
from pages.continue_shopping import Continue_shopping
from pages.view_cart import View_cart


def test_continue_shopping(logged_in_page, cart, page : Page):

    view_my_cart = View_cart(logged_in_page)
    view_my_cart.view_cart()
    
    continue_to_shop = Continue_shopping(logged_in_page)
    continue_to_shop.click_continue_shopping_button()
    continue_to_shop.add_item_one()
    continue_to_shop.add_item_two()










