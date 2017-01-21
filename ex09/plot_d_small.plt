clear
reset

file1 = "d_dt_1.0e-03_d0_5.0e-15_T_5.0e+01.txt"

set title "Lorenz Attractor, sigma = 10, R= 28, beta = 8/3\nDistance of trajectory for inital conditions (5,5,5) and (5,5,5+5e-15)"

set box

set grid

unset key

set logscale y

set format y "%.1e"

set xlabel "t"
set ylabel "d"

plot file1 u 1:2

pause -1
