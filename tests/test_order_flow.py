from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
expected_address = os.getenv("EXPECTED_ADDRESS")

import unittest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.logout_page import LogoutPage

class TestOrderFlow(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://automationexercise.com/")

    def test_complete_order_process(self):
        login = LoginPage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)
        checkout = CheckoutPage(self.driver)
        logout = LogoutPage(self.driver)

        login.click_signup_login()
        login.login(os.getenv("EMAIL"),os.getenv("PASSWORD"))  # Using this to Hide it from public view
        login.verify_login_success()

        product.go_to_products_page()
        product.search_product()
        product.select_product_and_add_to_cart()
        product.continue_shopping()

        cart.go_to_cart()
        cart.verify_price("Rs. 2000")
        cart.verify_quantity("2")
        cart.proceed_to_checkout()

        checkout.verify_address(expected_address)
        checkout.place_order()
        checkout.pay_and_confirm_order()
        checkout.verify_order_confirmation()
        checkout.download_invoice()

        logout.logout()
        logout.verify_logout()
        logout.go_to_home()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()