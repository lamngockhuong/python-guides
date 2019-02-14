# https://www.w3schools.com/python/python_json.asp

import json

# Convert from Python to JSON

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON
y = json.dumps(x)

# the result is a JSON string:
print(y)
