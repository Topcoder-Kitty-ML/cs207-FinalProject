#!/usr/bin/env python

import math
import sys
sys.path.append('../')
from genericdiff import *

def calc_du_dt(alpha, u_t):
	'''
	Calculate the rate of change of
	the unspliced RNA (reactant) with
	time.
	Implements equation 3 in the RNA
	velocity paper.
	'''
	result = alpha - u_t
	
	return result


def calc_ds_dt(gamma, u_t, s_t):
	'''
	Calculate the rate of change of
	the spliced RNA (product) with
	time.
	Implements equation 4 in the RNA
	velocity paper.
	'''
	result = u_t - gamma * s_t
	
	return result


def calc_u(alpha, u_0, t):
	'''
	Calculates the level of unspliced product (u)
	at time t. Implements equation 5 in the 
	RNA velocity paper.
	Parameters:
	alpha - Rate constant describing the transcription 
			rate
	u_0   - level of unspliced RNA (u) at time(t) = 0
	t     - Time (t)
	'''
	result = alpha * (1 - exp(-1 * t)) + u_0 * exp(-1 * t)

	return result


def calc_s(alpha, gamma, u_0, s_0, t):
	'''
	Calculates the level of spliced product (s) at
	time t. Implements equation 6 in the RNA velocity
	paper.
	Parameters:
	alpha - Rate constant describing the transcription 
			rate
	gamma - Rate constant describing the degradation
			rate
	u_0   - level of unspliced RNA (u) at time(t) = 0
	s_0   - level of spliced RNA (s) at time(t) = 0
	t     - Time (t)
	'''

	result = (exp((-1*t) * (1+gamma)) * (exp(t*(1+gamma)) * \
			alpha * (gamma-1) + \
			exp(t*gamma)*(u_0-alpha)*gamma + \
			exp(t)*(alpha-gamma*(s_0+u_0+s_0*gamma)))) / \
			(gamma * (gamma-1))


	
	return result
