#!/usr/bin/python3

import sys
mydict = {}

for customer in sys.stdin: 
	customer = customer.strip()
	customer = customer.split(",")
	customer_id = customer[0]
	
	if customer_id not in mydict:
		mydict[customer_id] = 1
	else:
		mydict[customer_id] += 1
# Works because there are only unique customer ids in my customer file 
for key in mydict.keys():
	if mydict[key] != 1:
		print("{customer_id}\t{count}".format(customer_id = mydict[key], count=1))
