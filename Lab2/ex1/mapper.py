#!/usr/bin/python3
import sys
# Always remember to add the first line as a comment 

for customer in sys.stdin:
	customer = customer.strip()
	# Split the customer line in customer ID, order date, and customer name
	customer = customer.split(",")
	# Extract the date, then select the month from the date 
	# By using its position within the string
	date = customer[1] 
	month = date[3:5] 
	# If the order took place in july, print the customer name
	if month == "07":
		print("{customername}\t{count}".format(customername=customer[2], count=1))

