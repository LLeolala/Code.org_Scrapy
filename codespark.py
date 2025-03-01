from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

def codespark(name, bir):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)  # Create WebDriverWait object with 10 second timeout
    load_dotenv()

    account = os.getenv('CODESPARK_ACCOUNT')
    class_name = os.getenv('CODESPARK_CLASS_NAME')
    password = os.getenv('CODESPARK_PASSWORD')
    if (not account or not class_name or not password):
        print('error', 'name: ' + str(account), 'class_name: ' + str(class_name), 'password: ' + str(password))
        return

    
    driver.get('https://dashboard.codespark.com/')
    driver.maximize_window()
    # Login to CodeSpark
    signin_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/login']"))
    )
    signin_link.click()
    
    email_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text'][name='login-email']"))
    )
    email_input.clear()
    email_input.send_keys(account)
    
    password_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password'][name='login-password']"))
    )
    password_input.clear()
    password_input.send_keys(password)
    
    submit_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='login-submit' and @type='submit']"))
    )
    submit_button.click()
    
    # Handle final OK button
    OK_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='dashboard-button' and text()='OK']"))
    )
    OK_button.click()
    
    classrooms_link = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/dashboard/classrooms']"))
    )
    classrooms_link.click()
    
    # Wait and click title
    title = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//h2[@class='title title--classroom' and text()='{class_name}']"))
    )
    title.click()
    
    buttons = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), 'edit')]"))
    )
    button = buttons[1]
    button.click()
    

    textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "addStudents"))
    )
    textarea.clear()
    
    no_years_bir = int(bir) % 10000
    if(no_years_bir // 1000 < 1):
        no_years_bir = str('0') + str( no_years_bir)
    name = str(name) + str(no_years_bir)
    textarea.send_keys(name)
    
    
    button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='add']"))
    )
    js = "arguments[0].scrollIntoView()"
    driver.execute_script(js, button)
    time.sleep(1)
    button.click()