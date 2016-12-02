# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:46:01 2016

@author: thomas
"""

import numpy as np;

def interp(x_vals,y_vals,x):
    """
    Using Lagrange-Polynomial interpolation to 
    interpolate the data points in x_vals, y_vals
    and return the function value of the interpolated
    function for all values in x.
    x_vals,y_vals and x are assumed to be numpy arrays.
    """
    N = x_vals.size;
    if y_vals.size != N:
        print("Vectors of x and function values are of unequal size!");
        return;
    sol = np.zeros(N);
    for i in range(N):
        L = np.ones(N);
        for j in np.append(np.arange(0,i),np.arange(i+1,N)):
            L *= (x - x_vals[j])/(x_vals[i]-x_vals[j]);
        sol += y_vals[i]*L;
    return sol;
    
def heaviside(x,alpha):
    """
    Approximation to the Heaviside function.
    """
    return 1.0/(1+np.exp(-2*alpha*x));
    
def calc_P(rho,rhoT=5.0,kappa1=20.0,kappa2=1.0,Gamma1=4.0/3,Gamma2=5.0/3,alpha=5):
    """
    Calc P via the hybrid Equation of States.
    """
    return heaviside(rhoT-rho)*kappa1*rho**Gamma1+heaviside(rho-rhoT)*kappa2*rho**Gamma2;
    
