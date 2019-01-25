# https://www.w3schools.com/python/python_strings.asp

x = "Hello, world!"
print(x[2:5])

y = "  Hello world   "
print(y.strip())  # remove any whitespace from the beginning or the end
print(len(y))  # return the length of a string
print(y.lower())  # return the string in lower case
print(y.upper())  # return the strung in upper case
print(y.replace("H", "J"))  # replace a string with another string
print(x.split(","))  # return list that splits the string into substrings


print(x is not y)
