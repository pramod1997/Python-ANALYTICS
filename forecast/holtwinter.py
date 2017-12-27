from __future__ import division
import pandas as pd
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt



import numpy as np


from sys import exit
from math import sqrt
from numpy import array
from scipy.optimize import fmin_l_bfgs_b
from django.contrib.staticfiles.templatetags.staticfiles import static
import os





def RMSE(params, *args):

	Y = args[0]
	#####	type = args[1]
	####introduced user input
	type= choice
	rmse = 0

	if type == 'linear':

		alpha, beta = params
		a = [Y[0]]
		b = [Y[1] - Y[0]]
		y = [a[0] + b[0]]

		for i in range(len(Y)):

			a.append(alpha * Y[i] + (1 - alpha) * (a[i] + b[i]))
			b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
			y.append(a[i + 1] + b[i + 1])

	else:

		alpha, beta, gamma = params
		###m = args[2]    removed command line 
		m= new_m		
		a = [sum(Y[0:m]) / float(m)]
		b = [(sum(Y[m:2 * m]) - sum(Y[0:m])) / m ** 2]

		if type == 'additive':

			s = [Y[i] - a[0] for i in range(m)]
			y = [a[0] + b[0] + s[0]]

			for i in range(len(Y)):

				a.append(alpha * (Y[i] - s[i]) + (1 - alpha) * (a[i] + b[i]))
				b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
				s.append(gamma * (Y[i] - a[i] - b[i]) + (1 - gamma) * s[i])
				y.append(a[i + 1] + b[i + 1] + s[i + 1])

		elif type == 'multiplicative':

			s = [Y[i] / a[0] for i in range(m)]
			y = [(a[0] + b[0]) * s[0]]

			for i in range(len(Y)):

				a.append(alpha * (Y[i] / s[i]) + (1 - alpha) * (a[i] + b[i]))
				b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
				s.append(gamma * (Y[i] / (a[i] + b[i])) + (1 - gamma) * s[i])
				y.append((a[i + 1] + b[i + 1]) * s[i + 1])

		else:

			exit('Type must be either linear, additive or multiplicative')
		
	rmse = sqrt(sum([(m - n) ** 2 for m, n in zip(Y, y[:-1])]) / len(Y))

	return rmse

def linear(x, fc, alpha = None, beta = None):

	Y = x[:]

	if (alpha == None or beta == None):

		initial_values = array([0.3, 0.1])
		boundaries = [(0, 1), (0, 1)]
		type = 'linear'

		parameters = fmin_l_bfgs_b(RMSE, x0 = initial_values, args = (Y, type), bounds = boundaries, approx_grad = True)
		alpha, beta = parameters[0]

	a = [Y[0]]
	b = [Y[1] - Y[0]]
	y = [a[0] + b[0]]
	rmse = 0

	for i in range(len(Y) + fc):

		if i == len(Y):
			Y.append(a[-1] + b[-1])

		a.append(alpha * Y[i] + (1 - alpha) * (a[i] + b[i]))
		b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
		y.append(a[i + 1] + b[i + 1])

	rmse = sqrt(sum([(m - n) ** 2 for m, n in zip(Y[:-fc], y[:-fc - 1])]) / len(Y[:-fc]))

	return Y[-fc:], alpha, beta, rmse

def additive(x, m, fc, alpha = None, beta = None, gamma = None):

	Y = x[:]

	if (alpha == None or beta == None or gamma == None):

		initial_values = array([0.3, 0.1, 0.1])
		boundaries = [(0, 1), (0, 1), (0, 1)]
		type = 'additive'

		parameters = fmin_l_bfgs_b(RMSE, x0 = initial_values, args = (Y, type, m), bounds = boundaries, approx_grad = True)
		alpha, beta, gamma = parameters[0]

	a = [sum(Y[0:m]) / float(m)]
	b = [(sum(Y[m:2 * m]) - sum(Y[0:m])) / m ** 2]
	s = [Y[i] - a[0] for i in range(m)]
	y = [a[0] + b[0] + s[0]]
	rmse = 0

	for i in range(len(Y) + fc):

		if i == len(Y):
			Y.append(a[-1] + b[-1] + s[-m])

		a.append(alpha * (Y[i] - s[i]) + (1 - alpha) * (a[i] + b[i]))
		b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
		s.append(gamma * (Y[i] - a[i] - b[i]) + (1 - gamma) * s[i])
		y.append(a[i + 1] + b[i + 1] + s[i + 1])

	rmse = sqrt(sum([(m - n) ** 2 for m, n in zip(Y[:-fc], y[:-fc - 1])]) / len(Y[:-fc]))

	return Y[-fc:], alpha, beta, gamma, rmse

