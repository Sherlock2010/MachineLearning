"""
test for sigmoid function 
"""
from __future__ import division
import time
from numpy import *
import pylab as pl
import random
import math
import sys

"""
1    3    1
0.5  3    1
2    3.5  1
2    2	  1
1.5  2    0
1    1.5  0
0.5  1    1
1    0.5  0
1    1    1
1.5  1    0
"""
alpha = 0.01
maxCycles = 1000000
maxNumber = 5

def loadData(file_path):
	dataMatrix = []
	labelMatrix = []
	X1 = []
	Y1 = []
	X2 = []
	Y2 = []

	f = open(file_path, 'r')

	for line in f.readlines():
		lineArray = line.strip().split()
		dataMatrix.append([1.0, float(lineArray[0]), float(lineArray[1])])
		labelMatrix.append(int(lineArray[2]))

		if(int(lineArray[2])):
			X1.append(float(lineArray[0]))
			Y1.append(float(lineArray[1]))
		else:
			X2.append(float(lineArray[0]))
			Y2.append(float(lineArray[1]))

	return dataMatrix, labelMatrix, X1, Y1, X2, Y2

def sigmoid(intX):
	# print 1.0/(1+exp(-intX))
	return 1.0/(1+exp(-intX))

def function(dataMatrixIn, labelMatrixIn, weights):
	dataMatrix = mat(dataMatrixIn)
	labelMatrix = mat(labelMatrixIn).transpose()

	m, n = shape(dataMatrix)
	r = 0
	# print "--------------"
	for i in range(m):
		print "%dth number : %f %f" % (i, (dataMatrix[i] * weights).tolist()[0][0], math.exp(labelMatrixIn[i] * math.log(sigmoid((dataMatrix[i] * weights).tolist()[0][0])) + (1 - labelMatrixIn[i]) * math.log(1 - sigmoid((dataMatrix[i] * weights).tolist()[0][0]))))
		r += labelMatrixIn[i] * math.log(sigmoid((dataMatrix[i] * weights).tolist()[0][0])) + (1 - labelMatrixIn[i]) * math.log(1 - sigmoid((dataMatrix[i] * weights).tolist()[0][0]))
		
		# print "%d , %f" % (i, math.exp(labelMatrixIn[i] * math.log(sigmoid((dataMatrix[i] * weights).tolist()[0][0])) + (1 - labelMatrixIn[i]) * math.log(1 - sigmoid((dataMatrix[i] * weights).tolist()[0][0]))))
		
	# print "--------------"
	return r

def randomMatrix(n):
	tmp = []

	for k in range(n):
		tmp.append(random.uniform(-1*maxNumber, maxNumber))

	return mat(tmp).transpose()

def gradAscent(dataMatrixIn, labelMatrixIn):
        
        dataMatrix = mat(dataMatrixIn)
        labelMatrix = mat(labelMatrixIn).transpose()
         
        #m denotes the row number
        #n denotes the column number(sample number)
        m, n = shape(dataMatrix)

        weights = randomMatrix(n)

        print weights
        
        for k in range(maxCycles):
            h = sigmoid(dataMatrix * weights)
            error = (labelMatrix - h)
            
            weights = weights + alpha * dataMatrix.transpose() * error

            # print "function = %f" % math.exp(function(dataMatrixIn, labelMatrixIn, weights))

        return weights

def count(dataMatrixIn, labelMatrixIn, weights):
	NUM_0 = 0
	NUM_1 = 0

	dataMatrix = mat(dataMatrixIn)

	h = sigmoid(dataMatrix * weights).tolist()

	for i in range(0, len(h)):
		if(h[i] > 0.5):
			h[i] = 1
		else:
			h[i] = 0

		
		if(h[i] != labelMatrixIn[i]):
			if(labelMatrixIn[i]):
				NUM_1 += 1
			else:
				NUM_0 += 1

def draw_line(X, weights): 

	N_0 = float(weights[0])
	N_1 = float(weights[1])
	N_2 = float(weights[2])

	return (-1)*(N_1 / N_2)*X + (-1)*(N_0 / N_2)

def draw_figure():
	"""
	draw in figure
	"""
	pl.plot(X1, Y1, 'or')
	pl.plot(X2, Y2, 'ob')

	startX = -5.0
	endX = 5.0
	startY = draw_line(startX, weights)
	endY = draw_line(endX, weights)

	pl.plot([startX, endX], [startY, endY])

	# set axis limits
	pl.xlim(0, 5.0)
	pl.ylim(0, 5.0)

	pl.show()

if __name__ == '__main__':

	start_time = time.time()
	
	file_path = './data_1'

	dataMatrix, labelMatrix, X1, Y1, X2, Y2 = loadData(file_path)

	weights = gradAscent(dataMatrix, labelMatrix)

	# print "weights = %f, %f, %f" % (weights[0] / weights[1], 1, weights[2] / weights[1])
	print "weights = %f, %f, %f" % (weights[0] , weights[1], weights[2])

	print "function = %f" % math.exp(function(dataMatrix, labelMatrix, weights))
	end_time = time.time()

	print "program run for %f seconds" % (end_time - start_time)
	draw_figure()
			


