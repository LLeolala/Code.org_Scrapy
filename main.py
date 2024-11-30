import globals
import input_script
import code_org
import codespark

globals.initialize()

input_script.input_script()

code_org.code_org(globals.name, globals.bir)
codespark.codespark(globals.name, globals.bir, globals.level)
