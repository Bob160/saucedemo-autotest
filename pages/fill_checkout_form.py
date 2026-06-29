import re 
from playwright.sync_api import Page

class Fill_checkout:

    def __init__(self, page : Page):
        self.page = page

        self.firstname = page.locator("[data-test=\"firstName\"]")
        self.lastname = page.locator("[data-test=\"lastName\"]")
        self.postalcode = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")

    def click_firstname(self):
        self.firstname.click()

    def fill_firstname(self):
        self.firstname.fill("Bob")

    def click_lastname(self):
        self.lastname.click()

    def fill_lastname(self):
        self.lastname.fill("Rox")
    
    def click_postalcode(self):
        self.postalcode.click()
    
    def fill_postalcode(self):
        self.postalcode.fill("L76 B43")
    
    def click_button(self):
        self.continue_button.click()
    
#Have one method that clicks and fills