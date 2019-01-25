# https://www.w3schools.com/python/python_file_handling.asp

import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
