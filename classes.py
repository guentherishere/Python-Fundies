#!/usr/bin/python

class me:
    # initialization routine
    def __init__(self, foo):
        self.myvar = foo

    def getval(self):
            return self.myvar

# this is an instance of the "me" class
my = me("this")
# my instantiation/assignment allows access to getval method
x = my.getval()
print(x)