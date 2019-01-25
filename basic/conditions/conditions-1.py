# https://www.w3schools.com/python/python_conditions.asp

a = 33
b = 200
c = 5

# case *
if b > a:
    print("b is greater than a")

# case **
if b > a: print("b is greater than a")

# case ***
if b > c:
    print("b is greater than c")
elif b == c:
    print("b and c are equal")
else:
    print("c is greater than b")

# case ****
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")

# case *****
if a > b and c > a:
    print("Both conditions are True")

# case ******
if a > b or c > a:
    print("At least one of the conditions is True")
