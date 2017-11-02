#!/usr/bin/python3

try:
    # the "w" indicates write the file
    fhandle = open("myfile", "w")
    fhandle.write("This is some data to dump into the file")
    print("Wrote some data to the file")
# catches the error as the variable "e" which allows you to do something with if if you need to
except IOError as e:
    print("Exception caught: Unable to write to myfile ", e)
except Exception as e:
    print("Another error occurred ", e)
else:
    print("File written to successfully")
    fhandle.close()
