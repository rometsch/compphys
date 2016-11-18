# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:33:19 2016

@author: thomas
"""

import nonlinear_system;

tol = 10**-12
verbosity = 0;
N_max_iter = 1000;

v0 = [0.5,0.5];
v1 = [-1,0];
v2 = [-0.5,0.5];
v3 = [0.5,-0.5];

for v in [v0,v1,v2,v3]:
    nonlinear_system.find_root(tol,v,verbosity,N_max_iter);
    print("\n");