import os
import webbrowser
import pathlib
from datetime import datetime

time = str(datetime.today().strftime('%Y-%m-%d'))

# read counter
path = pathlib.Path(__file__).parent / "counter.txt"
f = open(path, 'r+')
data = int(f.read())
# update counter
newCounter = str(data + 1)
# write new counter
f.seek(0)
f.write(newCounter)
f.truncate()
f.close()

command = "pytest --alluredir=ReportAllure/"+ time + "_" + newCounter + " " + "testing"
os.system(command)
os.system("allure serve "+"ReportAllure/" + time + "_" + newCounter)