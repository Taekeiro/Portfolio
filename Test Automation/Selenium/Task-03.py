from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def accept_cookie_consent(driver):
    try:
        time.sleep(3)
        consent_modal = driver.find_element(By.CLASS_NAME, "fc-dialog-container")
        if consent_modal.is_displayed():
            print("✅ Consent modal detected!")
            consent_button = consent_modal.find_element(By.XPATH, "//button[contains(@class, 'fc-cta-consent')]")
            consent_button.click()
            print("✅ Clicked on 'Consent' button successfully!")
            time.sleep(2)
        else:
            print("✅ No consent modal detected.")
    except Exception as e:
        print(f"❌ Could not handle cookie consent: {e}")


def launch_browser():
    driver = webdriver.Chrome()
    return driver


def navigate_to_url(driver, url):
    print(f"🌍 Navigating to {url}")
    driver.get(url)
    time.sleep(3)


def verify_home_page(driver):
    try:
        logo = driver.find_element(By.CSS_SELECTOR, "div.logo.pull-left")
        assert logo.is_displayed()
        print("✅ Home page is visible successfully!")
    except Exception as e:
        print(f"❌ Test failed: {e}")


def click_signup_login(driver):
    try:
        signup_login_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Signup / Login")
        signup_login_button.click()
        print("✅ Clicked on 'Signup / Login' button successfully!")
        time.sleep(3)
    except Exception as e:
        print(f"❌ Could not click on 'Signup / Login': {e}")


def fill_signup_form(driver, name, email):
    try:
        sign_up_form = driver.find_element(By.CLASS_NAME, "signup-form")
        assert sign_up_form.is_displayed(), "❌ Signup form not visible!"
        print("✅ Signup form detected!")
        name_field = sign_up_form.find_element(By.NAME, "name")
        email_field = sign_up_form.find_element(By.NAME, "email")
        submit_button = sign_up_form.find_element(By.TAG_NAME, "button")
        name_field.send_keys(name)
        email_field.send_keys(email)
        print("✅ Entered signup details!")
        submit_button.click()
        print("✅ Signup form submitted successfully!")
        time.sleep(3)
    except Exception as e:
        print(f"❌ Could not complete signup: {e}")


def fill_account_details(driver, password, dob):
    try:
        sign_up_form = driver.find_element(By.CLASS_NAME, "login-form")
        gender_label = sign_up_form.find_element(By.XPATH, "//label[@for='id_gender1']")
        gender_label.click()
        print("✅ Clicked on 'Mr.' successfully!")
        time.sleep(2)
        password_input = sign_up_form.find_element(By.ID, "password")
        password_input.send_keys(password)
        print("✅ Entered password!")
        day_dropdown = sign_up_form.find_element(By.ID, "days")
        month_dropdown = sign_up_form.find_element(By.ID, "months")
        year_dropdown = sign_up_form.find_element(By.ID, "years")
        day_dropdown.send_keys(dob[0])
        month_dropdown.send_keys(dob[1])
        year_dropdown.send_keys(dob[2])
        print("✅ Entered birthdate!")
        time.sleep(2)

        newsletter_checkbox = driver.find_element(By.ID, "newsletter")
        newsletter_checkbox.click()
        time.sleep(2)
        assert newsletter_checkbox.is_selected(), "❌ Newsletter checkbox not selected!"
        print("✅ 'Sign up for our newsletter!' checkbox selected successfully!")

        offers_checkbox = driver.find_element(By.ID, "optin")
        offers_checkbox.click()
        time.sleep(2)
        assert offers_checkbox.is_selected(), "❌ Offers checkbox not selected!"
        print("✅ 'Receive special offers from our partners!' checkbox selected successfully!")

        first_name_input = sign_up_form.find_element(By.ID, "first_name")
        first_name_input.send_keys("FirstName")
        print("✅ First name added!")

        last_name_input = sign_up_form.find_element(By.ID, "last_name")
        last_name_input.send_keys("LastName")
        print("✅ Last name added!")

        company_input = sign_up_form.find_element(By.ID, "company")
        company_input.send_keys("CompanyName")
        print("✅ Company name added!")

        address1_input = sign_up_form.find_element(By.ID, "address1")
        address1_input.send_keys("Address Str. 24 ")
        print("✅ Address 1 added!")

        address2_input = sign_up_form.find_element(By.ID, "address2")
        address2_input.send_keys("Address Str. 16 ")
        print("✅ Address 2 added!")

        country_dropdown = sign_up_form.find_element(By.ID, "country")
        country_dropdown.send_keys("Canada")
        time.sleep(2)
        print("✅ Selected Canada!")

        state_input = sign_up_form.find_element(By.ID, "state")
        state_input.send_keys("Canada 2")
        print("✅ Added state!")

        city_input = sign_up_form.find_element(By.ID, "city")
        city_input.send_keys("Toronto")
        print("✅ Added city!")

        zipcode_input = sign_up_form.find_element(By.ID, "zipcode")
        zipcode_input.send_keys("03179")
        print("✅ Added zipcode!")

        mobile_input = sign_up_form.find_element(By.ID, "mobile_number")
        mobile_input.send_keys("380983175096")
        print("✅ Added mobile number!")

        create_account_button = sign_up_form.find_element(By.TAG_NAME, "button")
        create_account_button.click()
        print("✅ Clicked on 'Create Account' button successfully!")
        time.sleep(3)

        continue_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue')]")
        continue_button.click()
        print("✅ Clicked on 'Continue' after account creation!")
        time.sleep(3)
    except Exception as e:
        print(f"❌ Could not fill in details or create account: {e}")


def delete_account(driver):
    try:
        delete_account_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Delete Account')]")
        delete_account_button.click()
        print("✅ Clicked 'Delete Account' successfully!")
        time.sleep(3)

        continue_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue')]")
        continue_button.click()
        print("✅ Clicked on 'Continue' after account deletion!")
        time.sleep(3)
    except Exception as e:
        print(f"❌ Could not click 'Delete Account' or 'Continue': {e}")


def main():
    driver = launch_browser()
    navigate_to_url(driver, "http://automationexercise.com")
    accept_cookie_consent(driver)
    verify_home_page(driver)
    click_signup_login(driver)
    fill_signup_form(driver, "Taekeiro", "goters91@gmail.com")
    fill_account_details(driver, "1234!!!Tai", ["26", "August", "1991"])
    delete_account(driver)
    driver.quit()
    print("✅ Test completed successfully!")


if __name__ == "__main__":
    main()
        
