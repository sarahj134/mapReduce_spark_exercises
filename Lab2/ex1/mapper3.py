#!/usr/bin/python3

import sys

for order_amount in sys.stdin: 
	customer_id, total_amount = order_amount.split('/t',1)
	print("{total_amount}\t{customer_id}".format(
		total_amount = id_amount, 
		count = 1))