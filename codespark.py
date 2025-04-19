from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time


def codespark(name, driver):
    
    wait = WebDriverWait(driver, 10)  # Create WebDriverWait object with 10 second timeout
    load_dotenv()

    class_name = os.getenv('CODESPARK_CLASS_NAME')
    if (not class_name):
        print('class_name: ' + str(class_name))


    
    driver.get('https://dashboard.codespark.com/')
    driver.maximize_window()
    #手動登入(第一次登入):
    #input("第一次手動登入完畢後 請輸入任何東西: ")
    #print("登入完畢")
    time.sleep(2)
    
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
    
    
    textarea.send_keys(name)
    
    
    button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='add']"))
    )
    js = "arguments[0].scrollIntoView()"
    driver.execute_script(js, button)
    time.sleep(1)
    button.click()