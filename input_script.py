import sys
import subprocess
import globals
def input_script(): 
    arguments = sys.argv
    globals.name = arguments[1]
    # print(globals.name)
    globals.bir = arguments[2]
    # print(globals.bir)
    globals.level = arguments[3]
