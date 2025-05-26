from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_signup_login(self):
        signup_login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
        signup_login_link.click()

    def login(self, email, password):
        email_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-qa='login-email']")))
        password_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-qa='login-password']")))
        login_btn = self.driver.find_element(By.XPATH, "//button[@data-qa='login-button']")

        email_input.send_keys(email)
        password_input.send_keys(password)
        login_btn.click()

    def verify_login_success(self):
        logout_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
        assert logout_link.is_displayed(), "Login unsuccessful - Logout link not found."
        print("Login successful!")
