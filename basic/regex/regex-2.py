# https://www.w3schools.com/python/python_regex.asp

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

y = re.findall("Portugal", txt)
print(y)

