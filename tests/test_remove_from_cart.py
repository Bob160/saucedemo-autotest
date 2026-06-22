from playwright.sync_api import Page, expect
from pages.remove_from_cart import Remove_from_cart
from conftest import logged_in_page


def test_remove_from_cart(logged_in_page, page : Page):
    remove_item = Remove_from_cart(logged_in_page)

    remove_item.item_one()
    remove_item.item_two()
    remove_item.open_the_cart()
    remove_item.remove_item()

    assert remove_item.cart_number() == "1"





