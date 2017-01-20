# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:54:10 2016

@author: thomas
"""
import numpy as np;
import matplotlib.pyplot as plt;


def sample_function(function, limits, N):
    """
    Calculate an array filled with values of the provided function
    evaluated at N equally spaced points between the two numbers in limits.
    Return array of funtion values, array of x values and the stepsize.
    """
    xmin = limits[0];
    xmax = limits[1];
    (X,h) = np.linspace(xmin,xmax,N,retstep=True);   
    Y = function(X);
    return (Y,h);
    
def integrate_2nd_newton_cotes(function,limits,N):
    """
    Intergrate the datapoints, which are assumed to be equally spaced
    with stepsize h and an odd number of datapoints using 
    the Newton-Cotes method with a 2nd order interpolation polynomial.
    """
    (ys,h) = sample_function(function,limits,N);
    if (N%2==1):        
    # Create multiplication mask to perform the sum with numpy array multiplication.
    # This is a lot faster than naive loops in python.
        mask = 2*np.ones(N)+2*(np.arange(N)%2);
        mask[0] = 1;
        mask[-1] = 1;
        I = np.sum(ys*mask)*h/3;
    else:
        # If number of datapoints is even, use a 4 point rule for 
        # the last subinterval. Its also of order h^5.
        mask = h/3*2*np.ones(N)+2*(np.arange(N)%2);
        mask[0] = h/3;
        mask[-1] = 3*h/8;
        mask[-2] = 9*h/8;
        mask[-3] = 9*h/8;
        mask[-4] = h/3 + 3*h/8; # first term from 3 point rule, second term from 4 point rule
        I = np.sum(ys*mask);
            
    return (I,h);
    
def integrate_trapezoidal(function,limits,N):
    """
    Intergrate function using the trapezoidal rule over the interval
    given by the two numbers in limits.
    """
    (ys,h) = sample_function(function,limits,N);
    mask = 2.0*np.ones(N);
    mask[0] = 1;
    mask[-1] = 1;
    I = np.sum(ys*mask)*h/2;
    
    return (I,h);
    
def integrate_gauss_legendre_single_2(function,limits):
    """ Integrate function over a single interval given by limits. """
    # map x values
    xmin = limits[0];
    xmax = limits[1];    
    def t(x):
        return 0.5*(xmin + xmax) + x*0.5*(xmax - xmin);
    x1 = t(-0.5773502692);
    x2 = t(0.5773502692);
    # Calculate integral.s
    I = 0.5*(xmax-xmin)*(function(x1) + function(x2));
    return I;
    
def integrate_gauss_legendre_2(function,limits,N):
    xmin = limits[0];
    xmax = limits[1];
    h = (xmax - xmin)/N;
    I = 0;
    for n in range(N):
        I += integrate_gauss_legendre_single_2(function,[xmin+n*h,xmin+(n+1)*h]);
    return (I,h);

def integrate_gauss_legendre_single_4(f,limits):
    """ Integrate function over a single interval given by limits. """
    # map x values
    xmin = limits[0];
    xmax = limits[1];    
    def t(x):
        return 0.5*(xmin + xmax) + x*0.5*(xmax - xmin);
    x1 = t(-0.8611363116);
    x2 = t(0.8611363116);
    x3 = t(-0.3394810436);
    x4 = t(0.3394810436);
    A1 = 0.3478548451;
    A2 = 0.3478548451;
    A3 = 0.6521451549;
    A4 = 0.6521451549;
    # Calculate integral.s
    I = 0.5*(xmax-xmin)*(A1*f(x1) + A2*f(x2) + A3*f(x3) + A4*f(x4));
    return I;
    
def integrate_gauss_legendre_4(function,limits,N):
    xmin = limits[0];
    xmax = limits[1];
    h = (xmax - xmin)/N;
    I = 0;
    for n in range(N):
        I += integrate_gauss_legendre_single_4(function,[xmin+n*h,xmin+(n+1)*h]);    
    return (I,h);
    
#def integrate_gauss_legendre_single_8(function,limits):
#    """ Integrate function over a single interval given by limits. """
#    # map x values
#    xmin = limits[0];
#    xmax = limits[1];    
#    def t(x):
#        return 0.5*(xmin + xmax) + x*0.5*(xmax - xmin);
#    x = np.array([   t(-0.9602898565), t(0.9602898565),
#                    t(-0.7966664774), t(0.7966664774),
#                    t(-0.5255324099), t(0.5255324099),
#                    t(-0.1834346425), t(0.1834346425) ]);
#    A = np.array([  0.1012285363, 0.1012285363,
#                    0.2223810345, 0.2223810345,
#                    0.3137066459, 0.3137066459,
#                    0.3626837834, 0.3626837834 ]);
#    # Calculate integral.s
#    I = 0.5*(xmax-xmin)*np.sum(A*function(x));
#    return I;
    
def integrate_gauss_legendre_single_8(f,limits):
    """ Integrate function over a single interval given by limits. """
    # map x values
    xmin = limits[0];
    xmax = limits[1];    
    def t(x):
        return 0.5*(xmin + xmax) + x*0.5*(xmax - xmin);
    x1 = t(-0.9602898565);
    x2 = t(0.9602898565);
    x3 = t(-0.7966664774);
    x4 = t(0.7966664774);
    x5 = t(-0.5255324099);
    x6 = t(0.5255324099);
    x7 = t(-0.1834346425);
    x8 = t(0.1834346425);
    A1 = 0.1012285363;
    A2 = 0.1012285363;
    A3 = 0.2223810345;
    A4 = 0.2223810345;
    A5 = 0.3137066459;
    A6 = 0.3137066459;
    A7 = 0.3626837834;
    A8 = 0.3626837834;
    # Calculate integral.s
    I = 0.5*(xmax-xmin)*(A1*f(x1) + A2*f(x2) + A3*f(x3) + A4*f(x4) + A5*f(x5) + A6*f(x6) + A7*f(x7) + A8*f(x8));
    return I;
    
    
def integrate_gauss_legendre_8(function,limits,N):
    xmin = limits[0];
    xmax = limits[1];
    h = (xmax - xmin)/N;
    I = 0;
    for n in range(N):
        I += integrate_gauss_legendre_single_8(function,[xmin+n*h,xmin+(n+1)*h]);    
    return (I,h);

def f1(x):
    return np.exp(x)*np.cos(x);
    
def f2(x):
    return np.exp(x);
    
def f3(x):
    y = (x<0)*np.exp(2*x) + (x>=0)*(x-2*np.cos(x)+4);
    return y;
    
def I1():
    # Solution of integral 1.
    return 0.5*(np.exp(np.pi/2)-1);
    
def I2():
    # Solution of integral 2.
    return np.exp(3)-np.exp(-1);

def I3():
    # Solution of integral 3.
    return 1-2*np.sin(1)-0.5/np.exp(2)+4;
    
def plot_error(E,h,name):
    """Plot error vs. h in a log-log plot"""
    print(np.min(h));    
    plt.clf();
#    for errs,hs in zip(E,h):
#        plt.loglog(hs,errs);
    plt.loglog(h,E);    
    plt.title(name);
    plt.xlabel("h");
    plt.ylabel("error");
    plt.grid();
    plt.show();
    
def test_method_on_function(method,func,limits,analytical_solution,N_min,N_max):
    """ Test the provided method by integrating the function func over
        over the interval given by limits and compare it to the solution
        obtained by calling the sol_ana.
        Repead the test for all integer values as number of datapoints between
        N_min and N_max and return errors and hs.
    """
    
    errors = [];
    hs = [];
    for N in range(N_min,N_max+1):
        (I,h) = method(func,limits,N);
        error = np.abs(I - analytical_solution);
        
        errors.append(error);
        hs.append(h);
        
    return (errors,hs);
    
def test_method(method,N_min,N_max):
    """ Test the given method on all three functions and make a plot
        showing error vs h"""
    limits1 = [0,np.pi/2];
    limits2 = [-1.0,3.0];
    limits3 = [-1.0,1.0];
    
    integrator_name = method.__name__;    
    
    (err1,h1) = test_method_on_function(method,f1,limits1,I1(),N_min,N_max);
    
    np.savetxt("f1/{}.txt".format(integrator_name), np.array([h1,err1]).transpose());
    
    (err2,h2) = test_method_on_function(method,f2,limits2,I2(),N_min,N_max);
    np.savetxt("f2/{}.txt".format(integrator_name), np.array([h2,err2]).transpose());
    
    (err3,h3) = test_method_on_function(method,f3,limits3,I3(),N_min,N_max);
    np.savetxt("f3/{}.txt".format(integrator_name), np.array([h3,err3]).transpose());

def main():
    test_method(integrate_2nd_newton_cotes,5,501)
#    print(integrate_gauss_legendre_2(f2,[-1,3],5))
    
if __name__=="__main__":
    main();