import numpy as np

#### Exercise 1 v1 ####
L = [ [1,2,3,4,5,6,7], [2,3,6,9], [3,7,10] ]
def n_way_ms(L):
	L1 = list()
	my_sorted_list = list()
	for i in np.arange(len(L)):
		L1 = L1+L[i]
	while len(L1) != 0:
		my_sorted_list.append(L1.pop(L1.index(min(L1)))) 
# Always adding the minimal element of all lists to my list
	return my_sorted_list
print(n_way_ms(L))

#### Exercise 1 v2  ####

def sorted_list(L):
	mydict = {}
	mysorted_list=[]
	for l in L:
		for elem in l:
			if elem not in mydict:
				mydict[elem]=1
			else:
				mydict[elem]+=1
	for k in mydict.keys():
		for i in range(mydict[k]): # for each number (key), append the key the number of times it is present
			mysorted_list.append(k)

	return mysorted_list
print(sorted_list(L))





