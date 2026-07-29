import re 
from playwright.sync_api import Page, expect

class Add_to_cart:

    def __init__(self, page : Page):

        self.page = page

        #Locators
        self.add_to_cart = page.locator("[data-test=add-to-cart]")
        self.view_item_locator = page.locator("[data-test=item-1-title-link]")
        self.view_item_in_cart = page.locator("[data-test=item-quantity]")

    #Methods
    def is_add_to_cart_visible(self):
        return self.add_to_cart.is_visible()
    
    def check_item_in_cart(self):
        item_count = self.view_item_locator.count
        assert item_count
    
    def view_item_in_inventory(self):
        self.view_item_locator.click()

    def click_add_to_cart_button(self):
        self.add_to_cart.click()