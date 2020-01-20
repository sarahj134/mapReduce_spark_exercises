#!/usr/bin/python3

import sys

for customer_total in sys.stdin: 
	customer_total = customer_total.split('\t',1)
# Use the total amount as a key to then get the distinct amounts from reduce
	total_amount = customer_total[1]
	print("{total_amount}\t{count}".format(total_amount = total_amount, count = 1))