from selenium.webdriver.common.keys import Keys
import time
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

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    load_dotenv()
    # print(globals.name)
    # print(globals.bir)
    driver.get('https://www.code.org/')

    driver.maximize_window()
    time.sleep(1)
    close_buttons = driver.find_elements(By.XPATH, "//span[@aria-hidden='true' and text()='×']")
    if close_buttons:
        close_button = close_buttons[0]  # Get the first one
    close_button.click()
    time.sleep(2)
    signin_button = driver.find_element(By.ID, 'signin_button')
    signin_button.click()
    time.sleep(2)
    login_email = driver.find_element(By.ID, 'user_login')

    login_email.send_keys(os.getenv('ACCOUNT'))
    login_password = driver.find_element(By.ID, 'user_password')
    login_password.send_keys(os.getenv('PASSWORD'))

    signin_button = driver.find_element(By.ID, 'signin-button')
    signin_button.click()

    time.sleep(1)
    link = driver.find_element(By.PARTIAL_LINK_TEXT, os.getenv('CLASS_NAME'))
    link.click()
# Ad
# close_buttons = driver.find_elements(By.ID, 'ui-close-dialog')
# close_button = close_buttons[0]
# close_button.click()
    time.sleep(1)

    student_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Manage Students")
    student_link.click()
    time.sleep(1)

    
    no_years_bir = int(bir) % 10000
    name = str(name) + str(no_years_bir)
    


    # 輸入學生名稱 # input_name
    student_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'uitest-display-name'))
    )
    student_name.send_keys(name)

    # 點擊添加按鈕
    add_button_xpath = "//button[contains(@class, 'fE6oW8WUIydrR0vkYdyC') and .//span[text()='Add']]"
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, add_button_xpath))
    )
    add_button.click()
    # 等待學生名稱出現在列表中

    time.sleep(1)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//span[text()='{name}']"))
    )
    tag_name = driver.find_element(By.XPATH, f"//span[text()='{name}']")
    # 找到父元素
    parent_element = tag_name.find_element(By.XPATH, "./../../../..")
    tag_names_brother = parent_element.find_element(By.XPATH, './td[5]/div/div/div/span/button')
    tag_names_brother.click()

    # get the password element

    password_address = parent_element.find_element(By.XPATH, './td[5]/div/div/div/div/p')
    password_text = password_address.text
    print(password_text)