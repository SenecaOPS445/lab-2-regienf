#!/usr/bin/env python3
# Author: Regie Francisco
# Author ID: 142631233

import sys

count = int(sys.argv[1])    #convert to int

while count > 0:
    print(str(count))       #print
    count = count - 1       #decrease by 1

print('blast off!')