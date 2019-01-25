# https://www.w3schools.com/python/python_file_handling.asp

f = open("demofile.txt", "r")
# print(f.read(5))
# print(f.read())
# print(f.readline())

for x in f:
    print(x)
