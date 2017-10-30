#!/usr/bin/python

import os
from subprocess import call

# use the OS interface to get access to sys info
print(os.getcwd())
# print(os.getuid())
print(os.getenv("PATH"))

# using system
os.system("tree")
os.system("calc")

# can use call
inp=input("hit enter")
# call below for nix
call(["ls", "-la"])

