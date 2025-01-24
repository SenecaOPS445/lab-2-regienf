#!/usr/bin/env python3

import sys

name = sys.argv[1]          # name argument
age = int(sys.argv[2])     # age argument
result = 'Hi ' + name + ', you are ' + str(age) + ' years old.'

print(result)