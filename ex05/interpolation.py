# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:46:01 2016

@author: thomas
"""

import numpy as np;
import sys;
import matplotlib.pyplot as plt;

def interp(x_vals,y_vals,x):
    """
    Using Lagrange-Polynomial interpolation to 
    interpolate the data points in x_vals, y_vals
    and return the function value of the interpolated
    function for all values in x.
    x_vals,y_vals and x are assumed to be numpy arrays.
    """
    N_data = x_vals.size;
    N_sol = x.size;
    if y_vals.size != N_data:
        print("Vectors of x and function values are of unequal size!");
        return;
    sol = np.zeros(N_sol);
    for i in range(N_data):
        L = np.ones(N_sol);
        for j in np.append(np.arange(0,i),np.arange(i+1,N_data)):
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
    return heaviside(rhoT-rho,alpha=alpha)*kappa1*rho**Gamma1+heaviside(rho-rhoT,alpha=alpha)*kappa2*rho**Gamma2;
    
def calc_data_on_interval(a,b,N):
    """
    Calculate variable function pairs on the interval [a,b]
    with N points.
    """
    x = np.linspace(a,b,N);
    y = calc_P(x);
    return [x,y];
    
def plot_function_interpolation(x_vals,y_vals,x_interp,y_interp,y_true,err,show=True,save=False):
    """
    Plot the true function values alongside the interpolated values.
    """
    n = x_vals.size;
    xmin = x_vals[0];
    xmax = x_vals[-1];
    plt.clf();
    plt.title("Interpolation with n={0:3d} values. Error = {1:.2e}".format(n,err));
    plt.plot(x_interp,y_interp,'b.', label="interpolation n = {:3d}".format(n));
    plt.plot(x_interp,y_true,'g-', label="true function");
    plt.plot(x_vals,y_vals,'rd', label="true function values");
    plt.legend(loc="upper right")
    if show:
        plt.show();
    if save:
        plt.savefig("{0:.1f}_{1:.1f}_n{2:03d}.png".format(xmin,xmax,n), format="png");
    
def print_err_data(intervals,Ns,err):
    """
    Print out error data to std out.
    """
    data_str = "";
    data_str += "# n\t"
    for I in intervals:
        data_str += "{}\t".format(I);
    data_str += "\n"
    for i,n in enumerate(Ns):
        data_str += "{}\t".format(n);
        for e in err[:,i]:
            data_str += "{:.3e}\t".format(e);
        data_str += "\n";
    print(data_str);
    
    
def calc_chi_sq_error(x_interp,y_interp,y_true):
    """
    Calculate the chi squared error of the interpolated values to
    the true values.
    """
    m = x_interp.size;
    error = np.sqrt(np.sum((y_interp-y_true)**2)/m);
    return error;
    
    
def study_accuracy(rho_min,rho_max,n,show=True,save=False):
    """
    Interpolate data with n data points, produce a plot
    and study error of the interpolation.
    """    
    a = rho_min;
    b = rho_max;
    m = 200;
    [x_vals,y_vals] = calc_data_on_interval(a,b,n);
    x_interp = np.random.uniform(a,b,m);
    x_interp = np.sort(x_interp);
    y_interp = interp(x_vals,y_vals,x_interp);
    y_true = calc_P(x_interp);
    err = calc_chi_sq_error(x_interp,y_interp,y_true);
    plot_function_interpolation(x_vals,y_vals,x_interp,y_interp,y_true,err,show,save);
    return err;
    
def main(argv):
    Ns = np.arange(3,41);
    err = np.zeros([3,41-3]);
    intervals = [[4.5,5.5],[0,10],[0,30]];
    for i,I in enumerate(intervals):        
        for j,n in enumerate(Ns):
            err[i,j] = study_accuracy(I[0],I[1],n,show=False,save=True);
     
    print_err_data(intervals,Ns,err);           

if __name__=="__main__":
    main(sys.argv);