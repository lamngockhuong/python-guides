# https://www.w3schools.com/python/python_json.asp

import json

print(json.dumps({"name": "John", "age": 30}, indent=4))
print(json.dumps({"name": "John", "age": 30}, indent=4, separators=(". ", " = ")))
print(json.dumps({"name": "John", "age": 30}, indent=4, sort_keys=True))
