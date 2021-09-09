#!/usr/bin/python3
for alpha in range(26):
    if alpha != 4 and alpha != 16:
       print("{:s}".format(chr(ord('a') + alpha), end="")) 