def multiplicative(x, m, fc, alpha = None, beta = None, gamma = None):

	Y = x[:]

	if (alpha == None or beta == None or gamma == None):

		initial_values = array([0.0, 1.0, 0.0])
		boundaries = [(0, 1), (0, 1), (0, 1)]
		type = 'multiplicative'

		parameters = fmin_l_bfgs_b(RMSE, x0 = initial_values, args = (Y, type, m), bounds = boundaries, approx_grad = True)
		alpha, beta, gamma = parameters[0]

	a = [sum(Y[0:m]) / float(m)]
	b = [(sum(Y[m:2 * m]) - sum(Y[0:m])) / m ** 2]
	s = [Y[i] / a[0] for i in range(m)]
	y = [(a[0] + b[0]) * s[0]]
	rmse = 0

	for i in range(len(Y) + fc):

		if i == len(Y):
			Y.append((a[-1] + b[-1]) * s[-m])

		a.append(alpha * (Y[i] / s[i]) + (1 - alpha) * (a[i] + b[i]))
		b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
		s.append(gamma * (Y[i] / (a[i] + b[i])) + (1 - gamma) * s[i])
		y.append((a[i + 1] + b[i + 1]) * s[i + 1])

	rmse = sqrt(sum([(m - n) ** 2 for m, n in zip(Y[:-fc], y[:-fc - 1])]) / len(Y[:-fc]))

	return Y[-fc:], alpha, beta, gamma, rmse

#################################################

def mainfn(seasonal_length, forecast_period, hw,path):


	#forecast=input("Enter forecasting period for eg 48 , 50 or 100   ")
	#choice=raw_input("Enter the type - additive, linear , multiplicative  ")
	#new_m= input("Enter season length in points like 12 or any integer ")
	#########

	forecast=forecast_period
	new_m=seasonal_length
	choice= hw

	column_names=[]

	#  Holt-Winters default parameters
	hw_alpha = 0.26      #  Based on robust optimization in Gelper 2007,
	hw_beta  = 0.19      #  for Gaussian, fat tail, and outlier data.
	hw_gamma = 0.5
	df = pd.read_csv(path, index_col=0)

	for i in df.columns:
		column_names=i
	


	#print column_names

	# convert index from string yyyy-mm to datetime object
	df.index = pd.to_datetime(df.index)
	x = df[column_names].tolist()
	# fc: forecasting period, m: season length (in points)
	##forecast =48
	#season_len = 12
	if hw == 'additive':
		Y, alpha, beta, gamma, rmse = additive(x[:-forecast], m=seasonal_length, fc=forecast, alpha = hw_alpha, beta = hw_beta, gamma = hw_gamma)

	if hw == 'linear':
		Y, alpha, beta,  rmse = linear(x[:-forecast],fc=forecast, alpha = hw_alpha, beta = hw_beta)

	if hw == 'multiplicative':
		Y, alpha, beta, gamma, rmse = multiplicative(x[:-forecast], m=seasonal_length, fc=forecast, alpha = hw_alpha, beta = hw_beta, gamma = hw_gamma)


	newY = [np.nan]*len(x)
	j = 0
	for i in range(len(x[:-forecast]),len(x)):
	    newY[i] = Y[j]
	    j += 1
	#ix = pd.DatetimeIndex(start=df.index[0], periods=len(df)+forecast, freq='M')
	#x = pd.DataFrame(df["Passengers"], index=ix)
	plt.plot(x, label='Original')
	plt.plot(newY, label='Prediction')
	plt.legend(loc='best')
	##plt.show()
	if (os.path.exists("/home/pramod/Desktop/analytics/forecastdjango/static/forecast/foo1.png")):
		### delete the file 
		os.remove("/home/pramod/Desktop/analytics/forecastdjango/static/forecast/foo1.png")
		plt.savefig("/home/pramod/Desktop/analytics/forecastdjango/static/forecast/foo1.png", bbox_inches='tight')

	else :

		plt.savefig("/home/pramod/Desktop/analytics/forecastdjango/static/forecast/foo1.png", bbox_inches='tight')
	plt.close()
