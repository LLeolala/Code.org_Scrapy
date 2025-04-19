import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv



def typing(name, password_text, driver):
    url = "https://teachers.typing.com/"
    
    driver.get(url)
    wait = WebDriverWait(driver, 10)  # Create WebDriverWait object with 10 second timeout
    load_dotenv()

    class_name = os.getenv('TYPING_CLASS_NAME')
    if (not class_name):
        print('error', 'class_name: ' + str(class_name))
        return
    button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="button"][role="link"].TcButton')))
    button.click()
    #手動登入(第一次登入):
    #input("第一次手動登入完畢後 請輸入任何東西: ")
    #print("登入完畢")
    time.sleep(1)
    driver.get("https://teachers.typing.com/classes")
    div_element = wait.until(EC.presence_of_element_located((By.XPATH, f'//div[text()="{class_name}"]')))
    div_element.click()
    students_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-id='students']")))
    students_tab.click()
    add_students = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Add Students']")))
    add_students.click()
    
    
    add_students_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-controls='student-creation-type-addMultiple']")))
    add_students_button.click()
    
    textarea = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'studentData'))
    )

    # Clear the existing content in the textarea
    textarea.clear()

    # Send text to the textarea
    textarea.send_keys(name)

    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "TcButton") and contains(text(), "Review Students")]')))
    button.click()
    # Example relative XPath based on button text
    time.sleep(2)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='student-creation-type-addMultiple']/div[2]/div/div[2]/button[2]")))
    button.click()
    driver.get("https://teachers.typing.com/classes")
    div_element = wait.until(EC.presence_of_element_located((By.XPATH, f'//div[text()="{class_name}"]')))
    div_element.click()
    students_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-id='students']")))
    students_tab.click()
    element = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[text()="{name}"]')))
    element.click()
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Settings']")))

    # Click the button
    button.click()
    password_field = driver.find_element(By.ID, "password")

    # Clear the existing value in the input field
    password_field.clear()

    # Type a new password into the password field
    password_field.send_keys(password_text)

    button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.TcButton[type='submit'][form='details']"))
    )
    button.click()

    
#<div class="flex items-center gap-1.5"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="inline-block stroke shrink-0 fill-current w-6 h-6 stroke-1-5 stroke-current"><use xlink:href="/teacher/images/icons-compiled.svg#add-circle"></use></svg>Add Students</div>
#<button type="button" class="TcButton relative inline-flex flex-row items-center content-center rounded-md text-left min-h-[34px] py-0 px-2.5 text-sm whitespace-nowrap focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 border bg-gradient-to-b focus-visible:ring-blue-500 text-white hover:text-white from-blue-400 to-blue-500 hover:border-blue-500 hover:from-blue-500 hover:to-blue-600 border-blue-600"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon" class="h-5 w-5 mr-1"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"></path></svg>Add Students</button>