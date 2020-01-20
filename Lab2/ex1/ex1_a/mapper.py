#!/usr/bin/python3

# always remember to add the first line as a comment 
import sys
for customer in sys.stdin:
	customer = customer.strip()
	customer = customer.split(",")
	date = customer[1] # 0 is customer id, 1 is customer date and 2 is customer name
	month = date[3:5] # the month is located in these positions
	if month == "07":
		print("{customername}\t{count}".format(customername=customer[2], count=1))

