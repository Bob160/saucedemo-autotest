import re 
from playwright.sync_api import Page, expect

class Remove_from_cart:

    def __init__(self, page : Page):
        self.page = page

        #Locators
        self.add_first_item = page.locator("[data-test=add-to-cart-sauce-labs-bike-light]")
        self.add_second_item = page.locator("[data-test=add-to-cart-sauce-labs-onesie]")
        self.open_cart = page.locator("[data-test=shopping-cart-link]")
        self.remove = page.locator("[data-test=remove-sauce-labs-bike-light]")
        self.check_number = page.locator("[data-test=shopping-cart-badge]")


    def item_one(self):
        self.add_first_item.click()
    
    def item_two(self):
        self.add_second_item.click()
    
    def open_the_cart(self):
        self.open_cart.click()

    def remove_item (self):
        self.remove.click()
    
    def cart_number (self):
        return self.check_number.text_content()