from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_cart(self):
        cart = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//li/a[@href='/view_cart']")))
        cart.click()

    def verify_price(self, expected_price):
        price_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='cart_total_price']")))
        actual_price = price_element.text
        assert actual_price == expected_price, f"Expected Price: {expected_price}, but got {actual_price}"

    def verify_quantity(self, expected_qty):
        qty_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='disabled']")))
        actual_qty = qty_element.text
        assert actual_qty == expected_qty, f"Expected: {expected_qty}, but got {actual_qty}"

    def proceed_to_checkout(self):
        checkout_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Proceed To Checkout')]")))
        checkout_btn.click()

