# https://www.w3schools.com/python/python_regex.asp

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

y = re.sub("\s", "9", txt, 2)
print(y)
