#Problem 1.8 Zero Matrix: Write an algorithm such that if an element in an M x N matrix is 0, it's
# enitre row and column are set to 0. 

def zeroMatrix(matrix):
	row = 0
	column = 0
	rowLength, columnLength = matrix.shape
	arr = []
	for row in range(rowLength):
		for column in range(columnLength):
			if (matrix[row, column] == 0):
				arr.append((row, column))

	for i in range(len(arr)):
		rowZero, columnZero = arr[i]
		matrix[rowZero,:] = 0
		matrix[:, columnZero] = 0

	return matrix

##do the testing here, the Big(O) should be O(MN)

import numpy as np
testMatrix = np.mat('1,2,0,4; 3,9,1,6; 0,2,4,5')
zeroMatrix(testMatrix)
print testMatrix
