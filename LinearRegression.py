#The implementation overall is somewhat hacky, requires cleanup, works efficiently enough for now.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

#get our dataset
initial_import = pd.read_csv('', names=[])

#remove the csv headings from the dataset
dataset = np.array(initial_import[1:])

#function to normalize the dataset values, we require this to ensure all values are within similar range
#Scaling the values to similar range is neccessary to get the best fit, otherwise the high difference in
#range of variables leads some features dominating over others, which in turn disrupts weight calculation
#for our best fit & also may appear like an outlier in comparison to extremely low values.
#Uses the formula normalized_x = ( x-mean(x) )/( max(x)-min(x) )
def normalize(x):
	fmean = []
	frange = []
	for j in range(x[0].size):
		fmean.append( np.mean(x[:,j]) )
		frange.append( np.amax(x[:,j]) - np.amin(x[:,j]) )
	normal = ( x - fmean ) / frange
	return normal

#function to calculate the weights, uses the formula m = ( (mean(x)*mean(y)) - mean(x*y) )/( mean(x2)^2 - mean(x^2) )
def calculate_weights(x_n):
	weights = np.zeros(7)
	for j in range(x_n[0].size): 
		 weights[j] = ( (np.mean(x_n[:,j]) * np.mean(yr)) - (np.mean(x_n[:,j] * yr)) ) / ( (np.mean(x_n[:,j])**2) - (np.mean(x_n[:,j] * x_n[:,j])) )
	return weights

#function to calculate the biases, uses formula b = mean(y) - (w*mean(x))
def calculate_biases(weight, x_n):
	biases = np.zeros(7)
	for j in range(x_n[0].size):
		 biases[j] = np.mean(y) - (weight[j] * (np.mean(x_n[:,j])))
	return biases

#Creates the best fit line via the derived weights & biases
#Uses formula y = mx+b
predict = lambda X, weights, biases: (weights * X) + biases
