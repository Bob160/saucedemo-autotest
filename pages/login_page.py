import re 
from playwright.sync_api import Page, expect


# def test_example(page: Page) -> None:
#     page.locator("[data-test=\"username\"]").click()
#     page.locator("[data-test=\"username\"]").fill("standard_user")
#     page.locator("[data-test=\"username\"]").press("Tab")
#     page.locator("[data-test=\"password\"]").fill("secret_sauce")
#     page.locator("[data-test=\"login-button\"]").click()


class LoginPage:

    def __init__(self, page : Page):
        self.page = page

        #Locators
        self.username_input = page.locator("[data-test=\"username\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")

    #Methods

    # def load_page (self):
    #     self.page.goto("https://www.saucedemo.com/")


    def enter_username (self, username : str):
        self.username_input.fill(username)

    def enter_password (self, password : str):
        self.password_input.fill(password)

    def click_login (self):
        self.login_button.click()


    # def __init__(self, page : Page):
    #     self.page = page

        # def login(self, username, password):
        #    self.username =  self.page.locator("[data-test=\"username\"]").fill("standard_user")
        #    self.password = self.page.locator("[data-test=\"password\"]").fill("secret_sauce")
        #    self.login = self.page.locator("[data-test=\"login-button\"]")
        #    self.login.click()
            
            