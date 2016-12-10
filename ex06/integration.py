# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:54:10 2016

@author: thomas
"""
import numpy as np;


def sample_function(function, xmin, xmax, N):
    """
    Calculate an array filled with values of the provided function
    evaluated at N equally spaced points between xmin and xmax.
    Return array of funtion values, array of x values and the stepsize.
    """
    (X,h) = np.linspace(xmin,xmax,N,retstep=True);   
    Y = function(X);
    return (Y,h);
    
def integrate_2nd_newton_cotes(y,h):
    """
    Intergrate the datapoints, which are assumed to be equally spaced
    with stepsize h and an odd number of datapoints using 
    the Newton-Cotes method with a 2nd order interpolation polynomial.
    """
    N = y.size;
    if (N%2==0):
        print("Number of datapoints is not odd. Can not use this method");
        return;
    # Create multiplication mask to perform the sum with numpy array multiplication.
    # This is a lot faster than naive loops in python.
    mask = 2*np.ones(N)+2*(np.arange(N)%2);
    mask[0] = 1;
    mask[-1] = 1;
    I = np.sum(y*mask)*h/3;
    # Calculate error.
#    err = np.abs(h/90*(y[0]-3*y[1]-y[2]-y[-3]-3*y[-2]+y[-1]));
    # Calculate error
    # Sample the error at 10 % of the points. Thus use every 10th point.
    # Only use points 2...N-2, thus indices 1...N-3 to be able to use 2nd order differentiation scheme.
    err = 0;
    stepsize = 5;
    cnt = 0;
    for n in range(2,N-2,stepsize):
        cnt += 1;
        err += 1.0/90*(y[n+2]-4*y[n+1]+6*y[n]-4*y[n-1]+y[n-2]);
    err = np.abs(err*N/cnt);
    
    
    return (I,err,h);
    
    
def part_a():
    """
    Calculate everything for part a of the exercise sheet.
    """
    def func(x):
        return x + x**3;
    (Y,h) = sample_function(func,0,1,7);
    print(integrate_2nd_newton_cotes(Y,h))        


def part_b():
    """
    Calculate everything for part a of the exercise sheet.
    """

    def calc_psi(x,t,L,omega1,omega2):
        return (0<=x)*(x<=L)*(np.sin(np.pi*x/L)*np.exp(-1j*omega1*t)+np.sin(2*np.pi/L)*np.exp(-1j*omega2*t))/np.sqrt(L);
    
    def calc_dPdx(x,t,L,omega1,omega2):
        return np.abs(calc_psi(x,t,L,omega1,omega2))**2;
    
    def calc_P(t,xmin,xmax,L,omega1,omega2,N):
        (data_vec,h) = sample_function(lambda x:calc_dPdx(x,t,L,omega1,omega2), xmin, xmax, N);        
        return integrate_2nd_newton_cotes(data_vec,h);
        
    L = 2.0;
    omega1 = 3.0;
    omega2 = 4.5;
#    xmin = 0;
    xmin = 3./4*L;
    xmax = L;
    for t in [0,np.pi/1.5]:
        log = "# n\tE\th\n";
        for n in range(5,503,2):
            res = calc_P(t,xmin,xmax,L,omega1,omega2,n);
            log += "{:d}\t{:.5e}\t{:.5e}\n".format(n,res[1],res[2]);
        
        with open("errors_t{:.3f}.txt".format(t), "w") as text_file:
            text_file.write(log);
    
def main():
    part_b();
    
if __name__=="__main__":
    main();