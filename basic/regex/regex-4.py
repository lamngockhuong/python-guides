# https://www.w3schools.com/python/python_regex.asp

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

y = re.split("\s", txt, 1)
print(y)
