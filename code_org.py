from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def code_org(name, bir):
    # Initialize WebDriver with explicit wait setup
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)  # 10-second timeout for all waits
    
    load_dotenv()
    
    # Environment variable retrieval
    account = os.getenv('CODE_ORG_ACCOUNT')
    class_name = os.getenv('CODE_ORG_CLASS_NAME')
    password = os.getenv('CODE_ORG_PASSWORD')
    
    if not all([account, class_name, password]):
        print('Error: Missing environment variables', 
              f'Account: {account}', 
              f'Class Name: {class_name}', 
              f'Password: {"*" * len(password) if password else "None"}')
        return

    # Navigate to website
    driver.get('https://www.code.org/')
    driver.maximize_window()

    # Wait and close initial popup
    try:
        close_buttons = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//span[@aria-hidden='true' and text()='×']"))
        )
        if close_buttons:
            close_buttons[0].click()
    except Exception as e:
        print("No close button found or error closing:", str(e))

    # Sign in process
    signin_button = wait.until(
        EC.element_to_be_clickable((By.ID, 'signin_button'))
    )
    signin_button.click()

    # Login
    login_email = wait.until(
        EC.presence_of_element_located((By.ID, 'user_login'))
    )
    login_email.send_keys(account)

    login_password = driver.find_element(By.ID, 'user_password')
    login_password.send_keys(password)

    signin_submit = wait.until(
        EC.element_to_be_clickable((By.ID, 'signin-button'))
    )
    signin_submit.click()

    # Navigate to class
    link = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, class_name))
    )
    link.click()

    # Navigate to Manage Students
    student_link = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Manage Students"))
    )
    student_link.click()

    # Prepare student name
    no_years_bir = int(bir) % 10000
    name = str(name) + str(no_years_bir)

    # Input student name
    student_name = wait.until(
        EC.presence_of_element_located((By.ID, 'uitest-display-name'))
    )
    student_name.send_keys(name)

    # Click Add button
    add_button_xpath = "//button[contains(@class, 'fE6oW8WUIydrR0vkYdyC') and .//span[text()='Add']]"
    add_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, add_button_xpath))
    )
    add_button.click()

    # Wait for student name to appear in the list
    wait.until(
        EC.presence_of_element_located((By.XPATH, f"//span[text()='{name}']"))
    )

    # Find and interact with new student
    tag_name = driver.find_element(By.XPATH, f"//span[text()='{name}']")
    parent_element = tag_name.find_element(By.XPATH, "./../../../..")
    
    # Open password section
    tag_names_brother = parent_element.find_element(By.XPATH, './td[5]/div/div/div/span/button')
    tag_names_brother.click()

    # Retrieve password
    password_address = parent_element.find_element(By.XPATH, './td[5]/div/div/div/div/p')
    password_text = password_address.text
    print(password_text)
    
    # Optional: Close browser

# Usage example
# code_org("StudentName", "BirthYear")