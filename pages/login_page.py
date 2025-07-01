from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.email_input = (By.XPATH, "//input[@placeholder='Enter your mail']")
        self.password_input = (By.XPATH, "//input[@placeholder='Enter your password ']")
        self.signin_button = (By.XPATH, "//button[@class='primary-btn sign-in-pad']")
        self.error_locator = (By.XPATH, "//p[text()='Email and password required!']")

    def login(self, email, password):
        print("Entering email...")
        self.enter_text(self.email_input, email)
        print("Entering password...")
        self.enter_text(self.password_input, password)
        print("Waiting for Sign In button to become clickable...")
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.signin_button)
        )
        self.driver.execute_script("arguments[0].click();", button)
        print("Clicked Sign In button.")

    def get_login_error_message(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_locator)
        )
        return element.text