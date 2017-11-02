#!/usr/bin/python3

import argparse

# creating a parser object passing in parameter called description
parser = argparse.ArgumentParser(description="This is our description")
# adding a required cli arg of -i with a help description
parser.add_argument('-i', type=str, help="This is the help text to describe the parameter", required=True)
# adding optional cli arg of -o
parser.add_argument('-o', type=str, help="This is optional", required=False)

#  cmdargs ends up being a dictionary/hash
cmdargs = parser.parse_args()

#  access the parameter based on the flag "i"
ivar = cmdargs.i
print(ivar)
