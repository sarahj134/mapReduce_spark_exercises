#!/usr/bin/python3

import sys
current_amount = None
total_amount = None
count = 0

for total_amount in sys.stdin: 
	total_amount = total_amount.strip()
	total_amount = total_amount.split('/t',1)

# If my total amount is not the same as previously
# Add 1 to my count (it's a new distinct order)
	if total_amount != current_amount:
		count += 1
# Initialise current amount to total amount, and count to 1
	else:
		current_amount = total_amount

print("There are", count, "distinct customer totals.") 

