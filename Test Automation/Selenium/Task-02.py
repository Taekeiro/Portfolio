import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Fixture to initialize and quit the WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


# List of usernames for parameterized testing
usernames = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
]


@pytest.mark.parametrize("username", usernames)
def test_login(driver, username):
    """Test login with multiple usernames."""
    password = "secret_sauce"

    # Locate login elements
    username_input = driver.find_element(By.NAME, "user-name")
    password_input = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.NAME, "login-button")

    # Perform login
    username_input.send_keys(username)

    password_input.send_keys(password)

    submit_button.click()

    # Handle assertions
    if username == "locked_out_user":
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "locked out" in error_message.lower(), f"Locked-out user '{username}' should not be able to login!"
    else:
        assert "inventory" in driver.current_url, f"Login failed for user: {username}"
