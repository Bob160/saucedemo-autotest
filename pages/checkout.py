import re 
from playwright.sync_api import Page, expect

class Checkout_page:

    def __init__ (self, page : Page):
        self.page = page


        #Locators
        self.open_cart = page.locator("[data-test=\"shopping-cart-link\"]")
        self.click_checkout = page.locator("[data-test=\"checkout\"]")

    #Methods
    def view_cart(self):
        self.open_cart.click()

    def check_out(self):
        self.click_checkout.click()