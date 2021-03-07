#!/usr/bin/env python3

import numpy as np

class Mathlib:

	# returns the roots of a polynomial eq.
	def poly_roots(self, coeff):
		return np.roots(coeff)

	# returns first derivative coeff - coeff(dy/dx)
	def d1_coeff(self,coeff):
		n = len(coeff)
		return np.array([coeff[i]*(n-1-i) for i in range(n-1)])

	# return second derivative coeff - coeff(d^2y/dx^2)
	def d2_coeff(self, d1_coeff):
		dn = len(d1_coeff)
		return np.array([d1_coeff[i]*(dn-1-i) for i in range(dn-1)])

	# returns the min/max points values of a polynomial eq.
	def poly_min_max_points(self, d1_coeff):
		return np.roots(d1_coeff)

	# returns the inflection points of a polynomial eq.
	def poly_inflection_points(self, d2_coeff):
		return np.roots(d2_coeff)