import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_and_verify_product():
    driver = webdriver.Chrome()
    time.sleep(1)  # Allow driver to start

    # Open the website
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    # Locate and interact with the login form
    username_input = driver.find_element(By.NAME, "user-name")
    password_input = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.NAME, "login-button")

    # Perform login
    username_input.send_keys("standard_user")
    time.sleep(1)
    password_input.send_keys("secret_sauce")
    time.sleep(1)
    submit_button.click()
    time.sleep(2)

    # Assert successful login by checking the URL
    assert "inventory" in driver.current_url, "Login failed!"

    # Verify the presence of 'Sauce Labs Backpack' product
    sauce_lab_backpack = driver.find_element(By.ID, "item_4_title_link")
    assert sauce_lab_backpack.is_displayed(), "Sauce Labs Backpack is not visible!"

    # Close browser
    driver.quit()
