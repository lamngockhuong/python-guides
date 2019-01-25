# https://www.w3schools.com/python/python_sets.asp

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

print(len(thisset))

thisset.remove("banana")  # If the item to remove does not exist, remove() will raise an error.
thisset.discard("cherry")  # If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)

thisset.pop()
print(thisset)
