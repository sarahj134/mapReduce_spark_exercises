#!/usr/bin/python3

import sys

for customer_order in st.din:
	customer_order = customer_order.strip()
	customer_order = customer_order.split(",")
	
	order_id = customer_order[0]
	order_amount = customer_order[1]
	print("{order_id}\t{order_amount}".format(
		order_id=order_id, 
		order_amount=order_amount))
