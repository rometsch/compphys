# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:44:34 2016

@author: thomas
"""
import numpy as np;
import sys;


def main(argv):
    # parse command line options
    a = float(argv[1]) + float(argv[2])*1j;
    b = float(argv[3]) + float(argv[4])*1j
    # Set parameter    
    N = 400;
    eps = 10**-9;
    M = 200;
    
    data_string = explore_rect(a,b,N,M,eps);
    
    data_file = open("N{0:d}_a{1:.2e}+{2:.2e}i_b{3:.2e}+{4:.2e}i.txt".format(N,a.real,a.imag,b.real,b.imag),'w');
    data_file.write(data_string);
    data_file.close();
    
    

def explore_rect(a,b,N,M,eps):
    ''' Explore the convergence of of Newtons method
    (build a convergence map)
    in a rectangle given by the upper left corner a
    and lower right corner b.
    Span the rectangle using NxN gridpoints.
    Consider the the method to not converge if it exceeds M iterations
    for a given tolerance eps.
    Return a data string ready to be printed with gnuplot.'''
    data_string = "# Re(z) \t Im(z) \t Re(root) \t Im(root) \t Re(f(z)) \t Im(f(z)) \t log_10(Niter)\n";
    for n in range(N):
        data_string += "\n"; # add extra line after each x value for splot
        for k in range(N):
            z0 = (a.real + (b-a).real*float(n)/N) + (a.imag + (b-a).imag*float(k)/N)*1j;
            f = calc_fdf(z0)[0];
            [root,Niter] = solve_cNewton(calc_fdf,eps,z0,M);
            data_string += "{0:.5e}\t{1:.5e}\t{2:.5e}\t{3:.5e}\t{4:.5e}\t{5:.5e}\t{6:.5e}\n".format(z0.real,z0.imag,root.real,root.imag,f.real,f.imag,np.log(Niter)/np.log(10));
    
    return data_string;
            


def calc_fdf(z):
    ''' Return function and derivative value at z'''
    f = z*z*z - 1;
    df = 3*z*z;
    return [f,df];
    

def solve_cNewton(calc_fdf,tol,z0,N_max_iteration):
    z = z0;
    method = newton;
    Niter=0;
    delta = 0;
    for n in range(0,N_max_iteration):
        Niter = n;
        [z,delta] = method(calc_fdf(z),z);
        if delta<=tol:
            break;
    if Niter == N_max_iteration-1:
        Niter == 0; # set to 0 to indicate non convergence.
    return [z,Niter]; 

def newton(fdf_val,z):
    # Calculate x_n+1, y_n+1 and check for division by 0.
    denom = fdf_val[1];
    if np.abs(denom) == 0:
#        print("Devivsion by zero encountered in calculation of new values for z={}.Returning 0.".format(z));
        return [z,1];
    z_new = z - fdf_val[0]/denom;
    return z_new,np.abs(z_new-z);

if __name__=="__main__":
    main(sys.argv);