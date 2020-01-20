#!/usr/bin/python3
import sys
current_element = None

for element in sys.stdin:
	element = element.strip()
	index, element = element.split("\t", 1)
	print(element)
