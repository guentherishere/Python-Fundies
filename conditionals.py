#!/usr/bin/python

# input from keyboard is a string, so it has to be converted w. the int() func
x=int(input("give me a number"))

if (x<=11):
    print("too little")
elif (x>1 and x<10):
    print("Just about right")
else:
    print("Too high")

