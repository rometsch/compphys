# -*- coding: utf-8 -*-
"""
Thomas Rometsch

Solution to Excercise Sheet 1
"""

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
        if verbosity == 2:
            print("iteration = {0:4d} \t delta = {1:.2e} \t r = {2:.14e} \t a =  {3:.4e} \t b = {4:.4e} \t f(r) = {5:.2e}".format(Niter,delta,r,a,b,f(r)));        
# verbosity:    0 for minimal, 1 for file output, 2 for maximum
        if verbosity == 1:
            print("{0:4d} \t {1:.2e} \t {2:.14e} \t {3:.4e} \t {4:.4e} \t {5:.2e}".format(Niter,delta,r,a,b,f(r))); 
        if delta<=tol:
            break;
    print("# After {0:d} iterations found root r = {1:.14e} with delta = {2:.3e}.".format(Niter,r,delta));


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


def main():
    a = 0.0;
    b = 1.0;
    tol = 10**-14;
    verbosity=2;
    find_root(tol,a,b,bisection,verbosity);
    find_root(tol,a,b,lin_interpol,verbosity);
    find_root(tol,a,b,newton,verbosity);

if __name__=="__main__":
    main();