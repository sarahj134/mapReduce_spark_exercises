#!/usr/bin/python

import sys

# Read pairs as lines of input from STDIN
for element in sys.stdin:
	element = element.strip()
	filename, element = element.split(':', 1)
	print("{element}\t{filename}".format(element=element, filename=filename))