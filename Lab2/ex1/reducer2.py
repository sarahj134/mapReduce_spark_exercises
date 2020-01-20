#!/usr/bin/python3

import sys
customer_id = None
current_id = None
current_amount = 0



for order in sys.stdin:
	order = order.strip()
    
    customer_id, order_amount = order.split('\t', 1)
    try: 
    	order_amount = int(order_amount)
    except ValueError:
    	continue

    if customer_id = current_id:
    	current_amount += order_amount
    	if current_id: 
    		print("{current_id}\t{current_amount}".format(
    			current_id=current_id, 
            	current_amount=current_amount))

if customer_id == current_id:
	print("{current_id}\t{current_amount}".format(
		current_id=current_order_id, 
        current_amount=current_amount)


