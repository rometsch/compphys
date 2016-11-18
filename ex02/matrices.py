# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:28:32 2016

@author: thomas
"""
import numpy as np;

def mul_mat_vec(mat,vec):
    '''Multiply a vector vec with a matrix mat from left'''
    N_rows = mat.shape[0];
    N_cols = mat.shape[1];
    N_vec_len = vec.shape[0];
    if (N_cols!=N_vec_len):
        print("Matrix and vector dimensions don't match");
        return;
    x = np.zeros(N_rows);
    for i in range(N_rows):
        for j in range(N_cols):
            x[i] = sum(np.transpose(mat[i,:])*vec); # use componentwise multiplication
    return x;       
    
    
def solve_lin_sys_updiag(mat,vec):
    ''' Solve a system of linear equations where mat is an 
    upper diagonal matrix and vec a vector of constants'''
    N_rows = mat.shape[0];
    N_vec_len = vec.shape[0];
    if (N_rows!=N_vec_len):
        print("Dimensions of matrix and vector don't match!");
        return;
    if not(is_upper_diagonal(mat)):
        print("Matrix is not in upper diagonal form");
        return;
    x = np.zeros([N_rows]);
    if (mat[-1,-1]==0):
        print("Encountered division by zero in solve_lin_sys_updiag");
    x[-1] = vec[-1]/mat[-1,-1];
    for n in range(N_rows-2,-1,-1): #iterate from n = N_rows-2...0
        if (mat[n,n] == 0):
            print("Encountered division by zero in solve_lin_sys_updiag");
        x[n] = (vec[n] - sum(mat[n,n+1:]*x[n+1:]))/mat[n,n];
    return x;

def is_upper_diagonal(mat):
    '''Check whether the matrix is in upper diagonal form'''
    if not(is_square(mat)):
        return False;
    for i in range(1,mat.shape[0]):
        for j in range(0,i):
            if (mat[i,j] != 0):
                return False;
    return True;
    
def is_square(mat):
    '''Check whether matrix is a diagonal matrix'''
    if (mat.shape[0] == mat.shape[1]):
        return True;
    else:
        return False;
    

telephone_matrix = np.arange(1,10).reshape([3,3])
vec = np.array([10,11,12])

sol = mul_mat_vec(telephone_matrix,vec);
print("Solution of matrix*vector multiplication:\n",sol)

M = np.array([1,2,3,0,5,6,0,0,9]).reshape([3,3]);
b = np.array([10,11,12]);
x = solve_lin_sys_updiag(M,b);
print("Solution of linear system in upper diagonal form:\n",x)
print("Test solution and calculate M*x\n",mul_mat_vec(M,x))

