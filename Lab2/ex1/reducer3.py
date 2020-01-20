#!/usr/bin/python3

import sys
id_amount = None
current_id_amount = None
current_count = 0

for amount_id in sys.stdin: 
	amount_id = amount_id.strip()
	
	id_amount,count = amount_id.split('/t',1)
	
	try:
		count = int(count)
	except ValueError:
		continue

	if id_amount = current_id_amount:
		current_count += count
		if current_id: 
			print("{current_id_amount}\t{current_count}".format(
    		current_id_amount=current_id_amount, 
            current_count=current_count))

if id_amount == current_id_amount:
	print("{current_id_amount}\t{current_count}".format(
    current_id_amount=current_id_amount, 
    current_count=current_count))
