import sys
import subprocess
arguments = sys.argv
a=arguments[1]
b=arguments[2]
with open("profile", 'w+') as f:
    f.write(str(a) + '\n')
    f.write(b)
    f.write('\n')
def run_web():
    subprocess.run(["python", "webdriver_test.py"], check=True)

run_web()



