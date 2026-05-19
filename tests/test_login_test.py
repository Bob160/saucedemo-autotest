from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
    
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.saucedemo.com')
        page.fill('input[name="user-name"]', 'standard_user')
        page.fill('input[name="password"]', 'secret_sauce')
        page.locator('#login-button').click()
        print("Login successful!")
        browser.close()

if __name__ == "__main__":
    run()
