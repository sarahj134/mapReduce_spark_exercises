#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for url in sys.stdin:
	url = url.strip()
	url_time = url.split('/t')
	print("{url}\t{time}".format(url=url_time[0], time=url_time[1]))