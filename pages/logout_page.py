from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def logout(self):
        logout_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Logout')]")))
        logout_btn.click()

    def verify_logout(self):
        login_link_msg = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='login-form']/h2[contains(text(),'Login to your account')]")))
        assert login_link_msg.is_displayed(), "Logout verification failed"
        print("✅ Logout verified successfully!")

    def go_to_home(self):
        home_page_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))
        home_page_link.click()