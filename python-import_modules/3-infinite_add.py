#!/usr/bin/python3
import sys
argv = sys.argv[1:]
total = 0
for arg in argv:
    total += int(arg)
print(total)
