from playwright.sync_api import sync_playwright, Page, expect
from tests.test_login_test import test_login
from pages.add_to_cart import Add_to_cart
import os
from dotenv import load_dotenv

load_dotenv(override=False)

def test_add_to_cart(page : Page) -> None:

    #Login
    test_login(page)
    
    #Run the methods - view item in the inventory, then check if add to cart button is visible, then add item to cart, and finally check that item is in the cart
    cart = Add_to_cart(page)
    cart.view_item_in_inventory()
    cart.is_add_to_cart_visible()
    cart.click_add_to_cart_button()
    cart.check_item_in_cart()






