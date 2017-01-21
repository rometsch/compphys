# Lab 7 of Numerical Methods lecture
All code is written in Python. Make sure to use Python version 3!

## Run the code
Before running the simulation make three folders with names `f1`, `f2` and `f3`.

Run `integration.py` to integrate all functions with various methods.

## Integration methods
The methods implemented are
  + Trapezoidal
  + Newton-Cotes 2nd order
  + Simpsons 3/8 rule
  + Gauss-Legendre of order 2,4,8

## Plots
Plots of the errors of the integration of the three functions are generated
using gnuplot scripts.
Run `plot_f#_err.plt` (#=1,2,3) with gnuplot to produce the plots.
This will produce plots `f#_err.pdf`.
