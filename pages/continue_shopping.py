import re 
from playwright.sync_api import Page, expect

class Continue_shopping:
    
    def __init__(self, page : Page):
        self.page = page

        #Locator

        self.continue_shopping = page.locator("[data-test=\"continue-shopping\"]")
        self.add_first_item = page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        self.add_second_item = page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]")
        self.cart_count = page.locator("[data-test=\"shopping-cart-badge\"]")

        #Method
    
    def click_continue_shopping_button(self):
        self.continue_shopping.click()

    def add_item_one(self):
        self.add_first_item.click()

    def add_item_two(self):
        self.add_second_item.click()
    
    # def check_cart_count(self, expected_count):
    #     return self.cart_count.text_content()

    def check_cart_count(self, expected_count):
        expect(self.cart_count).to_have_text(str(expected_count)== "3")