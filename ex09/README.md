# Lab 9 of Numerical Methods lecture
All code is written in Python. Make sure to use Python version 3!

## Lorenz Attractor

This exercise is about the Lorenz attractor.

Numerical solutions for the trajectory with inital values `(x,y,z) = (5,5,5)`
and paramter `sigma = 10`, `R = 28` and `beta = 8/3` are obtained.
See `lorenz_attractor_single_trajectory.pdf` for a plot.

Dependence of the solution on slight changes on the inital values are studied.
Choas is nicely shown here.
A plot of the distance between trajectories with close inital values
are shown in `distance_scaling.pdf`.

To perform the calculations yourself run `lorenzattractor.py` with Python3.
The integration with `dt=1e-6` is commented due to long runtime.
