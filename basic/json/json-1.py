# https://www.w3schools.com/python/python_json.asp

import json

# Convert from JSON to Python

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary
print(y["age"])
