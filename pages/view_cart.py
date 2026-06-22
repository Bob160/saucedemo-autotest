import re 
from playwright.sync_api import Page, expect

class View_cart:
    def __init__(self, page : Page):
        self.page = page

        #Locators
        self.click_cart = page.locator("[data-test=\"shopping-cart-link\"]")

        #Method

    def view_cart(self):
        self.click_cart.click()
        