# -*- coding: utf-8 -*-
"""
Thomas Rometsch

Solution to Excercise Sheet 1

Find roots of a function using the bisection,
linear interpolation and Newton's method.
"""

import sys, getopt;             # for command line arguments
import numpy as np;


# Define function
def f(x):
    return np.exp(np.sqrt(5)*x) - 13.5*np.cos(0.1*x) + x*x*x*x*25;

# Derivative of function f
def fp(x):
    return np.sqrt(5)*np.exp(np.sqrt(5)*x) + 1.35*np.sin(0.1*x) + x*x*x*100;

# Function to call a given method untill a certain accuracy is reached.
# @param:
# tol:      desired accuracy
# a0:       start point of inital interval
# b0:       end point of inital interval
# method:   method to be used
def find_root(tol,a,b,method,verbosity=2,N_max_iteration = 1000):
    print("# Finding root of f with {} method:".format(method.__name__));
    if verbosity == 1:
        print("# iteration \t delta \t r \t a \t b \t f(r)")
    Niter = 0;      # iteration counter
    for n in range(0,N_max_iteration):
        [r,a,b,delta] = method(a,b);
        Niter+=1;
        if (verbosity == 2):
            print("iteration = {0:4d} \t delta = {1:.2e} \t r = {2:.14e} \t a =  {3:.4e} \t b = {4:.4e} \t f(r) = {5:.2e}".format(Niter,delta,r,a,b,f(r)));
# verbosity:    0 for minimal, 1 for file output, 2 for maximum
        elif (verbosity == 1):
            print("{0:d} \t {1:.2e} \t {2:.14e} \t {3:.4e} \t {4:.4e} \t {5:.2e}".format(Niter,delta,r,a,b,f(r)));
        if delta<=tol:
            break;
    print("# After {0:d} iterations found root r = {1:.16e} with delta = {2:.3e}.".format(Niter,r,delta));


# implement bisection method
def bisection(a,b):
    mu = (a+b)/2;
    if f(mu) == 0:
        return mu,a,b,0;
    if f(mu)*f(a)<0:
        b = mu;
    else:
        a = mu;
    return mu,a,b,b-a;

# implement linear interpolation method
def lin_interpol(a,b):
    c = b-f(b)*(b-a)/(f(b)-f(a));
    if f(c) == 0:
        return c,a,b,0;
    if f(c)*f(a)<0:
        b=a;
    else:
        a=c;
    return c,a,b,np.abs(f(c));

# implement newtons method
# here a = x_n
def newton(a,b):
    r = a - f(a)/fp(a);
    if f(r) == 0:
        return r,r,r,0;
    return r,r,0,abs(r-a);


def main(argv):

    method = "newton";
    verbosity = 0;
    # parse command line options
    try:
        opts, args = getopt.getopt(argv,"hm:v:",["method=","verbosity="]);
    except getopt.GetoptError:
        print("rootfinding.py -m <method> -v <verbosity>\n\nmethod can be bisection, lin_interpol or newton\n\nverbosity can be 0 for minimal output, 1 for file output, 2 for maximal output");
        sys.exit(2);
    for opt, arg in opts:
        if opt == '-h':
            print("rootfinding.py -m <method> -v <verbosity>\n\nmethod can be bisection, lin_interpol or newton\n\nverbosity can be 0 for minimal output, 1 for file output, 2 for maximal output");
            sys.exit();
        elif opt in ("-m", "--method"):
            method = arg;
        elif opt in ("-v", "--verbosity"):
            verbosity = int(arg);

    methods_list = {"bisection":bisection , "lin_interpol": lin_interpol , "newton":newton };
    a = 0;
    b = 1;
    tol = 10**-14;
    max_iterations=1000;
    find_root(tol,a,b,methods_list[method],verbosity,max_iterations);

if __name__=="__main__":
    main(sys.argv[1:]);
