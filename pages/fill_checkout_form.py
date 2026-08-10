import re 
from playwright.sync_api import Page

class Fill_checkout:

    def __init__(self, page : Page):
        self.page = page

        # self.firstname = page.locator("[data-test=firstName]")
        # self.lastname = page.locator("[data-test=lastName]")
        # self.postalcode = page.locator("[data-test=postalCode]")
        # self.continue_button = page.locator("[data-test=continue]")
        
        self.firstname = page.get_by_test_id("firstName")
        self.lastname = page.get_by_test_id("lastName")
        self.postalcode = page.get_by_test_id("postalCode")
        self.continue_button = page.get_by_test_id("continue")

    def fill_firstname(self):
        self.firstname.fill("Bob")

    def fill_lastname(self):
        self.lastname.fill("Rox")
    
    def fill_postalcode(self):
        self.postalcode.fill("L76 B43")
    
    def click_button(self):
        self.continue_button.click()

#Have one method that clicks and fills