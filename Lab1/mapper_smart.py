#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    line = line.split()
    # increase counters
    counter = 0
    mydict = {}
    for word in line:
        if word not in mydict:
            mydict[word]=1
        else:
            mydict[word]+=1
    for key in mydict.keys():
        print("{key}\t{count}".format(key=key, count=mydict[key]))



