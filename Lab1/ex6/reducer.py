#!/usr/bin/python

import sys

current_element = None
current_filename = None
count = 0
element = None
filename = None

for element in sys.stdin:
	element = element.strip()
# Get the element and its filename, which are fed in by the mapper
	element, filename = element.split('\t', 1)
# If the element is the same as previously, check if it comes from a different file
	if element == current_element:
		if filename != current_filename:
			count += 1
# If it is the first time it comes from a different file, print it
			if count ==1:
				print("{element}".format(element=element))
# If the element changed, or if it is None (first loop)
# Initialise the value of count, current_element and current_file
	else: 
		current_element = element
		current_filename = filename
		count = 0




