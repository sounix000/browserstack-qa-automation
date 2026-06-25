import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.3)

def main():
    # Load Environment Variables
    load_dotenv()
    AMAZON_EMAIL = os.environ.get("AMAZON_EMAIL")
    AMAZON_PASSWORD = os.environ.get("AMAZON_PASSWORD")
    AMZ_URL = "https://amazon.in/"

    if not AMAZON_EMAIL or not AMAZON_PASSWORD:
        raise ValueError("Missing AMAZON_EMAIL or AMAZON_PASSWORD in environment configurations.")

    print("Launching local Chrome browser...")
    browser = webdriver.Chrome()
    browser.maximize_window()

    try:
        browser.get(AMZ_URL)
        time.sleep(2)

        print("Navigating to Sign-In Page...")
        sign_in_button = browser.find_element(By.ID, "nav-link-accountList")
        sign_in_button.click()
        time.sleep(2)

        print("Entering Username...")
        username_textbox = browser.find_element(By.ID, "ap_email")
        slow_typing(username_textbox, AMAZON_EMAIL)
        time.sleep(2)

        continue_button = browser.find_element(By.ID, "continue")
        continue_button.submit()
        time.sleep(2)

        print("Entering Password...")
        password_textbox = browser.find_element(By.ID, "ap_password")
        slow_typing(password_textbox, AMAZON_PASSWORD)
        time.sleep(2)

        sign_in_submit = browser.find_element(By.ID, "auth-signin-button-announce")
        sign_in_submit.submit()
        time.sleep(5)
        
        print("Local Automation sequence finished.")

    finally:
        browser.quit()

if __name__ == "__main__":
    main()
