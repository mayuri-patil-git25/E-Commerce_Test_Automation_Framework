from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_address(self, expected_address):
        address_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@id='address_delivery']")))
        actual_address = address_element.text
        assert expected_address in actual_address, "Address Verification Failed"

    def place_order(self):
        pay_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Place Order')]")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", pay_btn)
        pay_btn.click()

    def pay_and_confirm_order(self):
        name_input = self.wait.until(EC.presence_of_element_located((By.NAME, "name_on_card")))
        name_input.send_keys("Rosey Churcho")

        card_num_input = self.wait.until(EC.presence_of_element_located((By.NAME, "card_number")))
        card_num_input.send_keys("123456789")

        cvc_input = self.wait.until(EC.presence_of_element_located((By.NAME, "cvc")))
        cvc_input.send_keys("211")

        expiry_month_input = self.wait.until(EC.presence_of_element_located((By.NAME, "expiry_month")))
        expiry_month_input.send_keys("10")

        expiry_year_input = self.wait.until(EC.presence_of_element_located((By.NAME, "expiry_year")))
        expiry_year_input.send_keys("2027")

        confirm_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Pay and Confirm Order')]")))
        confirm_msg.click()

    def verify_order_confirmation(self):
        confirm_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Congratulations! Your order has been confirmed!')]")))
        assert confirm_msg.is_displayed(), "Order confirmation message not displayed"

    def download_invoice(self):
        invoice_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Download Invoice")))
        invoice_link.click()

        continue_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='pull-right']/a[contains(text(),'Continue')]")))
        continue_link.click()