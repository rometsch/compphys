#!/bin/bash

# Find root using bisection method
python3 rootfinding.py -v 1 -m bisection > result_bisection.txt

# Find root using linear interpolation method
python3 rootfinding.py -v 1 -m lin_interpol > result_linear_interplation.txt

# Find root using Newton's method
python3 rootfinding.py -v 1 -m newton > result_newton.txt

# Produce plot
gnuplot plot_error.plt
