from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_banner = (By.XPATH, "//div[@class='user-name-div']")
        self.logout_button = (By.XPATH, "//div[contains(text(), 'Log out')]")

    def is_user_logged_in(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_banner)
        )
        return self.is_displayed(self.username_banner)

    def logout(self):

        self.click(self.username_banner)
        self.click(self.logout_button)


