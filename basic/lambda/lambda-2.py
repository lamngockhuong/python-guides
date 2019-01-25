# https://www.w3schools.com/python/python_lambda.asp


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))
