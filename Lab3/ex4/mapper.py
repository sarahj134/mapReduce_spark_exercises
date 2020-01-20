#!/usr/bin/python3
import sys
import numpy as np
index = 0

for element in sys.stdin:
	element = element.strip()
	element = element.split("\t")
	index += 1
	print("{index}\t{element}".format(index=index, element=element[1]))
	
