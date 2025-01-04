import time
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import undetected_chromedriver
from webdriver_manager.chrome import ChromeDriverManager
import save_cookie
import load_cookie
import is_file_live


def typing(name, bir):
    
    driver = undetected_chromedriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)  # Create WebDriverWait object with 10 second timeout
    load_dotenv()

    account = os.getenv('TYPING_ACCOUNT')
    class_name = os.getenv('TYPING_CLASS_NAME')
    password = os.getenv('TYPING_PASSWORD')
    if (not account or not class_name or not password):
        print('error', 'name: ' + str(account), 'class_name: ' + str(class_name), 'password: ' + str(password))
        return
    driver.get('https://teachers.typing.com/dashboard')
    driver.maximize_window()
    cookie_loaded = False
    if is_file_live.is_file_live("./cookies.pkl"):
        try:
            load_cookie.load_cookie(".", "cookies.pkl", driver)
            cookie_loaded = True
            # Refresh the page after loading cookies
            driver.refresh()
            
            pass
        except Exception as e:
            print(f"Failed to load cookies: {e}")
            cookie_loaded = False
    if not cookie_loaded:
        driver.get('https://teachers.typing.com/login')
        # login_link = wait.until(
        #         EC.element_to_be_clickable((By.CLASS_NAME, "js-open-modal"))
        # )
        # login_link.click()

        # login_button = wait.until(
        #         EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'btn-a') and contains(text(), 'Log In as an Instructor')]"))
        # )
        # login_button.click()

        button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@role='link' and contains(@class, 'TcButton') and contains(., 'Google')]"))
        )
        button.click()

        email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "identifierId"))
        )
        email_input.send_keys(os.getenv('EMAIL'))

        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'VfPpkd-LgbsSe') and .//span[text()='下一步']]"))
        )
        next_button.click()
        password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((
                By.CSS_SELECTOR, 
                        'input[type="password"].whsOnd.zHQkBf[name="Passwd"]'
                ))
        )
        
        password_field.send_keys(os.getenv('EMAIL_PASSWORD'))
        

        button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button//span[text()='下一步']/parent::button"))
        )
        button.click()
        time.sleep(20)
        
        save_cookie.save_cookie(".", "cookies.pkl", driver)
        

    time.sleep(30)

        # ToDo: Fix load_cookie

        #<input type="password" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="current-password" spellcheck="false" tabindex="0" aria-label="輸入您的密碼" name="Passwd" aria-disabled="false" autocapitalize="off" dir="ltr" data-initial-dir="ltr" data-initial-value="">s