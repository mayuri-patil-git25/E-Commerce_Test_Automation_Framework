from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_products_page(self):
        go_to_product_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Products')]")))
        go_to_product_section.click()

    def search_product(self):
        product = self.wait.until(EC.visibility_of_element_located((By.ID, "search_product")))
        product.send_keys("Madame top")

        click_search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='submit_search']")))
        click_search_button.click()

    def select_product_and_add_to_cart(self):
        view_product = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'View Product')])[1]")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", view_product)
        view_product.click()

        qty_input = self.wait.until(EC.presence_of_element_located((By.ID, "quantity")))
        qty_input.clear()
        qty_input.send_keys("2")

        add_to_cart = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default cart']")))
        add_to_cart.click()

    def continue_shopping(self):
        continue_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue Shopping')]")))
        continue_btn.click()