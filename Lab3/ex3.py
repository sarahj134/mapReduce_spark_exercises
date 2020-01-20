#!/usr/bin/python3
# cd Dev
# spark-2.4.4-bin-hadoop2.7/bin/pyspark

### Exercise 2 ###
pets = sc.parallelize([("cat",1), ("dog", 1), ("cat", 2), ("dog", 3)])
pets.collect()
pets.take(2)

pet_sum = pets.reduceByKey(lambda x, y : x +y)
pet_count = pets.map(lambda x : (x[0], 1))
pet_count = pet_count.reduceByKey(lambda x, y : x +y)

#pet_sum_count = pet_sum.cogroup(pet_count).map(lambda x :(x[0], (list(x[1][0]), list(x[1][1])))).collect()
pet_average = pet_sum.join(pet_count).map(lambda x :(x[0], x[1][0]/x[1][1])).collect()

### Exercise 3 ###

## Reducer job ##
#!/usr/bin/python3
# touch ~/Database_management/Lab3/reducer_trigger.txt 
cat reducer_trigger.txt | python mapper.py | sort -k1,1 -s | python reducer.py > F1.txt # the last argument stores the output as a text file

## Mapper
import sys
for reducer_trigger in sys.stdin:
	trigger = reducer_trigger.strip()
	trigger = reducer.split("\t")
	print("{trigger}\t{count}".format(trigger=trigger, count=1))

# Reducer 
import sys
import numpy as np
n_points, dimension = (500, 5)
for reducer_trigger in sys.stdin:
	reducer = reducer_trigger.strip()
	reducer, count = reducer.split('\t', 1)
	points = (np.random.rand(n_points*dimension)*5).reshape((n_points, dimension)) # creating a matrix of n_points lines and dimension columns
	for point_index in np.arange(n_points):
		point = points[point_index,:]
		print("{point_index}\t{point}".format(point_index=point_index, point=point)


# to prevent similar point generation from one reducer to another, use the reducer key in the range argument of np.random.rand() instead of 5








