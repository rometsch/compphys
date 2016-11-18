# -*- coding: utf-8 -*-
"""
Thomas Rometsch

Solution to Excercise Sheet 1

Find roots of a function using the bisection,
linear interpolation and Newton's method.
"""

import sys, getopt;             # for command line arguments
import numpy as np;



# function f
def f(x,y):
    return x*y-0.1;

# Partial derivative of f w.r.t. x 
def fx(x,y):
    return y;

# Partial derivative of f w.r.t. y
def fy(x,y):
    return x;    

# function g
def g(x,y):
    return x*x + 3*y*y -2;
    
# Partial derivative of g w.r.t. x 
def gx(x,y):
    return x;

# Partial derivative of g w.r.t. y
def gy(x,y):
    return 3*y;    


# Function to call a given method untill a certain accuracy is reached.
# @param:
# tol:      desired accuracy
# a0:       start point of inital interval
# b0:       end point of inital interval
# method:   method to be used
def find_root(tol,v0,verbosity=2,N_max_iteration = 1000):
    print("# Finding root of (f,g) with Newton's method");
    method = newton;
    x = v0[0];
    y = v0[1];
    Niter=0;
    delta_x = 0;
    delta_y = 0;
    if verbosity == 1:
        print("# iteration \t delta_x \t delta_y \t x \t y \t f(x,y) \t g(x,y)")
    for n in range(0,N_max_iteration):
        Niter = n;
        [x,y,delta_x,delta_y] = method(x,y);
        if (verbosity == 2):
            print("iteration = {0:4d} \t delta_x = {1:.2e} \t delta_y = {2:.2e} \t x =  {3:.4e} \t y = {4:.4e} \t f(x,y) = {5:.2e} \t g(x,y) = {6:.2e}".format(n,delta_x,delta_y,x,y,f(x,y),g(x,y)));
# verbosity:    0 for minimal, 1 for file output, 2 for maximum
        elif (verbosity == 1):
            print("{0:d} \t {1:.2e} \t {2:.14e} \t {3:.4e} \t {4:.4e} \t {5:.2e} \t {6:.2e}".format(n,delta_x,delta_y,x,y,f(x,y),g(x,y)));
        if delta_x<=tol and delta_y<=tol:
            break;
    if Niter == N_max_iteration-1:
        print("# Warning! Reached maximum number of iterations = {}!".format(N_max_iteration))
    print("# After {0:d} iterations found root (x,y) = ({1:.3e},{2:.3e}) with delta = ({3:.3e},{4:.3e}).\n\t# Residual function values: f(x,y) = {5:.3e}, g(x,y) = {6:.3e}".format(Niter,x,y,delta_x,delta_y,f(x,y),g(x,y)));


# implement newtons method
# here a = x_n
def newton(x,y):
    # Calculate x_n+1, y_n+1 and check for division by 0.
    denom = fx(x,y)*gy(x,y)-gx(x,y)*fy(x,y);
    if denom == 0:
        print("Devivsion by zero encountered in calculation of new values for x={}, y={}".format(x,y));
    x_new = x - (f(x,y)*gy(x,y)-g(x,y)*fy(x,y))/denom;
    y_new = y - (g(x,y)*gx(x,y)-f(x,y)*gx(x,y))/denom;
    return x_new,y_new,abs(x_new - x),abs(y_new - y);


def main(argv):

    x0 = 0.5;
    y0 = 0.5;
    verbosity = 0;
    help_text = "rootfinding.py -v <verbosity> -x <initial x> -y <initial y>\n\nverbosity can be 0 for minimal output, 1 for file output, 2 for maximal output";
    # parse command line options
    try:
        opts, args = getopt.getopt(argv,"h:v::x:y",["verbosity=","x=","y="]);
    except getopt.GetoptError:
        print(help_text);
        sys.exit(2);
    for opt, arg in opts:
        if opt == '-h':
            print(help_text);
            sys.exit();
        elif opt in ("-x", "--x"):
            print(arg);
            x0 = float(arg);
        elif opt in ("-y", "--y"):
            y0 = float(arg);
        elif opt in ("-v", "--verbosity"):
            verbosity = int(arg);

    tol = 10**-14;
    max_iterations=1000;

    find_root(tol,[x0,y0],verbosity,max_iterations);

if __name__=="__main__":
    main(sys.argv[1:]);
