from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def wait_for_element(driver, by, value, timeout=10):
    """Waits for an element to be present and returns it."""
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))


def click_element(driver, by, value):
    """Waits for an element and clicks it."""
    try:
        element = wait_for_element(driver, by, value)
        element.click()
        
    except (NoSuchElementException, TimeoutException) as e:
        print(f"❌ Could not click element {value}: {e}")


def fill_input(driver, by, value, text):
    """Fills an input field."""
    try:
        field = wait_for_element(driver, by, value)
        field.send_keys(text)
        print(f"✅ Filled {value} with {text}")
    except (NoSuchElementException, TimeoutException) as e:
        print(f"❌ Could not fill input {value}: {e}")


def accept_cookie_consent(driver):
    """Handles the cookie consent popup."""
    try:
        consent_button = wait_for_element(driver, By.XPATH, "//button[contains(@class, 'fc-cta-consent')]", timeout=5)
        consent_button.click()
        print("✅ Clicked on 'Consent' button successfully!")
    except TimeoutException:
        print("✅ No consent modal detected.")


# Main Execution
with webdriver.Chrome() as driver:
    driver.get("http://automationexercise.com")

    # Handle cookies
    accept_cookie_consent(driver)

    # Verify homepage visibility
    try:
        logo = wait_for_element(driver, By.CSS_SELECTOR, "div.logo.pull-left")
        assert logo.is_displayed(), "❌ Home page is not visible!"
        print("✅ Home page is visible!")
    except Exception as e:
        print(f"❌ Test failed: {e}")

    # Click 'Signup / Login' button
    click_element(driver, By.PARTIAL_LINK_TEXT, "Signup / Login")

    # Verify 'New User Signup!' form is visible
    try:
        sign_up_form = wait_for_element(driver, By.CLASS_NAME, "signup-form")
        assert sign_up_form.is_displayed(), "❌ Signup form is not visible!"
        print("✅ Signup form is visible!")
    except Exception as e:
        print(f"❌ Could not verify signup form: {e}")

    # Fill signup form
    fill_input(sign_up_form, By.NAME, "name", "Taekeiro")
    fill_input(sign_up_form, By.NAME, "email", "goters91@gmail.com")

    # Click 'Signup' button
    click_element(sign_up_form, By.TAG_NAME, "button")

    # Verify 'ENTER ACCOUNT INFORMATION' page appears
    try:
        wait_for_element(driver, By.CLASS_NAME, "login-form")
        print("✅ Login form is visible!")
    except TimeoutException:
        print("❌ Login form is not visible!")

    # Fill account information
    click_element(driver, By.XPATH, "//label[@for='id_gender1']")
    fill_input(driver, By.ID, "password", "1234!!!Tai")
    fill_input(driver, By.ID, "days", "26")
    fill_input(driver, By.ID, "months", "August")
    fill_input(driver, By.ID, "years", "1991")

    # Select checkboxes
    click_element(driver, By.ID, "newsletter")
    click_element(driver, By.ID, "optin")

    # Fill address details
    details = {
        "first_name": "FirstName",
        "last_name": "LastName",
        "company": "CompanyName",
        "address1": "Address Str. 24",
        "address2": "Address Str. 16",
        "country": "Canada",
        "state": "Ontario",
        "city": "Toronto",
        "zipcode": "03179",
        "mobile_number": "380983175096",
    }
    for field, value in details.items():
        fill_input(driver, By.ID, field, value)

    # Submit account creation form
    click_element(driver, By.TAG_NAME, "button")

    # Verify account creation
    try:
        account_created = wait_for_element(driver, By.TAG_NAME, "h2")
        assert "ACCOUNT CREATED" in account_created.text, "❌ Account creation failed!"
        print("✅ Account created successfully!")
    except Exception as e:
        print(f"❌ Could not verify account creation: {e}")

    # Click 'Continue' button
    click_element(driver, By.XPATH, "//a[contains(text(), 'Continue')]")

    # Verify user is logged in
    try:
        logged_in_message = wait_for_element(driver, By.XPATH, "//a[contains(text(), 'Logged in as')]")
        assert logged_in_message.is_displayed(), "❌ 'Logged in as username' message not visible!"
        print("✅ Logged in successfully!")
    except Exception as e:
        print(f"❌ Could not verify login: {e}")

    # Delete account
    click_element(driver, By.XPATH, "//a[contains(text(), 'Delete Account')]")

    # Verify account deletion
    try:
        account_deleted_message = wait_for_element(driver, By.TAG_NAME, "h2")
        assert "ACCOUNT DELETED" in account_deleted_message.text, "❌ Account deletion failed!"
        print("✅ Account deleted successfully!")
    except Exception as e:
        print(f"❌ Could not verify account deletion: {e}")

    # Click 'Continue' button
    click_element(driver, By.XPATH, "//a[contains(text(), 'Continue')]")
