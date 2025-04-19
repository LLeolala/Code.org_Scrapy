import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv



def code_org(name, driver):
    # Initialize WebDriver with explicit wait setup
    wait = WebDriverWait(driver, 10)  # 10-second timeout for all waits
    
    load_dotenv()
    
    # Environment variable retrieval
    class_name = os.getenv('CODE_ORG_CLASS_NAME')
    
    if not class_name:
        print('Error: Missing environment variables', 
              f'Class Name: {class_name}')
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
    #手動登入(第一次登入):
    #input("第一次手動登入完畢後 請輸入任何東西: ")
    #print("登入完畢")
    try:
        close_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//i[@data-testid='font-awesome-v6-icon' and contains(@class, 'fa-times')]]"))
        )
        close_button.click()
        print("成功使用XPath點擊關閉按鈕")
        
    except:
            print("使用XPath方法失敗，嘗試其他方法...")

    # Navigate to class
    element = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "test_class"))
    )
    element.click()

    # Navigate to Manage Students
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "l73WWV9XeuD321FND147")))
    element=elements[8]
    element.click()

    

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
    return password_text
    
    # Optional: Close browser

# Usage example
# code_org("StudentName", "BirthYear")