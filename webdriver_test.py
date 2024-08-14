from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
load_dotenv(".env")
chromedriver = '/usr/local/bin/chrome-mac-arm64'
driver = webdriver.Chrome()
driver.get('https://www.code.org/')
time.sleep(2)

driver.maximize_window()

close_buttons = driver.find_elements(By.XPATH, "//span[@aria-hidden='true' and text()='×']")
if close_buttons:
    close_button = close_buttons[0]  # Get the first one
close_button.click()
time.sleep(1)

signin_button = driver.find_element(By.ID, 'signin_button')
signin_button.click()
time.sleep(2)

login_email = driver.find_element(By.ID, 'user_login')
login_email.send_keys(os.getenv('ACCOUNT'))
login_password = driver.find_element(By.ID, 'user_password')
login_password.send_keys(os.getenv('PASSWORD'))
time.sleep(2)

signin_button = driver.find_element(By.ID, 'signin-button')
signin_button.click()
time.sleep(2)

link = driver.find_element(By.PARTIAL_LINK_TEXT, os.getenv('CLASS_NAME'))
link.click()
time.sleep(3)
# Ad
# close_buttons = driver.find_elements(By.ID, 'ui-close-dialog')
# close_button = close_buttons[0]
# close_button.click()
# time.sleep(3)

student_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Manage Students")
student_link.click()
time.sleep(3)

with open('profile_name', 'r') as f:
    name = f.readline().strip()
    bir = f.readline().strip()
no_years_bir = int(bir) % 10000
name = str(name) + str(no_years_bir)

# 輸入學生名稱 # input_name
student_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'uitest-display-name'))
)
student_name.send_keys(name)
time.sleep(5)

# 點擊添加按鈕
time.sleep(5)
add_button_xpath = "//button[contains(@class, 'fE6oW8WUIydrR0vkYdyC') and .//span[text()='Add']]"
add_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, add_button_xpath))
)
add_button.click()
# 等待學生名稱出現在列表中

time.sleep(5)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"//span[text()='{name}']"))
)

# 找到學生名稱的span元素
tag_name = driver.find_element(By.XPATH, f"//span[text()='{name}']")

# 找到父元素
tag_name_parent = tag_name.find_element(By.XPATH, "./ancestor::*[3]")  # 假設是第三級祖先元素

# 在父元素中尋找符合特定類別的子元素
target_class = "uitest-show-picture-or-word RgEAWGSURVHXgsym55ZC SfFcj2dNRCSSkdsG0JWm SpnpMKQTi1rIE2H6S2st pUlkLwlwitRrefPiTBSj"
tag_name_parent_child = tag_name_parent.find_element(By.XPATH, f".//*[contains(@class, '{target_class}')]")

# 記錄點擊前的文本
before_click_text = tag_name_parent_child.text

# 點擊元素
tag_name_parent_child.click()
time.sleep(5)
# 與找到的元素互動（例如點擊）
#show_password.click()

# time.sleep(5)

# password = driver.find_elements(By.TAG_NAME, 'p')
# password_text = password[1].text
# time.sleep(3)

# driver.get('https://typing.com/')
# time.sleep(3)