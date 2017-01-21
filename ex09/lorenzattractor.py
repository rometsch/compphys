# -*- coding: utf-8 -*-
"""
This is a python program to integrate the Lorenz Attractor.
"""

import numpy as np;

def F(v):
    """ Derivative function of the Lorenz Attractor
        Hardcoded paramteres for now."""
    sigma = 10.0;
    R = 28.0;
    beta = 8.0/3;
    x = v[0];
    y = v[1];
    z = v[2];
    xp = sigma*(y-x);
    yp = -x*z + R*x - y;
    zp = x*y - beta*z;
    return np.array([xp,yp,zp]);
    

def integrate_RK4(F,v0,dt,T,N):
    """ Integrate a system using Runge Kutta 4th order keeping N datapoints """
    step = int(T/dt/N);
    if (step < 1): step = 1;
    t = 0;
    v = v0;
    N_actual = min(N,round(T/dt));
    log = np.zeros([int(N_actual+1),4]);
    cnt = 0;
    cnt_data = 0;
    while t < T:
        if (cnt%step==0):
            log[cnt_data,:] = [t,v[0],v[1],v[2]];
            cnt_data += 1;
            print("t = {:.5e}".format(t));
        v += RK4_timestep(F,v,dt);
        t += dt;
        cnt += 1;
    return log;

def RK4_timestep(F,v,dt):
    """ Make one integration step with timestep dt using Runge-Kutta 4th order. 
    F is a function taking a vector v (numpy array or vector type 
    that supports addition and multiplication with a factor)"""
    
    k1 = dt*F(v);
    k2 = dt*F(v + 0.5*k1);
    k3 = dt*F(v + 0.5*k2);
    k4 = dt*F(v+k3);
    
    return k1/6 + k2/3 + k3/3 + k4/6;
   
   
def single_trajectory():
    v0 = np.array([5.0,5.0,5.0],dtype="float64");
    dt = 1e-3;
    N = 1e4;
    T = 50;
    log = integrate_RK4(F,v0,dt,T,N);
    np.savetxt("single_trajectory.txt", log);

def distance(dt,d0,T):
    v0 = np.array([5.0,5.0,5.0],dtype="float64");
    v1 = np.array([5.0,5.0,5.0+d0],dtype="float64");
    N = 5e2;
    log0 = integrate_RK4(F,v0,dt,T,N);
    log1 = integrate_RK4(F,v1,dt,T,N);
    d = log0[:,1:3]-log1[:,1:3];
    d = np.sqrt(np.sum(d*d,axis=1));
    out = np.zeros([d.size,2])
    out[:,0] = log0[:,0];
    out[:,1] = d;
    np.savetxt("d_dt_{:.1e}_d0_{:.1e}_T_{:.1e}.txt".format(dt,d0,T), out);


def main():
    single_trajectory();    
    distance(1e-3,1e-5,20);
#    distance(1e-6,1e-5,20);
    distance(5e-4,1e-5,20);
    distance(1e-3,5e-15,50);
    
if __name__=="__main__":
    main();
