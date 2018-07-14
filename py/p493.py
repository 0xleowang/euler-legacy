# http://stackoverflow.com/questions/27903590/statistics-optimizing-probability-calculations-within-python

from sympy import binomial

7.0 * (1 - (binomial(60, 20) / binomial(70, 20)))