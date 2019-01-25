# https://www.w3schools.com/python/python_dictionaries.asp

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

x = thisdict["model"]
print(x)

y = thisdict.get("model")
print(y)

# Change values
thisdict["year"] = 2019
print(thisdict)

# Return values of a dictionary
for x in thisdict:
    print(thisdict[x])

# Return values of a dictionary
for x in thisdict.values():
    print(x)

# Loop through both keys and values
for x, y in thisdict.items():
    print(x, y)

# Check if key exists
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# return dict length
print(len(thisdict))

# add items
thisdict["color"] = "red"
print(thisdict)

# remove items
thisdict.pop("model")
print(thisdict)

# remove last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)

# del
# del thisdict["model"]
# print(thisdict)
#
# del thisdict
# print(thisdict)

# clear
thisdict.clear()
print(thisdict)

thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)
