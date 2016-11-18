# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:01:55 2016

@author: thomas

Class to handle matrix and vector calculations
"""

import numpy as np;

class matrix:
    ''' Class to represent a matrix and common operators. ''' 
        
    def __init__(self,M):
        ''' Initialize matrix with a numpy array. '''
        arr = np.array(M);
        if (arr.size==0):
            print("Warning! Initialized empty matrix!");
        # Save a 1d array as vector
        if (arr.size == arr.shape[0]) and (len(arr.shape)==1):
            arr = np.transpose(np.array([arr]));
        self.mat = arr;
        self.N_rows = self.mat.shape[0];
        self.N_cols = self.mat.shape[1];
    
    def __mul__(self,other):
        ''' Define multiplication '''
        A = self;
        B = other;
        return self.multiply(A,B);
        
    def __rmul__(self,other):
        ''' Define reverse multiplication '''
        A = other;
        B = self;
        return self.multiply(A,B);
        
    def __str__(self):
        ''' Implement string repesentation '''
        # Just call representation of numpy array.
        return str(self.mat);
        
    def __getitem__(self,key):
        ''' Implement indexing for matrix '''
        # Use numpy indexing to have fancy slicing.
        return matrix(self.mat[key]);
        
    def __setitem__(self,key,value):
        ''' Implement indexing for matrix '''
        # Use numpy indexing to have fancy slicing.
        self.mat[key] = value;
        
    def multiply(self,A,B):
        ''' Implement matrix multiplication '''        
        # First check that the multiplication is possible, i.e. that the dimensions match
        if (A.N_cols!=B.N_rows):
            print("Can not multiply matrices of type {0:d}x{1:d} with {2:d}x{3:d}".format(A.N_rows,A.N_cols,B.N_rows,B.N_cols))
            return np.array([]);
        # This is A*B, so the size of the new matrix will be rows(A) x cols(B)
        C = matrix(np.zeros([A.N_rows,B.N_cols]));
        for i in range(A.N_rows): # all rows of A
            row = A.mat[i,:];
            for j in range(B.N_cols): # with all cols of B
                col = np.transpose(B.mat[:,j]);
                C[i,j] = sum(row*col);  # use componentwise multiplication of numpy here.
        # Return scalar, if dimension is 1x1;
        if (C.N_cols == 1) and (C.N_rows == 1):
            return C.mat[0,0];
        return C;
        
    def solve_lin_sys_updiag(self,b):
        ''' Solve a system of linear equations with self.mat as 
            coefficient matrix, assuming its in upper diagonal form
            and b as vector of constant s.t. mat*x = b.
            Return solution vector x.
            b must be an object of this class with dimensions N_rows x 1'''
        if not(b.N_rows == self.N_rows and b.N_cols == 1):
            print("Given vector of constants doesn't match dimension of matrix. Return nothing!");
            return;
        if not(self.is_upper_diagonal):
            print("Matrix is not in upper diagonal form. Can not solve system of linear equations using this routine! Return nothing.")
            return;
        x = matrix(np.zeros([self.N_rows,1]));
        if (self.mat[-1,-1]==0):
            print("Encountered division by zero in solve_lin_sys_updiag");
        x[-1,0] = b.mat[-1,0]/self.mat[-1,-1];
        for n in range(self.N_rows-2,-1,-1): #iterate from n = N_rows-2...0
            if (self.mat[n,n] == 0):
                print("Encountered division by zero in solve_lin_sys_updiag");
            print("matrix\n",self[n,n+1:])
            print("vector\n",b[n+1:,0])
            x[n,0] = (b.mat[n,0] - self[n,n+1:]*b[n+1:,0])/self.mat[n,n];
        return x;
    
    def is_square(self):
        '''Check whether matrix is a diagonal matrix'''
        if (self.N_rows == self.N_cols):
            return True;
        else:
            return False;
            
    def is_upper_diagonal(self):
        '''Check whether the matrix is in upper diagonal form'''
        if not(self.is_square()):
            return False;
        for i in range(1,self.N_rows):
            for j in range(0,i):
                if (self.mat[i,j] != 0):
                    return False;
        return True;