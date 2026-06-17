from playwright.sync_api import Page, expect
from conftest import logged_in_page, cart
from pages.continue_shopping import Continue_shopping




def test_continue_shopping(cart):
    
    continue_to_shop = Continue_shopping(cart)
    continue_to_shop.click_continue_shopping_button()
    continue_to_shop.add_item_one()
    continue_to_shop.add_item_two()

    assert continue_to_shop.check_cart_count() == '3'










