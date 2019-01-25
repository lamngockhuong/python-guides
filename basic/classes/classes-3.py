# https://www.w3schools.com/python/python_classes.asp


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.name = "Kaka"
p1.myfunc()
print(p1)

# delete object
del p1
print(p1)  # name 'p1' is not defined
