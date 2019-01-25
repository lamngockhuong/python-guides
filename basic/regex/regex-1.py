# https://www.w3schools.com/python/python_regex.asp

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

y = re.search("\s", txt)
print(y)
print("The first white-space character is located in position:", y.start())

z = re.search(r"\bS\w+", txt)
print(z.span())
print(z.string)
print(z.group())
