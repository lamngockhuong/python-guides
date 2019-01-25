# https://www.w3schools.com/python/python_modules.asp

import platform
x = platform.system()
print(x)

# List all the function names (or variable names) in a module
# The dir() function can be used on all modules, also the ones you create yourself
y = dir(platform)
print(y)
