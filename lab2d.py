#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:      #check for correct args
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit()

name = sys.argv[1]    # get name
age = sys.argv[2]     # get age
result = 'Hi ' + name + ', you are ' + str(age) + ' years old.'

print(result)