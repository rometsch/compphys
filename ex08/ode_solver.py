# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:30:02 2017

@author: thomas

Numerical solver for first order ODE
"""

import numpy as np;

def adams_multon_step(F,xs,ys,h,use_corrector=True):
    """ Perform one step using Adams-Multon method wit hderivative function F.
        ys must contain the last 4 values, i.e. ys = (y_n-3, ... , y_n)
        h is the stepsize and use_corrector determines wheter 
        the correction step is to be used (defaults to True). """
        
    # Prediction
    y_pred = ys[3] + h/24*(55*F(xs[3],ys[3]) - 59*F(xs[2],ys[2]) + 37*F(xs[1],ys[1]) - 9*F(xs[0],ys[0]));
    
    # Correction
    if (use_corrector):
        y_new = ys[3] + h/24*(9*F(xs[3]+h,y_pred) + 19*F(xs[3],ys[3]) - 5*F(xs[2],ys[2]) + F(xs[1],ys[1]));
    else:
        y_new = y_pred;
    
    return y_new;
    
def adams_multon_solver(F,x0,y0,x_final,N_steps,use_corrector=True):
    """ Integrate the system given by derivative function F from 
        x0 to x_final with initial value y0 using N_steps and using the
        Adams Multon method with or without corrector step.
    """       
    # Jumpstart using RK4 method.
    (xs,h) = np.linspace(x0,x_final,N_steps,retstep=True);
    xs[0] = x0;
    ys = np.zeros(4);
    ys[0] = y0;
    for n in range(1,4):
        ys[n] = RK4_step(F,xs[n-1],ys[n-1],h);

    for n in range(4,N_steps):
        y_new = adams_multon_step(F,xs[n-3:n],ys,h,use_corrector);
        ys = np.array([ys[-3],ys[-2],ys[-1],y_new]);
        print(ys,xs[n-3:n])
        
    return ys[-1];
        
            
def RK4_step(F,x,y,h):
    """ Perform one Runge-Kutta 4th order step (locally 5th order)
        with derivative function F using stepsize h. """
    k1 = h*F(x,y);
    k2 = h*F(x + 0.5*h,y + 0.5*k1);
    k3 = h*F(x + 0.5*h,y + 0.5*k2);
    k4 = h*F(x,y+k3);
    
    return y + k1/6 + k2/3 + k3/3 + k4/6;
    
def RK4_solver(F,x0,y0,x_final,N_steps):
    """ Integrate the system given by derivative function F from 
        x0 to x_final with initial value y0 using N_steps and using the
        Runge-Kutta 4th order method with or without corrector step.
    """
    y = y0;
    (xs,h) = np.linspace(x0,x_final,N_steps,retstep=True);
    for x in xs:
        y = RK4_step(F,x,y,h);
        
    return y;
    
def derivative_function(x,y):
    """ derivative function of system in problem set """
    return y + x*x - 2*x + np.sin(x);    
    
def f_analytical_solution(x):
    return 0.6*np.exp(x) - x*x - 0.5*(np.cos(x)+np.sin(x));
    
def study_convergence(solver,filename):
    x0 = 0.0;
    y0 = 0.1;
    x_final = 2.0;

    log = np.zeros([500,2]);
        
    for i,N_steps in enumerate(range(10,5000,10)):
        y_final = solver(derivative_function,x0,y0,x_final,N_steps);
        y_final_analytic = f_analytical_solution(x_final);
        error = np.abs(y_final-y_final_analytic);
        log[i,0] = N_steps;
        log[i,1] = error;
        
    np.savetxt(filename,log);
    
def main():
#    study_convergence(RK4_solver,"RK4.txt");
    study_convergence(adams_multon_solver,"Adams_Multon_Corr.txt");

if __name__=="__main__":
    main();