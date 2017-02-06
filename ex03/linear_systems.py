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
    
def solve_gauss(mat, vec):
    '''Solve the matrix vector equation M*x = b using the Gauss algorithm. '''
    M = np.copy(mat);
    b = np.copy(vec);
    N_rows = M.shape[0];
    N_vec_len = b.shape[0];
    if (N_vec_len != N_rows):
        print("Dimensions of matrix and vector don't match!");
        return;
    # Gauss algorithm
    for n in range(N_rows):
        for k in range(n+1,N_rows):
            factor = M[k,n]/M[n,n];
            M[k,n:] -= factor*M[n,n:];
            b[k] -= factor*b[n];
    # Check whether upper diagonal
    if not(is_upper_diagonal(M)):
        print("Matrix is not upper diagonal!");
        print(M);
    sol = solve_lin_sys_updiag(M,b);
    det = 1.0;
    for n in range(N_rows):
        det *= M[n,n];
    return (sol,det);
        

def part_a():
    M = np.array([[2.0,0.1,-0.2],
                  [0.05,4.2,0.032],
                  [0.12,-0.07,5.0]]);
    b = np.array([10.0,11.0,12.0]);
    (x,det) = solve_gauss(M,b);
    print("solution vector: x = ",x);
    print("det(M) = ",det);
    b_test = mul_mat_vec(M,x);
    print("test: M*x = ",b_test);
    
part_a();