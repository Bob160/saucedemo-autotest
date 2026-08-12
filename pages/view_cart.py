import re 
from playwright.sync_api import Page, expect

class View_cart:
    def __init__(self, page : Page):
        self.page = page

        #Locators
        # self.click_cart = page.locator("[data-test=shopping-cart-link]")
        # self.checkout_button = page.locator("[data-test=checkout]")

        self.click_cart = page.get_by_test_id("shopping-cart-link")
        self.checkout_button = page.get_by_test_id("checkout")

        #Method

    def view_cart(self):
        self.click_cart.click()

    def my_checkout_button(self):
        self.checkout_button.click()