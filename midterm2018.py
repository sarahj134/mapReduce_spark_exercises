

import sys  

customer = None 
current_customer = None 
current_max = 0  

for line in sys.stdin:     
    line = line.strip()     
    element = line.split('\t')     
    customer = element[0]     
    total = int(element[1])      
    if current_customer == customer:    
        if total > current_max:              
            current_max += total               
    else:         
        if current_customer:             
            print(f'{current_customer}\t{current_max}}')                       
        current_customer = customer         
        current_max = int(total)   
print(f'{customer}\t{current_max}')