################################################################################
# Using "/" and "\" to simulate a simple random walk.
# Just for fun XD
# 
# Author: Eleven Wang
#
# Next: Waving hand
################################################################################

from random import *
from string import join
import sys

#------------------------------------------------------------------------------
# Configuration
x_size = 50
try:
    prob_go_up = float(sys.argv[1])
except:
    prob_go_up = 0.5
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Generate simple random walk.
walk = []
for i in range(x_size):
    walk.append(1) if random() < prob_go_up else walk.append(-1)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Generate the coordinates of each walk step.
y = 0
coordinates = {(0, 0): walk[0]}
for x in range(1, len(walk)):
    step = walk[x]
    if step == walk[x - 1]:
        y += step
    coordinates[(x, y)] = step
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Not finish
y_upper_boundary = 0
y_lower_boundary = 0
for c in coordinates:
	if y_upper_boundary < c[1]:
		y_upper_boundary = c[1]
	if y_lower_boundary > c[1]:
		y_lower_boundary = c[1]
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Set vertical size
y_size = y_upper_boundary - y_lower_boundary + 1
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Initialize the graph as a list
graph_list = []
for y in range(y_size):
	graph_list.append([])
	for x in range(x_size):
		graph_list[y].append(" ")
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Draw the graph
for c in coordinates:
	y_for_graph = y_upper_boundary - c[1]
	if coordinates[c] is 1:
	    graph_list[y_for_graph][c[0]] = "/"
	else:
		graph_list[y_for_graph][c[0]] = "\\"
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Merge lines to graph, then print it.
graph = "\n                Simple Ramdom Walk (p = %.3f)\n\n" % prob_go_up
for line in graph_list:
    graph += "|"
    graph += join(line, "")
    graph += "\n"
print graph
#------------------------------------------------------------------------------