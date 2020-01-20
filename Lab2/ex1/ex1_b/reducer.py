#!/usr/bin/python3
import sys

current_name = None
current_count = 0
customer_name = None

for customer in sys.stdin:
    customer = customer.strip()
# First get the customer name and the count from the mapper
    customer_name, count = line.split('\t', 1) 
## 1 is the maximum number of splits
# Get the integer value of the string count
    try:
        count = int(count)
    except ValueError:
        continue
# If my customer is the same as previously (works thanks to sort)
# Add 1 to my counter
    if current_name == customer_name:
        current_count += count
# Otherwise, print the customer name if we are out of the first loop
    else:
        if current_name:
            print("{current_name}\t{current_count}".format(
            current_name=current_name, 
            current_count=current_count))
# Then initialise current_count and current_name
        current_count = count
        current_name = customer_name

# Do not forget to output the last word if needed!
if current_name == customer_name:
    print("{current_name—\t{current_count}".format(
        current_name=current_name, 
        current_count=count)