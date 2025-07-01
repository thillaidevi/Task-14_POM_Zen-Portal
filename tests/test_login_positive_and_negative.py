import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Positive Test
def test_successful_login(setup_driver):
    driver = setup_driver
    login = LoginPage(driver)
    login.login("k.thillaidevi@gmail.com", "Thillai@235295") #Submitting valid fields
    print("Waiting for dashboard to load...")

    WebDriverWait(driver, 15).until(lambda d: d.current_url == "https://v2.zenclass.in/dashboard")
    print("Login confirmed on dashboard!")
    dashboard = DashboardPage(driver)

    #  Close the launch popup if it appears (inherited from BasePage)
    dashboard.close_launch_popup()

    assert dashboard.is_user_logged_in(), "Dashboard not fully loaded"

    # Perform logout, once logged in the dashboard
    dashboard.logout()
    WebDriverWait(driver, 10).until(lambda d: "login" in d.current_url.lower())

    assert "login" in driver.current_url.lower()
    # Validation done
    print("Validated username, password fields with submit button functionality for the valid credentials")
    print(" Successfully logged out and returned to login page.")

# Negative Test
def test_invalid_login(setup_driver):
    driver = setup_driver
    login = LoginPage(driver)
    login.login("invalid@example.com", "wrongpass") # Submitting invalid fields

    sign_button=driver.find_element(By.XPATH, "//button[@class='primary-btn sign-in-pad']")
    sign_button.click()
    print("Current URL after invalid login:", driver.current_url)

    expected_url = "https://v2.zenclass.in/login"
    actual_url = driver.current_url
    # Validation done
    assert actual_url == expected_url, f"Expected to stay on login page, but landed on: {actual_url}"

    print("Validated username, password fields with submit button functionality for the invalid credentials")

# Negative Test
def test_login_with_empty_fields(setup_driver):
    driver = setup_driver
    login = LoginPage(driver)
    login.login("", "")  # Submitting empty fields
    sign_button = driver.find_element(By.XPATH, "//button[@class='primary-btn sign-in-pad']")
    sign_button.click()
    error_text = login.get_login_error_message()
    assert error_text == "Email and password required!", f"Unexpected error: {error_text}"
    # Validation done
    print("You can not logged in with empty username and password")
