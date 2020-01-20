#!/usr/bin/python3

import sys
customer_id = None
current_id = None
current_amount = 0
count = 0


for order in sys.stdin:
    order = order.strip()
    order = order.split('\t', 1)
# Get the customer ID and the order amount fed in by the mapper
    customer_id = order[0]
    order_amount = order[1]
# Get the value of the order amount from the string
    try: 
    	order_amount = int(order_amount)
    except ValueError:
    	continue

# If the customer is the same as before
# Add this order's amount to their expenses
    if customer_id == current_id:
        current_amount += order_amount

# Otherwise, if we are out of the first loop
# Print the customer ID and their expenses
    else:
        if current_id:
            print("{current_id}\t{current_amount}".format(current_id=current_id, current_amount=current_amount))
# Then initialise the current ID and current amount 
# With this client's references
        current_id = customer_id
        current_amount = order_amount

# Do not forget to print the last line!
if customer_id == current_id:
	print("{current_id}\t{current_amount}".format(current_id=current_id, current_amount=current_amount))
