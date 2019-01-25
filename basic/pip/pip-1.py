# https://www.w3schools.com/python/python_pip.asp

import camelcase

c = camelcase.CamelCase()

txt = "hello world"
x = c.hump(txt)
print(x)

'''
+ Install package
pip install camelcase
+ Uninstall package
pip uninstall camelcase
+ List all packages
pip list
'''
