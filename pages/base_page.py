from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver): #Initializes the driver
        self.driver = driver

    def enter_text(self, locator, text, timeout=10):  # Parameterizing Timeout
        # Enter test method is for username and password fields
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def click(self, locator,timeout=10):
        # Click method is for sign in and logout functionality
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def is_displayed(self, locator,timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).is_displayed() # Visibility_of_element_located to ensure the element is interactable.

        except Exception as e:
            print(f"Element not displayed due to: {e}")
            return False

    def close_launch_popup(self, timeout=5):
        """Closes the promotional popup if it appears after login."""
        try:
            # Adjust this XPath/CSS selector based on actual DOM
            popup_close_button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close') or contains(@aria-label, 'Close')]"))
            )
            self.driver.execute_script("arguments[0].click();", popup_close_button)
        except (TimeoutException, NoSuchElementException):
            # Popup not present — optionally log or silently ignore
            pass


