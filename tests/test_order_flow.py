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
        login.login("rose1004@gmail.com","RoseChrucho")
        login.verify_login_success()

        product.go_to_products_page()
        product.search_product()
        product.select_product_and_add_to_cart()
        product.continue_shopping()

        cart.go_to_cart()
        cart.verify_price("Rs. 2000")
        cart.verify_quantity("2")
        cart.proceed_to_checkout()

        expected_address = "Mrs. Rosey Chrucho\n969 Cox Rd, Gastonia, NC 28054-3455, USA\nGastonia North Carolina 28054-3455\nUnited States\n121 55 4567"
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