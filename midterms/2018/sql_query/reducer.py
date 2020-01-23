#!/usr/bin/python
import sys
dict_customers = {}
dict_orders = {}

# In order to ensure scalability, flush dict_customers to disk and add a reducer.
for line in sys.stdin:
    line = line.strip()
    records = line.split('\t')
    cust_data = records[1].split(';')
    # when customer:
        # cust_data = [date, name]
    # when order
        # cust_data = [total]
    if len(cust_data) == 2:
        cid = records[0]
        date, name = cust_data
        if '2017' in date:
            dict_customers[cid] = (date, name) # we add customers verifying the where clause
    else:
        cid, total = records
        if cid in dict_orders:
            if total > dict_orders[cid]:
                dict_orders[cid] = total # we keep the max total
        else:
            dict_orders[cid] = total

for cid_c in dict_customers.keys(): # for each customer verifying the where clause
    if cid_c in dict_orders:
        print '{}\t{}'.format(cid_c, dict_orders[cid_c]) # we print the max total of the array of totals of each customer

#from collections import OrderedDict
#d = OrderedDict() 
#d[1] = 120 
#d[2] = 130 
#d[3] = 150 

#for k in d.keys(): 
 #   print(d[k])
 # Combiner useful but not inside the map, with this solution