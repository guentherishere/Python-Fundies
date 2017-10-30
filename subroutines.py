#!/usr/bin/python

# TL;DR - subroutines are aka functions

def sub(x,y):
        # out of scope here
        z=x-y
        # just print, no return
        print(z)

# using params
def add(x,y):
        # return value
        return x+y

print(add(15,4))
# not passing params initially
sub(12,2)