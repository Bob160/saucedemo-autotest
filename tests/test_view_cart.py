from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
    
        browser = p.chromium.launch(headless=False, slow_mo=500)

        #Navigate to website
        page = browser.new_page()
        page.goto('https://www.saucedemo.com')

        #Login
        page.fill('input[name="user-name"]', 'standard_user')
        page.fill('input[name="password"]', 'secret_sauce')
        page.locator('#login-button').click()
        print("Login successful!")

        #Add items to cart
        page.locator('#add-to-cart-sauce-labs-bike-light').click()
        print("Product 1 added to cart successfully!")
        page.locator('#add-to-cart-sauce-labs-onesie').click()
        print("Product 2 added to cart successful!")

        #View cart items
        page.locator('.shopping_cart_link').click()
        print("Cart has been opened!")

        browser.close()

if __name__ == "__main__":
    run()