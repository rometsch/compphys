clear
reset

file = "single_trajectory.txt"

set title "Lorenz Attractor, sigma = 10, R= 28, beta = 8/3, v0 = (5,5,5)"

set box

set grid

unset key

set xlabel "x"
set ylabel "y"
set zlabel "z"

splot file u 2:3:4 w l

pause -1
