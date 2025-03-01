import globals
import input_script
import code_org
import codespark
import typing_com

globals.initialize()

input_script.input_script()

password_text = code_org.code_org(globals.name, globals.bir)
codespark.codespark(globals.name, globals.bir)
typing_com.typing(globals.name, globals.bir,password_text)