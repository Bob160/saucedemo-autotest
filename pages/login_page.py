import re 
from playwright.sync_api import Page, expect

class LoginPage:

    def __init__(self, page : Page):
        self.page = page

        #Locators
        # self.username_input = page.locator("[data-test=username]")
        # self.password_input = page.locator("[data-test=password]")
        # self.login_button = page.locator("[data-test=login-button]")

        self.username_input = page.get_by_test_id("username")
        self.password_input = page.get_by_test_id("password")
        self.login_button = page.get_by_test_id("login-button")
    #Methods

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
         
            