#!/bin/bash

# First run
python complex_newton.py -2 2 2 -2
gnuplot -e "datafile='N400_a-2.00e+00+2.00e+00i_b2.00e+00+-2.00e+00i.txt'" plot_root_imag.plt
gnuplot -e "datafile='N400_a-2.00e+00+2.00e+00i_b2.00e+00+-2.00e+00i.txt'" plot_root_Niter.plt

python complex_newton.py -0.25 1 0.75 0.25
gnuplot -e "datafile='N400_a-2.50e-01+1.00e+00i_b7.50e-01+2.50e-01i.txt'" plot_root_imag.plt
gnuplot -e "datafile='N400_a-2.50e-01+1.00e+00i_b7.50e-01+2.50e-01i.txt'" plot_root_Niter.plt

python complex_newton.py -0.25 0.25 0.25 -0.25
gnuplot -e "datafile='N400_a-2.50e-01+2.50e-01i_b2.50e-01+-2.50e-01i.txt'" plot_root_imag.plt
gnuplot -e "datafile='N400_a-2.50e-01+2.50e-01i_b2.50e-01+-2.50e-01i.txt'" plot_root_Niter.plt

python complex_newton.py 0.05 0.05 0.075 0.025
gnuplot -e "datafile='N400_a5.00e-02+5.00e-02i_b7.50e-02+2.50e-02i.txt'" plot_root_imag.plt
gnuplot -e "datafile='N400_a5.00e-02+5.00e-02i_b7.50e-02+2.50e-02i.txt'" plot_root_Niter.plt

python complex_newton.py -1e-5 1e-5 1e-5 -1e-5
gnuplot -e "datafile='N400_a-1.00e-05+1.00e-05i_b1.00e-05+-1.00e-05i.txt'" plot_root_imag.plt
gnuplot -e "datafile='N400_a-1.00e-05+1.00e-05i_b1.00e-05+-1.00e-05i.txt'" plot_root_Niter.plt
