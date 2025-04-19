import globals
import input_script
import code_org
import codespark
import typing_com
import create_driver
globals.initialize()

input_script.input_script()
no_years_bir = int(globals.bir) % 10000
if(no_years_bir // 1000 < 1):
    no_years_bir = str('0') + str(no_years_bir)
name = str(globals.name) + str(no_years_bir)
driver = create_driver.create_driver()
password_text = code_org.code_org(name, driver)
codespark.codespark(name, driver)
typing_com.typing(name, password_text, driver)