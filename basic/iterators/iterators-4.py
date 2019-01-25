# https://www.w3schools.com/python/python_iterators.asp

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myit = iter(myclass)

for x in myit:
    print(x)

# The for loop actually creates an iterator object and executes the next() method for each loop.
