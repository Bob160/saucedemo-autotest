import re 
from playwright.sync_api import Page, expect

class Checkout_page:

    def __init__ (self, page : Page):
        self.page = page


        #Locators
        # self.open_cart = page.locator("[data-test=shopping-cart-link]")
        # self.click_checkout = page.locator("[data-test=checkout]")
        self.open_cart = page.get_by_test_id("shopping-cart-link")
        self.click_checkout = page.get_by_test_id("checkout")
        #self.command = page.wait_for_url("**/checkout-step-one.html") add this to the check_out function

    #Methods
    def view_cart(self):
        self.open_cart.click()

    def check_out(self):
        self.click_checkout.click()

    # def make_assertion(self):
    #     self.command