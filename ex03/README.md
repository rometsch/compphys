# Lab 3 of Numerical Methods lecture
All code is written in Python. Make sure to use Python version 3!

Run the code with `python3 linear_systems.py` to calculate the solutions and produce some meaningful output.

## Gauss Method
The standard Gauss method is done in part 2.
The program will output
```python
#-------------------------------
# Numerical Methods lab 3
# Part a
#-------------------------------
solution vector: x =  [ 5.10427371  2.54065909  2.31306666]
det(M) =  42.081364
test: M*x - b =  [ 0.  0.  0.]

```
which shows that the code is working correctly.

## Pivoting
Trying to solve the second system without pivoting results in a division by 0 in the last step of the Gauss algorithm.
Python simply stops then and throws an error.

With pivoting the system can be solved.
The program produces the following output:
```python
#-------------------------------
# Numerical Methods lab 3
# part 3
#-------------------------------
calculate with pivoting:
solution vector: x =  [ 0.  1.  2.]
det(A) =  6.0
test: M*x - b =  [ 0.  0.  0.]
```
