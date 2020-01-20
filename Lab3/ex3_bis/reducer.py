#!/usr/bin/python3
import sys
import numpy as np
n_points, dimension = (500, 5)
for reducer_trigger in sys.stdin:
	reducer = reducer_trigger.strip()
	reducer, count = reducer.split('\t', 1)
	points = (np.random.rand(n_points*dimension)*5).reshape((n_points, dimension)) # creating a matrix of n_points lines and dimension columns
	for point_index in np.arange(n_points):
		point = points[point_index,:]
		print("{point_index}\t{point}".format(point_index=point_index, point=point))
# to prevent similar point generation from one reducer to another, use the reducer key in the range argument of np.random.rand() instead of 5
