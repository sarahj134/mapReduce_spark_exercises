#!/usr/bin/python

import sys

current_url = None
current_time = 0
current_count = 0
url = None

for url in sys.stdin: 
	url = url.strip()
	url_time = url.split('\t')
	url = url_time[0] # get the url
	time = url_time[1] # get the time
	try:
		time = float(time) # make the time into a number 
	except ValueError: 
		continue # otherwise ignore it

# If the current url and the url are the same, add the time and increment the count by 1
	if current_url == url:
		current_time += time
		current_count += 1
# Otherwise, if you are out of the first loop, print the first average and then initialise the current url with your new url
	else:
		if current_url: # if current_url is not None, e.g. if I am out of the first loop
			print("{current_url}\t{avg_time}".format(current_url=current_url, avg_time=(current_time/current_count)))
		current_url = url
		current_time = time
		current_count = 1

# This is the output of the last line: careful that the indentation is far LHS	
if current_url == url:
	print("{current_url}\t{avg_time}".format(current_url=current_url,avg_time=current_time/current_count))