from selenium import webdriver
from selenium.webdriver.common.by import By

def display_cookies_before_and_after_login():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Open URL
        driver.get("https://www.saucedemo.com/")

        # Display cookies before login
        print("Cookies before login:")
        print(driver.get_cookies())

        # Login
        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        # Enter username and password
        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")

        # Click login button
        login_button.click()

        # Display cookies after login
        print("\nCookies after login:")
        print(driver.get_cookies())

        # Logout
        logout_button = driver.find_element(By.ID, "logout_sidebar_link")
        logout_button.click()

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    display_cookies_before_and_after_login()