#!/usr/bin/env python3
# Author: Regie Francisco
# Author ID: 142631233
# Date Created: 2025/01/23

import sys

if len(sys.argv) == 2:
    count = int(sys.argv[1])    #convert to int
else:
    count = 3

while count > 0:
    print(str(count))       #print
    count = count - 1       #decrease by 1

print('blast off!')