#from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import os
from dotenv import load_dotenv


load_dotenv(override=False)

def test_login (page : Page) -> None:

    base_url = os.getenv("BASE_URL")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    
    

    #load_dotenv(override=False)

    #my_username = os.getenv("USERNAME")
    # login_page.load_page()
    page.goto(base_url)

    login_page = LoginPage(page)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()




# def run():
#     with sync_playwright() as p:
    
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto('https://www.saucedemo.com')
#         page.fill('input[name="user-name"]', 'standard_user')
#         page.fill('input[name="password"]', 'secret_sauce')
#         page.locator('#login-button').click()
#         print("Login successful!")
#         browser.close()

# if __name__ == "__main__":
#     run()
