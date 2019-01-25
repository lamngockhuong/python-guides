# https://www.w3schools.com/python/python_try_except.asp


try:
    f = open("demofile.txt", "w")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    if 'f' in locals():
        f.close()
