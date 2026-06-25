import os
import time
from threading import Thread
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

load_dotenv()

BUILD_NAME = "browserstack-build-amazon-sign-in"
AMZ_URL = "https://amazon.in/"

capabilities = [
    {
        "browserName": "chrome",
        "browserVersion": "103.0",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "Parallel Test Chrome Windows",
        "buildName": BUILD_NAME
    },
    {
        "browserName": "firefox",
        "browserVersion": "102.0",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "Parallel Test Firefox Windows",
        "buildName": BUILD_NAME
    }
]

def get_browser_option(browser_name):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
    }
    return switcher.get(browser_name.lower(), ChromeOptions())

def run_session(cap):
    username = os.environ.get("BROWSERSTACK_USERNAME")
    access_key = os.environ.get("BROWSERSTACK_ACCESS_KEY")
    amazon_email = os.environ.get("AMAZON_EMAIL")
    amazon_password = os.environ.get("AMAZON_PASSWORD")

    if not username or not access_key:
        print(f"Skipping session {cap['sessionName']} due to missing BrowserStack Credentials.")
        return

    # Deep copy capability to configure credential hooks dynamically
    cap_session = cap.copy()
    cap_session["userName"] = username
    cap_session["accessKey"] = access_key

    options = get_browser_option(cap_session["browserName"])
    options.set_capability("browserName", cap_session["browserName"].lower())
    options.set_capability("bstack:options", cap_session)

    print(f"Starting remote session: {cap_session['sessionName']}")
    try:
        driver = webdriver.Remote(
            command_executor="https://hub.browserstack.com/wd/hub",
            options=options
        )
    except Exception as e:
        print(f"Failed to connect to BrowserStack Remote Hub: {e}")
        return

    try:
        driver.get(AMZ_URL)
        time.sleep(2)

        sign_in_button = driver.find_element(By.ID, "nav-link-accountList")
        sign_in_button.click()
        time.sleep(2)

        username_textbox = driver.find_element(By.ID, "ap_email")
        username_textbox.send_keys(amazon_email if amazon_email else "placeholder_email")
        time.sleep(2)

        continue_button = driver.find_element(By.ID, "continue")
        continue_button.submit()
        time.sleep(2)

        password_textbox = driver.find_element(By.ID, "ap_password")
        password_textbox.send_keys(amazon_password if amazon_password else "placeholder_password")
        time.sleep(2)

        sign_in_submit = driver.find_element(By.ID, "auth-signin-button-announce")
        sign_in_submit.submit()
        time.sleep(2)

        print(f"Session Finished Successfully: {cap_session['sessionName']}")
    except Exception as e:
        print(f"Error encountered in session {cap_session['sessionName']}: {e}")
    finally:
        driver.quit()

def main():
    threads = []
    for cap in capabilities:
        t = Thread(target=run_session, args=(cap,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
