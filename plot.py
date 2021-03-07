#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

class Plot:

	# plot the curve of a eq
	def plot_curve(self, curve_coeff, curve_type, initial_coeff):
		n = len(curve_coeff)
		y_values = []
		x_values = np.arange(-300, 300, 8)
		for x in x_values:
			y_values.append(np.sum(np.array([curve_coeff[i]*(x**(n-1-i)) for i in range(n)]))) 


		fig, ax = plt.subplots()
		ax.plot(x_values,y_values)
		ax.set(xlabel = "x", ylabel="y", title="{} of a polynomial function with coefficients: {}".format(curve_type, initial_coeff))
		ax.grid()
		plt.show()


	# plot root points, min/max, and inflection points
	def plot_points(self, coeff, data_points, points_type, poly_degree):
		x1 = [x.real for x in data_points]
		imag = [x.imag for x in data_points]

		n = len(coeff)
		x2 = [x.real for x in data_points if x.imag == 0]
		y = []
		for x in x2:
			y.append(np.sum(np.array([coeff[i]*(x**(n-1-i)) for i in range(n)])))


		fig, (ax1, ax2) = plt.subplots(2,1)
		fig.suptitle = ("{} of a {} degree polynomial".format(points_type,poly_degree))

		ax1.scatter(x1, imag)
		ax1.set_ylabel("Imaginary = Img(z)")
		ax1.grid()

		ax2.scatter(x2,y)
		ax2.set_ylabel("y = f(x)")
		ax2.set_xlabel("x = Real(z)")
		ax2.grid()

		plt.show()
