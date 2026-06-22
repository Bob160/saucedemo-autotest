from playwright.sync_api import Page, expect
from conftest import logged_in_page
from pages.view_cart import View_cart

def test_view_cart(logged_in_page, page : Page):

    view_cart = View_cart(logged_in_page)

    view_cart.view_cart()

    page.wait_for_url('**/cart.html')

    assert "cart" in page.url