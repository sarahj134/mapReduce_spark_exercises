# Print cid and total for each order

import sys  

for line in sys.stdin: 
	line = line.strip() 
	order = line.split(",") 
	cid = order[0] 
	total = order[1] 
	print(f'{cid}\t{total}')