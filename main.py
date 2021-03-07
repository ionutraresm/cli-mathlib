#!usr/bin/env python3

import mathlib
import plot
import numpy as np
import argparse


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	math = mathlib.Mathlib()
	plt = plot.Plot()

	parser.add_argument('coeff', metavar="c", type=int, nargs="+", help="The polynomial coefficients")
	parser.add_argument("--roots", action="store_true", help="Plot the roots of a polynomial function with the given coefficients")
	parser.add_argument("--min-max", action="store_true", help="Plot the min-max points of a polynomial function with the given coefficients")
	parser.add_argument("--inflection", action="store_true", help="Plot the inflection points of a polynomial function with the given coefficients")
	parser.add_argument("--graph", action="store_true", help="Plot a polynomial function with the given coefficients")
	parser.add_argument("--first-derivative", action="store_true", help="Plot the first derivative of a polynomial function with the given coefficients")
	parser.add_argument("--second-derivative", action="store_true", help="Plot the second derivative of a polynomial function with the given coefficients")

	args = parser.parse_args()

	coeff = np.array(args.coeff)
	n = len(coeff)

	if args.roots:
		points = math.poly_roots(coeff)
		plt.plot_points(coeff, points, "Root points", n-1)

	elif args.min_max:
		d1_coeff = math.d1_coeff(coeff)
		points = math.poly_min_max_points(d1_coeff)
		plt.plot_points(coeff, points, "Min-Max points", n-1)

	elif args.inflection:
		d1_coeff = math.d1_coeff(coeff)
		d2_coeff = math.d2_coeff(d1_coeff)
		points = math.poly_inflection_points(d2_coeff)
		plt.plot_points(coeff, points, "Inflection points", n-1)

	elif args.graph:
		plt.plot_curve(coeff, "Graph", coeff)

	elif args.first_derivative:
		d1_coeff = math.d1_coeff(coeff)
		plt.plot_curve(d1_coeff, "First derivative", coeff)

	elif args.second_derivative:
		d1_coeff = math.d1_coeff(coeff)
		d2_coeff = math.d2_coeff(d1_coeff)
		plt.plot_curve(d2_coeff, "Second derivative", coeff)